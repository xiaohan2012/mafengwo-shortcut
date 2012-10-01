import os
import sys
from util import get_urls

def open_urls(urls):
     os.system("google-chrome %s" %' '.join(urls))

if __name__ == "__main__":
    chunk_size = 20
    chunk_num = int(sys.argv[1])
    urls = get_urls()
    if (chunk_num + 1) * chunk_size >= len(urls):
        url_subset = urls[chunk_num * chunk_size : ]
    else:                
        url_subset = urls[chunk_num * chunk_size : (chunk_num + 1) * chunk_size]
    open_urls(url_subset) 


