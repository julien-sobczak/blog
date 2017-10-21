# -*- coding: utf-8 -*-
# Dependencies:
# - BeautifulSoup 4 => $ easy_install BeautifulSoup4

########################
# Traverse the posts imported from Blogger to generate the metadata at the top of the files.
# We fix some minor problems like XML entities too.
###########

import os
import glob
import pprint
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# List all the tags recensed when the blog was migrated
tags = {}
tags['Agile'] = 'agile'
tags['Architecture'] = 'architecture'
tags['Big Data'] = 'big-data'
tags['Blog'] = 'blog'
tags['Build'] = 'build'
tags['Classics'] = 'classics'
tags['Clean Code'] = 'clean-code'
tags['Cloud'] = 'cloud'
tags['Computer Science'] = 'computer-science'
tags['Database'] = 'database'
tags['DDD'] = 'ddd'
tags['Delivery'] = 'delivery'
tags['Design'] = 'design'
tags['Design Patterns'] = 'design-patterns'
tags['Devops'] = 'devops'
tags['Essays'] = 'essays'
tags['Frameworks'] = 'frameworks'
tags['Gaming'] = 'gaming'
tags['Hiring'] = 'hiring'
tags['HTML5'] = 'html5'
tags['Java'] = 'java'
tags['JavaScript'] = 'javascript'
tags['Kid Programming'] = 'kid-programming'
tags['Languages'] = 'languages'
tags['Learning'] = 'learning'
tags['Management'] = 'management'
tags['Mathematics'] = 'mathematics'
tags['Performance'] = 'performance'
tags['PHP'] = 'php'
tags['Popular'] = 'popular'
tags['Productivity'] = 'productivity'
tags['Public Speaking'] = 'public-speaking'
tags['Refactoring'] = 'refactoring'
tags['Security'] = 'security'
tags['SOA'] = 'soa'
tags['Team'] = 'team'
tags['Testing'] = 'testing'
tags['Tools'] = 'tools'
tags['UX Design'] = 'ux-design'
tags['Web'] = 'web'


def process(content):
    """
    Contains all the logic and delegates to more specific methods.

    :param content: the full file content
    :return: the new content
    """

    content = remove_xml_entities(content)
    content = prepend_metadata(content)

    return content


def remove_xml_entities(content):

    """
    Replace XML entities required by Blogger (XML editor...) but no longer required. Thanks Jekyll!!!!

    :param content: the full file content
    :return: the new content
    """

    entities = {}

    # https://fr.wikipedia.org/wiki/Liste_des_r%C3%A9f%C3%A9rences_d%27entit%C3%A9s_de_caract%C3%A8res_en_XML_et_HTML
    entities["quot"] = "\"" # U+0022
    entities["amp"] = "&" # U+0026
    entities["apos"] = "'" # U+0027
    entities["lt"] = "<" # U+003C
    entities["gt"] = ">" # U+003E
    entities["acute"] = "´" # U+00B4
    entities["Agrave"] = "À" # U+00C0
    entities["Acirc"] = "Â" # U+00C2
    entities["Auml"] = "Ä" # U+00C4
    entities["Ccedil"] = "Ç" # U+00C7
    entities["Eacute"] = "É" # U+00C9
    entities["Ecirc"] = "Ê" # U+00CA
    entities["Euml"] = "Ë" # U+00CB
    entities["Icirc"] = "Î" # U+00CE
    entities["Ouml"] = "Ö" # U+00D6
    entities["Ugrave"] = "Ù" # U+00D9
    entities["Uacute"] = "Ú" # U+00DA
    entities["Ucirc"] = "Û" # U+00DB
    entities["Uuml"] = "Ü" # U+00DC
    entities["agrave"] = "à" # U+00E0
    entities["aacute"] = "á" # U+00E1
    entities["acirc"] = "â" # U+00E2
    entities["ccedil"] = "ç" # U+00E7
    entities["egrave"] = "è" # U+00E8
    entities["eacute"] = "é" # U+00E9
    entities["ecirc"] = "ê" # U+00EA
    entities["ocirc"] = "ô" # U+00F4
    entities["ouml"] = "ö" # U+00F6
    entities["ugrave"] = "ù" # U+00F9
    entities["ucirc"] = "û" # U+00FB
    entities["uuml"] = "ü" # U+00FC
    entities["hellip"] = "…" # U+2026
    entities["le"] = "≤" # U+2264 
    entities["ge"] = "≥" # U+2265

    for entity in entities:
        content = content.replace("&%s;" % entity, entities[entity])

    return content

#
def prepend_metadata(content):

    """
    Extract the YAML front matter block from the metadata stored in the original blog post.

    :param content: the full file content
    :return: the new content
    """

    # We will collect the metadata in this variable
    metadata = {}

    # We use the BeautifulSoup library to extract information from an HTML string
    soup = BeautifulSoup(content, 'html.parser')

    article = soup.find('article')
    article_type = article.get('class')[0]

    # Common metadata
    metadata['author'] = 'Julien Sobczak'
    metadata['layout'] = 'post'
    date_written = article.find('meta', { 'itemprop' : 'datePublished'})
    if date_written:
        metadata['date'] = date_written.get('content')

    labels = article.find('ul', { 'class' : 'labels' })
    if labels:
        labels = labels.find_all('span', { 'class' : 'label-text' })
    metadata['tags'] = []
    if labels:
        for label in labels:
            label = label.get_text().strip()
            if label in tags:
                metadata['tags'].append(tags[label])
            elif label in [ "I'm readin' I.T.", "I'm watchin' I.T.", "I'm tellin' I.T.", "I'm inspectin' I.T." ]:
                pass # ignore
            else:
                raise Exception("Unknown tag <%s>" % label)


    # Specific metadata
    if article_type == 'post-read':
        metadata['category'] = 'read'
        metadata['title'] = article.h1.get_text()
        image = article.find('img', { "class" : "book-cover" })
        if image:
            metadata['image'] = image.get('src')
        metadata['read_authors'] = article.h2.get_text()
        metadata['read_note'] = article.find('div', { "class" : "evaluations"}).find('meta', { "itemprop" : "ratingValue"}).get('content')

        informations = article.find('section', { "class" : "informations"})
        isbn = informations.find('span', { "itemprop" : "isbn"})
        number_of_pages = informations.find('span', { "itemprop" : "numberOfPages"})
        date_published = informations.find('span', { "itemprop" : "datePublished"})
        book_format = informations.find('span', { "itemprop" : "bookFormat"})

        if date_published:
            metadata['read_date_published'] = date_published.get('content')
        if book_format:
            metadata['read_book_format'] = book_format.get_text()
        if isbn:
            metadata['read_isbn'] = isbn.get_text()
        if number_of_pages:
            metadata['read_number_of_pages'] = number_of_pages.get_text()


    elif article_type == 'post-watch':
        metadata['category'] = 'watch'
        metadata['title'] = article.h1.get_text()
        metadata['watch_speakers'] = article.h2.get_text()
        image = article.header.find('img')
        if image:
            metadata['image'] = article.header.find('img').get('src')
        metadata['watch_note'] = article.find('div', { "class" : "evaluations"}).find('meta', { "itemprop" : "ratingValue"}).get('content')

        informations = article.find('section', { "class" : "informations"})
        url = informations.find('span', { "itemprop" : "url"})
        organizer = informations.find('span', { "itemprop" : "organizer"})
        start_date = informations.find('span', { "itemprop" : "startDate"})

        if url:
            metadata['watch_url'] = url.get('content')
        if organizer:
            metadata['watch_organizer'] = organizer.get_text()
        if start_date:
            metadata['watch_date'] = start_date.get('content')


    elif article_type == 'post-tell':
        metadata['category'] = 'tell'
        metadata['title'] = article.h1.get_text()


    elif article_type == 'post-inspect':
        metadata['category'] = 'inspect'
        metadata['title'] = article.h1.get_text()


    # Collect is over! We should format the metadata to the Front Matter YAML format.

    metadata_str = ""
    metadata_str += "---\n"
    metadata_str += "layout: %s\n" % metadata['layout']
    metadata_str += "title: '%s'\n" % metadata['title']
    metadata_str += "author: '%s'\n" % metadata['author']
    if "date" in metadata:
        metadata_str += "date: '%s'\n" % (metadata['date'] + 'T09:00:00.002+02:00')
    metadata_str += "category: %s\n" % metadata['category']
    metadata_str += "tags:\n"
    for tag in metadata['tags']:
        metadata_str += "- %s\n" % tag

    if article_type == 'post-read':
        if "image" in metadata:
            metadata_str += "image: '%s'\n" % metadata['image']
        metadata_str += "read_authors: '%s'\n" % metadata['read_authors']
        metadata_str += "read_note: %s\n" % metadata['read_note']
        if "read_date_published" in metadata:
            metadata_str += "read_date_published: '%s'\n" % metadata['read_date_published']
        if "read_book_format" in metadata:
            metadata_str += "read_book_format: '%s'\n" % metadata['read_book_format']
        if "read_isbn" in metadata:
            metadata_str += "read_isbn: '%s'\n" % metadata['read_isbn']
        if "read_number_of_pages" in metadata:
            metadata_str += "read_number_of_pages: %s\n" % metadata['read_number_of_pages']

    elif article_type == 'post-watch':
        if "image" in metadata:
            metadata_str += "image: '%s'\n" % metadata['image']
        metadata_str += "watch_speakers: '%s'\n" % metadata['watch_speakers']
        metadata_str += "watch_note: %s\n" % metadata['watch_note']
        if "watch_url" in metadata:
            metadata_str += "watch_url: '%s'\n" % metadata['watch_url']
        if "watch_organizer" in metadata:
            metadata_str += "watch_organizer: '%s'\n" % metadata['watch_organizer']
        if "watch_date" in metadata:
            metadata_str += "watch_date: '%s'\n" % metadata['watch_date']

    metadata_str += "---\n\n"
    metadata_str += content

    return metadata_str


######
# Main
######

for filename in glob.glob('_posts/*.html'):
    print "Processing %s" % filename

    f = open(filename, 'r')
    content = f.read().decode('utf8')
    content = process(content)

    # read() seems to close the file...

    f = open(filename, 'w')
    f.write(content)

