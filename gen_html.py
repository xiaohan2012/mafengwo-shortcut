import re
import os
import math
from util import get_urls

template = """<object type="application/x-shockwave-flash" data="http://www.mafengwo.cn/swf/mfwcat.swf?v35" width="288" height="218" id="pnl_goldcat" style="visibility: visible; ">
        <param name="wmode" value="transparent">
        <param name="allowscriptaccess" value="always">
        <param name="flashvars" value="isself=0&amp;uid=%s&amp;isfriend=1">
    </object>"""
    
def _get_uid(url):
    return re.findall(r"(\d+)\.html",url)[0]

def gen_html(root_path ,chunk_size= 20):
    urls = list(get_urls())
    chunk_count = math.ceil( len(urls) / float(chunk_size) )
    for i in xrange(int(chunk_count)):
        with open(os.path.join(root_path , "%d.html" %i),"w") as f:
            subset = (i == chunk_count - 1 and urls[i*chunk_size:] or urls[i*chunk_size : (i+1)*chunk_size])

            print len(subset)

            f.write("""<html lang="en"><head><meta charset="UTF-8"><title>No.%d file</title>""" %i)

            for url in subset:
                html = template %(_get_uid(url))
                f.write(html)
            f.write("""</head><body>""")

if __name__ == "__main__":
    gen_html("mafengwo")
