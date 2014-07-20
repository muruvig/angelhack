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
    article_links = []
    for x in range(10):
        archive_html = opener.open(archive_url[x]).read()
        archive_soup = BeautifulSoup(archive_html)

        article_list = archive_soup.find("div", class_="primaryContent").find("div", class_="module").find_all("a")
        for x in article_list:
            article_links += re.compile(r"<a href=\"(.*?)\">").findall(str(x))
    
    return article_links[::100]

article_links = article_spider()

def article_parser():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36')]

    art_dic = {}
    
    for x in range(10):
        article_html = opener.open(article_links[x]).read()
        article_soup = BeautifulSoup(article_html)
        art_dict["art_id"] = article_links[x]
        
        if article_soup.find("span", id="articleText").find("pre") == None:
            art_dict["text"] = ""
            for string in article_soup.find("span", id="articleText").stripped_strings:
                art_dict["text"] += str(string)
        else:
            art_dict["text"] = (article_soup.find("span", id="articleText").find("pre").string)
        
    return art_dic
