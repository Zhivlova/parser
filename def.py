import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import re
import itertools

URL = 'https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov'

def download(URL, user_agent='wswp', num_retries=2, charset='utf-8'):
    print('Downloading:', URL)
    request = urllib.request.Request(URL)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(URL, num_retries - 1)
    return html

print(download('https://wciom.ru/ratings/dejatelnost-gosudarstvennykh-institutov'))


def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(URL)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)

def crawl_site(url, max_errors=5):
    for page in itertools.count(1):
        pg_url = '{}{}'.format(url, page)
        html = download(pg_url)
        if html is None:
            num_errors += 1
                if num_errors == max_errors:
                # max errors reached, exit loop
                break
        else:
            num_errors = 0


def link_crawler(start_url, link_regex):
    """ Crawl from the given start URL following links matched by
link_regex
    """
    crawl_queue = [start_url]
    seen = set(crawl_queue)
    while crawl_queue:
        URL = crawl_queue.pop()
        html = download(URL)
        if not html:
            continue
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                abs_link = urljoin(start_url, link)
                # check if have already seen this link
                if abs_link not in seen:
                    seen.add(abs_link)
                    crawl_queue.append(abs_link)


def link_crawler(start_url, link_regex, robots_url=None,
   user_agent='wswp'):
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""",
                               re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)
    if not robots_url:
        robots_url = '{}/robots.txt'.format(start_url)
    rp = get_robots_parser(robots_url)

