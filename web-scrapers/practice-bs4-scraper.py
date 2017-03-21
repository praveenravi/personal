from bs4 import BeautifulSoup
from urllib2 import urlopen
from sys import argv
import re

script, theurl = argv

# test url: http://jessicayung.github.io

def job_info(url):
	html = urlopen(url).read()
	soup = BeautifulSoup(html, "lxml")

	el1 = soup.select("h1 ~ nav")
	# print(soup.find("table").tr.td.findNextSibling().a['href'])

	el2 = "hi" 

	el3 = "hello"
	print " el1: {0} \n el2: {1} \n el3: {2}".format(el1, el2, el3)

job_info(theurl)