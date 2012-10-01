
from util import get_urls

def gen_js():
    url_str_list = []
    for url in get_urls():
        url_str_list.append("\"%s\"" %url.strip())
    return "var urls = [%s];" %(','.join(url_str_list))

if __name__ == "__main__":
    print gen_js()
