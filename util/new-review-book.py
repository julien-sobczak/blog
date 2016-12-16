# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import codecs
import urllib2
import re
from optparse import OptionParser
from datetime import date, datetime

class BookMetadata:

    def __init__(self):
        self.title = None
        self.image = None
        self.authors = None
        self.amazon = None
        self.goodreads = None
        self.isbn13 = None
        self.isbn10 = None
        self.format_type = None
        self.number_of_pages = None
        self.publisher = None
        self.publishing_date = None


class GoodreadsMetadataExtractor:

    MONTHS = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12",
    }

    def __init__(self, follow_links = True):
        self.follow_links = follow_links

    def extract(self, url):
        """
        Load the goodreads webpage to extract metadata.
        :param url: the URL of the book on Goodreads
        :return: the BookMetadata object
        """

        response = urllib2.urlopen(url)
        if response.code != 200:
            raise Exception("[%s] Invalid URL: %s" % (response.code, url))
        source = response.read()

        return self.extracts(url, source)


    def extracts(self, url, source):
        """
        Extracts the metadata from the given source.
        Useful for test-purpose
        :param url: the URL representing the source
        :param source: the raw html page
        :return: the BookMetadata object
        """

        soup = BeautifulSoup(source, 'html.parser')

        metadata = BookMetadata()
        metadata.title = self._title(soup)
        metadata.image = self._image(soup)
        metadata.author = self._author(soup)
        metadata.amazon = self._amazon(soup)
        metadata.goodreads = self._goodreads(soup)
        metadata.isbn13 = self._isbn13(soup)
        metadata.isbn10 = self._isbn10(soup)
        metadata.format_type = self._format_type(soup)
        metadata.number_of_pages = self._number_of_pages(soup)
        metadata.publisher = self._publisher(soup)
        metadata.publishing_date = self._publishing_date(soup)

        return metadata


    def _goodreads(self, soup):
        return soup.find("link", { "rel": "canonical" }).get("href").strip();


    def _format_type(self, soup):
        return soup.find("span", { "itemprop": "bookFormatType" }).get_text().strip();


    def _number_of_pages(self, soup):
        elementNumberOfPages = soup.find("span", { "itemprop": "numberOfPages" })
        if not elementNumberOfPages:
            # Some books does not have their number of pages filled on
            # Goodreads...
            return None

        pages = elementNumberOfPages.get_text().strip()

        # We extract the number of pages
        indexPages = pages.index(" pages")
        numberOfPages = pages[0:indexPages]

        return numberOfPages


    def _amazon(self, soup):

        if not self.follow_links:
            return None

        bookId = soup.find(id="book_id").get("value")

        amazonVendorId = "1"
        urlRedirect = "https://www.goodreads.com/book_link/follow/" + amazonVendorId + "?book_id=" + bookId

        response = urllib2.urlopen(urlRedirect)

        if response.code != 200:
            raise Exception("[%s] Invalid url: " % (response.code, urlRedirect))

        location = response.geturl()
        location = self._calculate_url_amazon(location)

        return location



    def _calculate_url_amazon(self, location):
        """
        Remove unnecessary URL parameters. Ex:
        "http://www.amazon.com/gp/product/0321125215/ref=x_gr_w_bb?ie=UTF8&tag=httpwwwgoodco-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0321125215&SubscriptionId=1MGPYB6YW3HWK55XCGG2"
        """

        indexOfRef = location.index("ref=")
        if indexOfRef != -1:
            location = location[:indexOfRef]

        return location


    def _author(self, soup):
        return soup.find("span", { "itemprop": "author" }).get_text().strip()


    def _image(self, soup):
        element = soup.find(id="coverImage")

        if not element:
            return None

        return element.get("src")


    def _title(self, soup):
        return soup.find(id="bookTitle").get_text().strip()


    def _isbn13(self, soup):
        isbn13Element = self._get_isbn13_element(soup)

        if not isbn13Element:
            return None

        return isbn13Element.get_text().strip()


    def _isbn10(self, soup):
        isbn13Element = self._get_isbn13_element(soup)

        if not isbn13Element:
            return None

        isbn10 = isbn13Element.parent.parent.get_text().strip()
        indexParenthesis = isbn10.index('(')
        isbn10 = isbn10[0:indexParenthesis].strip()
        return isbn10


    def _get_isbn13_element(self, soup):
        isbn = soup.find_all("span", { "itemprop": "isbn" })
        if not isbn:
            return None
        isbn13Element = isbn[0]
        return isbn13Element


    def _publisher(self, soup):
        publishingInformation = self._get_publishing_information(soup)

        if not publishingInformation:
            return None

        # We extract publishing information
        indexBy = publishingInformation.index("by")
        if indexBy == -1:
            return None

        publisher = publishingInformation[indexBy+3:].strip()

        return publisher


    def _publishing_date(self, soup):
        publishingInformation = self._get_publishing_information(soup)

        if not publishingInformation:
            return None

        # We extract publishing information
        indexBy = publishingInformation.index("by")
        if indexBy == -1:
            return None

        publishingDate = publishingInformation[len("Published"):indexBy].strip()

        match = re.match("^(\w+)\s+(\d+).*\s+(\d+)$", publishingDate)
        if match:
            monthName = match.group(1)
            day = match.group(2)
            year = match.group(3)
            publishingDate = "%s-%s-%s" % (year, GoodreadsMetadataExtractor.MONTHS[monthName], day)
            return publishingDate
        else:
            return None


    def _get_publishing_information(self, soup):
        publishElement = soup.select("#details > div.row")
        if len(publishElement) <= 1:
            return None
        return publishElement[1].get_text().strip()



class BookReviewPost:

    def __init__(self, metadata, publication_date):
        self.metadata = metadata
        self.publication_date = publication_date

    def creates(self):
        result = ""
        result += "---\n"

        result += "layout: post-read\n"
        result += "title: %s\n" % self.metadata.title
        result += "author: Julien Sobczak\n"
        result += "date: '%s'\n" % self.publication_date
        result += "categories: read\n"
        result += "tags:\n"
        result += "- ???\n"
        if self.metadata.image:
            result += "image: '%s'\n" % self.metadata.image
        result += "read_authors: %s\n" % self.metadata.author
        result += "read_note: ???\n"
        result += "read_roti: ???\n"
        result += "read_time: ???\n"
        if self.metadata.publisher:
            result += "read_publisher: '%s'\n" % self.metadata.publisher
        if self.metadata.publishing_date:
            result += "read_date_published: '%s'\n" % self.metadata.publishing_date
        if self.metadata.format_type:
            result += "read_book_format: '%s'\n" % self.metadata.format_type
        if self.metadata.isbn10:
            result += "read_isbn: '%s'\n" % self.metadata.isbn10
        if self.metadata.number_of_pages:
            result += "read_number_of_pages: %s\n" % self.metadata.number_of_pages
        result += "read_headline: ???\n"
        if self.metadata.amazon: # KO
            result += "link_amazon: '%s'\n" % self.metadata.amazon
        if self.metadata.goodreads:
            result += "link_goodreads: '%s'\n" % self.metadata.goodreads

        result += "---\n"
        result += "\n"

        return result


    def create(self):
        content = self.creates()

        title = self.metadata.title.lower().replace(' ', '-').replace(',', '-').replace('_', '-').replace(':', '-')
        filename = '../_posts/%s-%s.md' % (self.publication_date, title)
        f = codecs.open(filename, encoding='utf-8', mode='w')
        f.write(content)
        f.close()

        print "New post created: %s" % filename




usage = "usage: %prog [options] url"
parser = OptionParser(usage=usage)
parser.add_option("-l", "--disable-follow", dest="follow_links", action="store_false", default=True,
                  help="Do not follow links on Goodreads.com")
parser.add_option("-d", "--date", dest="publication_date", metavar="YYYY-MM-DD", default=date.today().isoformat(),
                  help="Set the publication date")

(options, args) = parser.parse_args()

# Process arguments
if len(args) != 1:
    parser.error("incorrect number of arguments")

goodreads_url = args[0]


extractor = GoodreadsMetadataExtractor(follow_links=options.follow_links)
metadata = extractor.extract(goodreads_url)

post = BookReviewPost(metadata, publication_date=options.publication_date)
post.create()



