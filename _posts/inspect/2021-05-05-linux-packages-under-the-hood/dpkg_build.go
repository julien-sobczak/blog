package main

import (
	"archive/tar"
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strings"

	"github.com/blakesmith/ar"
)

func tarballPack(directory string, filter func(string) bool) []byte {
	var bufdata bytes.Buffer
	twdata := tar.NewWriter(&bufdata)
	filepath.Walk(directory, func(path string, info os.FileInfo, errParent error) error {
		if info.IsDir() {
			return nil
		}
		if filter != nil && filter(path) {
			return nil
		}
		sep := fmt.Sprintf("%c", filepath.Separator)
		hdr := &tar.Header{
			Name: strings.TrimPrefix(strings.TrimPrefix(path, directory), sep), // Ex: hello/DEBIAN/control => control
			Uid:  0,                                                            // root
			Gid:  0,                                                            // root
			Mode: 0650,
			Size: info.Size(),
		}
		twdata.WriteHeader(hdr)
		content, _ := ioutil.ReadFile(path)
		twdata.Write(content)

		return nil
	})
	twdata.Close()

	return bufdata.Bytes()
}

func arPutFile(w *ar.Writer, name string, body []byte) {
	hdr := &ar.Header{
		Name: name,
		Mode: 0600,
		Uid:  0,
		Gid:  0,
		Size: int64(len(body)),
	}
	w.WriteHeader(hdr)
	w.Write(body)
}

func main() {
	if len(os.Args) < 3 {
		log.Fatalf("Missing 'directory' and/or 'dest' arguments. Usage: dpkg directory dest")
	}
	directory := os.Args[1]
	dest := os.Args[2]

	// Create the debian archive file
	fdeb, _ := os.Create(dest)
	defer fdeb.Close()

	writer := ar.NewWriter(fdeb) // LIKE dpkg_ar_create
	writer.WriteGlobalHeader()

	// Append debian-binary
	arPutFile(writer, "debian-binary", []byte("2.0\n"))

	// Append control.tar
	controlDir := filepath.Join(directory, "DEBIAN")
	controlTarball := tarballPack(controlDir, nil)
	arPutFile(writer, "control.tar", controlTarball)

	// Append data.tar
	dataDir := directory
	dataTarball := tarballPack(dataDir, func(path string) bool {
		return strings.HasPrefix(path, controlDir)
	})
	arPutFile(writer, "data.tar", dataTarball)
}
