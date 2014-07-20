from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import requests
import re
import sys

def archive_spider():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36')]
    url = "http://reuters.com/resources/archive/us/"
    html = opener.open(url).read()

    soup = BeautifulSoup(html)

    date_list = soup.find("div", class_="moduleBody").find_all("p")
    archive_ids = []
    for x in date_list:
        archive_ids += re.compile(r"\"(.*?)\"").findall(str(x))
    archive_list = ["http://www.reuters.com" + str(x) for x in archive_ids]

    return archive_list[::100]

archive_url = archive_spider()

def article_spider():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36')]

    archive_html = opener.open(archive_url[0]).read()
    archive_soup = BeautifulSoup(archive_html)

    article_list = archive_soup.find("div", class_="primaryContent").find("div", class_="module").find_all("a")
    article_links = []
    for x in article_list:
        article_links += re.compile(r"<a href=\"(.*?)\">").findall(str(x))
    return article_links[::100]

article_links = article_spider()

def article_parser():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36')]

    article_html = opener.open(article_links[1]).read()
    article_soup = BeautifulSoup(article_html)

    if article_soup.find("span", id="articleText").find("pre") == None:
        text = ""
        for string in article_soup.find("span", id="articleText").stripped_strings:
            text += str(string)
    else:
        text = (article_soup.find("span", id="articleText").find("pre").string)
    
    return text
