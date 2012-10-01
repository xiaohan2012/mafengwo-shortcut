import re
from codecs import open

def get_urls():
    with open("urllist.txt","r") as f:
        for line in f.readlines():
            yield line

def extract_urls():
    with open("urls.js","r","utf-8") as f:
        for line in f.readlines():
            try:
                url = re.findall(r"http.+\.html" , line)[0]
                print url
            except IndexError:
                pass
