from bs4 import BeautifulSoup
from urllib2 import urlopen
from sys import argv
import re

script, theurl = argv

def job_info(url):
	html = urlopen(url).read()
	soup = BeautifulSoup(html, "lxml")
	job_title = soup.h2.contents

	# Finds all div siblings of 1st h4 tag
	job_responsibilities = soup.select("h4:nth-of-type(1) ~ div")
	pretty_job_responsibilities = []
	for resp in job_responsibilities:
		resp = resp.get_text()
		pretty_job_responsibilities.append(resp)

	job_requirements = soup.select("h4:nth-of-type(2) ~ div")
	pretty_job_requirements = []
	for req in job_requirements:
		req = req.get_text()
		pretty_job_requirements.append(req)

	print "Job title: {0} \n Responsibilities: {1} \n Requirements: {2}".format(job_title, pretty_job_responsibilities, pretty_job_requirements)

job_info(theurl)
