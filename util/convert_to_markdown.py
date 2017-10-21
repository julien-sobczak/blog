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
import re

reload(sys)
sys.setdefaultencoding('utf8')


def process(content):
    """
    Contains all the logic and delegates to more specific methods.

    :param content: the full file content
    :return: the new content
    """

    content = prepend_metadata(content)

    return content


#
def prepend_metadata(content):

    """
    Extract the YAML front matter block from the metadata stored in the original blog post.

    :param content: the full file content
    :return: the new content
    """

    # We will collect the new metadata in this variable
    new_metadata = ""

    # We will extract the current metadata in this variable
    current_metadata = ""
    lines = content.split("\n")
    front_matter = False
    for line in lines:
        if line.startswith('---'):
            if front_matter == True:
                # This is the ending of Front Matter
                break
            else:
                # We found the beginning of Front Matter
                front_matter = True
        elif front_matter:
            current_metadata += line + "\n"


    # We use the BeautifulSoup library to extract information from an HTML string
    soup = BeautifulSoup(content, 'html.parser')

    article = soup.find('article')

    class_roti = article.\
        find('div', { "class" : "evaluations"}). \
        find_all('span')[1].get('class')[0]
    new_metadata += "read_roti: %s\n" % class_roti[-1]

    class_time = article. \
        find('div', { "class" : "evaluations"}). \
        find_all('span')[2].get('class')[0]
    new_metadata += "read_time: %s\n" % class_time[class_time.rfind('-') + 1:]

    headline = article.find('div', { "class" : "headline"}).get_text().strip()
    headline = re.sub(r'\s+.\s+', ' ', headline, flags=re.MULTILINE & re.DOTALL)
    new_metadata += "read_headline: \"%s\"\n" % headline

    publisher_tag = article.find('span', { "itemprop" : "publisher"})
    if publisher_tag:
        publisher = publisher_tag.get_text()
        new_metadata += "read_publisher: \"%s\"\n" % publisher


    links = article.find_all('option')
    if len(links) == 4:
        link_amazon = links[1].get('value')
        link_goodreads = links[3].get('value')
        new_metadata += "link_amazon: \"%s\"\n" % link_amazon
        new_metadata += "link_goodreads: \"%s\"\n" % link_goodreads
    else:
        print "Missing links..."
    new_metadata += "---\n\n"


    paragraphs = article.find('section', { "class" : "comment" }).find_all('p')
    new_content = ""
    for paragraph in paragraphs:
        if paragraph.get('class') and paragraph.get('class')[0] == "me":
            continue
        paragraph_text = str(paragraph)
        paragraph_text = re.sub(r'\s+.\s+', ' ', paragraph_text, flags=re.DOTALL & re.MULTILINE).strip()
        paragraph_text = re.sub(r'<p.*?>(.*?)</p>', r'\1', paragraph_text)
        paragraph_text = re.sub(r'<em>(.*?)</em>', r'*\1*', paragraph_text)
        paragraph_text = re.sub(r'<a\shref=\"(.*?)\".*?>(.*?)</a>', r'[\2](\1)', paragraph_text)
        paragraph_text = re.sub(r'\s+', ' ', paragraph_text).strip()
        new_content += paragraph_text + "\n\n"

    # The "touche finale"!
    current_metadata = current_metadata.replace("layout: post", "layout: post-read")

    return "---\n" + current_metadata + new_metadata + "\n" + new_content


######
# Main
######


for filename in glob.glob('../_posts/*.html'):
    print "Processing %s" % filename

    f = open(filename, 'r')
    content = f.read().decode('utf8')

    if "read_note:" not in content:
        print "Ignoring %s" % filename
        continue

    content = process(content)

    print "Writing %s" % filename.replace('.html', '.md')
    f = open(filename.replace('.html', '.md'), 'w')
    f.write(content)

