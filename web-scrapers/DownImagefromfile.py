from bs4 import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys

def main(url, out_folder):
    """Downloads all the images at 'url' to /test/"""
    soup = bs(urlopen(url))
    parsed = list(urlparse.urlparse(url))
    
    for image in soup.findAll("img"):
        print "Image: %(src)s" % image
        filename = image["src"].split("/")[-1]
        parsed[2] = image["src"]
        outpath = os.path.join(out_folder, filename)
        if image["src"].lower().startswith("http"):
            urlretrieve(image["src"], outpath)
        else:
            urlretrieve(urlparse.urlunparse(parsed), outpath)

def _usage():
    print "usage: python dumpimages.py filepath [outpath]"

if __name__ == "__main__":
  #  filePath = sys.argv[-1]
    #out_folder = "/test/"
    out_folder = sys.argv[1]
  #  if not url.lower().startswith("http"):
   #     out_folder = sys.argv[-1]
    ##   if not url.lower().startswith("http"):
      #      _usage()
       #     sys.exit(-1)
    input_file = open('links.txt','r')
    for line in input_file:
	url = line
	print line
 	main(url, out_folder)
	
