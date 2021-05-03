package main

import (
	"archive/tar"
	"bytes"
	"fmt"
	"io"
	"log"
	"os"
	"os/exec"
	"path/filepath"
	"strings"

	"github.com/blakesmith/ar"
	"github.com/julien-sobczak/deb822"
)

func main() {
	if len(os.Args) < 2 {
		log.Fatalf("Missing package archive(s)")
	}

	// Read the database
	db, _ := loadDatabase()

	// Unpack and configure the archive(s)
	for _, archivePath := range os.Args[1:] {
		processArchive(db, archivePath)
	}

	// Note: we don't manage a queue to defer the configuration of packages
	// as we are going to test with a single package.
}

//
// Dpkg Database
//

type Database struct {
	// File /var/lib/dpkg/status
	Status deb822.Document
	// Packages under /var/lib/dpkg/info/
	Packages []*PackageInfo
}

type PackageInfo struct {
	Paragraph deb822.Paragraph // Extracted package section in /var/lib/dpkg/status

	// info
	Files             []string          // File <name>.list
	Conffiles         []string          // File <name>.conffiles
	MaintainerScripts map[string]string // File <name>.{preinst,prerm,postinst,postrm}

	Status      string // Current status (as also present in Paragraph under the field Status)
	StatusDirty bool   // True to ask for sync
}

func (p *PackageInfo) Name() string {
	// Extract the package name from its section in /var/lib/dpkg/status
	return p.Paragraph.Value("Package")
}

func (p *PackageInfo) Version() string {
	// Extract the package version from its section in /var/lib/dpkg/status
	return p.Paragraph.Value("Version")
}

func (p *PackageInfo) isConffile(path string) bool {
	for _, conffile := range p.Conffiles {
		if path == conffile {
			return true
		}
	}
	return false
}

// InfoPath returns the path a file under /var/lib/dpkg/info.
// Ex: "list" => /var/lib/dpkg/info/hello.list
func (p *PackageInfo) InfoPath(filename string) string {
	return filepath.Join("/var/lib/dpkg", p.Name()+"."+filename)
}

// We now add a method to change the package status
// and make sure the section in the status file is updated too.

func (p *PackageInfo) SetStatus(new string) {
	p.Status = new
	p.StatusDirty = true
	// Override in DEB 822 document used to write the status file
	old := p.Paragraph.Values["Status"]
	parts := strings.Split(old, " ")
	p.Paragraph.Values["Status"] = fmt.Sprintf("%s %s %s", parts[0], parts[1], new)
}

// Now, we are ready to read the database directory to initialize the structs.

func loadDatabase() (*Database, error) {
	// Load the status file
	f, _ := os.Open("/var/lib/dpkg/status")
	parser, _ := deb822.NewParser(f)
	status, _ := parser.Parse()

	// Read the info directory
	var packages []*PackageInfo
	for _, statusParagraph := range status.Paragraphs {
		statusField := statusParagraph.Value("Status") // Ex: "install ok installed"
		statusValues := strings.Split(statusField, " ")

		pkg := PackageInfo{
			Paragraph:         statusParagraph,
			MaintainerScripts: make(map[string]string),
			Status:            statusValues[2],
			StatusDirty:       false,
		}

		// Read configuration files
		pkg.Files, _ = ReadLines(pkg.InfoPath("list"))
		pkg.Conffiles, _ = ReadLines(pkg.InfoPath("conffiles"))

		// Read maintainer scripts
		for _, script := range []string{"preinst", "postinst", "prerm", "postrm"} {
			scriptPath := pkg.InfoPath(script)
			if _, err := os.Stat(scriptPath); !os.IsNotExist(err) {
				content, err := os.ReadFile(scriptPath)
				if err != nil {
					return nil, err
				}
				pkg.MaintainerScripts[script] = string(content)
			}
		}
		packages = append(packages, &pkg)
	}

	return &Database{
		Status:   status,
		Packages: packages,
	}, nil
}

// Now we are ready to process the archive to install.

func processArchive(db *Database, archivePath string) error {

	// Read the debian archive file
	f, err := os.Open(archivePath)
	if err != nil {
		return err
	}
	defer f.Close()
	reader := ar.NewReader(f)

	// Skip debian-binary
	reader.Next()

	// control.tar
	reader.Next()
	var bufControl bytes.Buffer
	io.Copy(&bufControl, reader)

	pkg, err := parseControl(db, bufControl)
	if err != nil {
		return err
	}

	// Add new package in database
	db.Packages = append(db.Packages, pkg)
	db.Sync()

	// data.tar
	reader.Next()
	var bufData bytes.Buffer
	io.Copy(&bufData, reader)

	fmt.Printf("Preparing to unpack %s ...\n", filepath.Base(archivePath))

	if err := pkg.Unpack(bufData); err != nil {
		return err
	}
	if err := pkg.Configure(); err != nil {
		return err
	}

	db.Sync()

	return nil
}

// parseControl processes the control.tar archive.
func parseControl(db *Database, buf bytes.Buffer) (*PackageInfo, error) {

	pkg := PackageInfo{
		MaintainerScripts: make(map[string]string),
		Status:            "not-installed",
		StatusDirty:       true,
	}

	tr := tar.NewReader(&buf)

	for {
		hdr, err := tr.Next()
		if err == io.EOF {
			break // End of archive
		}
		if err != nil {
			return nil, err
		}

		// Read the file content
		var buf bytes.Buffer
		if _, err := io.Copy(&buf, tr); err != nil {
			return nil, err
		}

		switch filepath.Base(hdr.Name) {
		case "control":
			parser, _ := deb822.NewParser(strings.NewReader(buf.String()))
			document, _ := parser.Parse()
			controlParagraph := document.Paragraphs[0]

			// Copy control fields and add the Status field in second position
			pkg.Paragraph = deb822.Paragraph{
				Values: make(map[string]string),
			}

			// Make sure the field "Package' comes first, then "Status", then remaining fields.
			pkg.Paragraph.Order = append(pkg.Paragraph.Order, "Package", "Status")
			pkg.Paragraph.Values["Package"] = controlParagraph.Value("Package")
			pkg.Paragraph.Values["Status"] = "install ok non-installed"
			for _, field := range controlParagraph.Order {
				if field == "Package" {
					continue
				}
				pkg.Paragraph.Order = append(pkg.Paragraph.Order, field)
				pkg.Paragraph.Values[field] = controlParagraph.Value(field)
			}
		case "conffiles":
			pkg.Conffiles = SplitLines(buf.String())
		case "prerm":
			fallthrough
		case "preinst":
			fallthrough
		case "postinst":
			fallthrough
		case "postrm":
			pkg.MaintainerScripts[filepath.Base(hdr.Name)] = buf.String()
		}
	}

	return &pkg, nil
}

// Unpack processes the data.tar archive.
func (p *PackageInfo) Unpack(buf bytes.Buffer) error {
	if err := p.runMaintainerScript("preinst"); err != nil {
		return err
	}

	fmt.Printf("Unpacking %s (%s) ...\n", p.Name(), p.Version())

	tr := tar.NewReader(&buf)
	for {
		hdr, err := tr.Next()
		if err == io.EOF {
			break // End of archive
		}
		if err != nil {
			return err
		}

		var buf bytes.Buffer
		if _, err := io.Copy(&buf, tr); err != nil {
			return err
		}

		switch hdr.Typeflag {
		case tar.TypeReg:
			dest := hdr.Name
			if strings.HasPrefix(dest, "./") {
				// ./usr/bin/hello => /usr/bin/hello
				dest = dest[1:]
			}
			if !strings.HasPrefix(dest, "/") {
				// usr/bin/hello => /usr/bin/hello
				dest = "/" + dest
			}

			tmpdest := dest
			if p.isConffile(tmpdest) {
				// Extract using the extension .dpkg-new
				tmpdest += ".dpkg-new"
			}

			os.MkdirAll(filepath.Dir(tmpdest), 0755)
			os.WriteFile(tmpdest, buf.Bytes(), 0755)

			p.Files = append(p.Files, dest)
		}
	}

	p.SetStatus("unpacked")
	p.Sync()

	return nil
}

// Configure processes the conffiles.
func (p *PackageInfo) Configure() error {
	fmt.Printf("Setting up %s (%s) ...\n", p.Name(), p.Version())

	// Rename conffiles
	for _, conffile := range p.Conffiles {
		os.Rename(conffile+".dpkg-new", conffile)
	}
	p.SetStatus("half-configured")
	p.Sync()

	// Run maintainer script
	if err := p.runMaintainerScript("postinst"); err != nil {
		return err
	}
	p.SetStatus("installed")
	p.Sync()

	return nil
}

func (p *PackageInfo) runMaintainerScript(name string) error {
	if _, ok := p.MaintainerScripts[name]; !ok {
		// Nothing to run
		return nil
	}

	out, err := exec.Command("/bin/sh", p.InfoPath(name)).Output()
	if err != nil {
		return err
	}
	fmt.Print(string(out))

	return nil
}

// We still have to write the code to sync the database

func (d *Database) Sync() error {
	newStatus := deb822.Document{
		Paragraphs: []deb822.Paragraph{},
	}

	// Sync the /var/lib/dpkg/info directory
	for _, pkg := range d.Packages {
		newStatus.Paragraphs = append(newStatus.Paragraphs, pkg.Paragraph)

		if pkg.StatusDirty {
			if err := pkg.Sync(); err != nil {
				return err
			}
		}
	}

	// Make a new version of /var/lib/dpkg/status
	os.Rename("/var/lib/dpkg/status", "/var/lib/dpkg/status-old")
	formatter := deb822.NewFormatter()
	formatter.SetFoldedFields("Description")
	formatter.SetMultilineFields("Conffiles")
	if err := os.WriteFile("/var/lib/dpkg/status", []byte(formatter.Format(newStatus)), 0644); err != nil {
		return err
	}

	return nil
}

func (p *PackageInfo) Sync() error {
	// Write <package>.list
	if err := os.WriteFile(p.InfoPath("list"), []byte(MergeLines(p.Files)), 0644); err != nil {
		return err
	}

	// Write <package>.conffiles
	if err := os.WriteFile(p.InfoPath("conffiles"), []byte(MergeLines(p.Conffiles)), 0644); err != nil {
		return err
	}

	// Write <package>.{preinst,prerm,postinst,postrm}
	for name, content := range p.MaintainerScripts {
		err := os.WriteFile(p.InfoPath(name), []byte(content), 0755)
		if err != nil {
			return err
		}
	}

	p.StatusDirty = false
	return nil
}

/* Utility functions */

func ReadLines(path string) ([]string, error) {
	if _, err := os.Stat(path); !os.IsNotExist(err) {
		content, err := os.ReadFile(path)
		if err != nil {
			return nil, err
		}
		return SplitLines(string(content)), nil
	}
	return nil, nil
}

func SplitLines(content string) []string {
	var lines []string
	for _, line := range strings.Split(string(content), "\n") {
		if strings.TrimSpace(line) == "" {
			continue
		}
		lines = append(lines, line)
	}
	return lines
}

func MergeLines(lines []string) string {
	return strings.Join(lines, "\n") + "\n"
}
