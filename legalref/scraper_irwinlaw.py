from twisted.internet import reactor
from twisted.web.client import getPage
import sys
import os
from bs4 import BeautifulSoup
from cPickle import dump, load
from hashlib import md5
from traceback import print_exc


BASE_URL = 'http://www.irwinlaw.com'
INITIAL_URL = 'http://www.irwinlaw.com/cold/terms'

settings_file = 'settings.pcl'
items_file = 'items.pcl'
items = []


visited_links = set()
pending_links = []


REQUIRED_STRINGS = [
    '/cold/term/',
]


FORBIDDEN_STRINGS = []


def is_good_link(url):
    for good in REQUIRED_STRINGS:
        if not (good in url):
            return False
    for bad in FORBIDDEN_STRINGS:
        if bad in url:
            return False
    return True


if os.path.exists(settings_file):
    f = open(settings_file)
    visited_links, pending_links = load(f)
    pending_links = [l for l in pending_links if is_good_link(l)]
    f.close()


out_dir = 'terms'
delay_sec = .2


def save_settings():
    f = open(settings_file, 'w')
    dump((visited_links, pending_links), f)
    f.close()


def save_items():
    f = open(items_file, 'w')
    dump(items, f)
    f.close()


def on_page(page, url):
    global pending_count
    print 'Got page %s' % url
    orig_url = url
    soup = BeautifulSoup(page)

    # Navigate through links
    for a in soup.find_all('a'):
        try:
            url = a.get('href') or ''
            if '#' in url:
                url = url.split('#')[0]
            #print 'Checking %s' % a.prettify()
            h = md5(url.encode('utf8')).digest()
            if is_good_link(url) and h not in visited_links:
                visited_links.add(h)
                if not url.lower().startswith('http://'):
                    url = BASE_URL + url
                print ('Adding to pending links: %s' % url)
                pending_links.append(url)
                save_settings()
        except:
            print_exc()

    try:
        term = None
        definition = None
        source = None
        related_terms = []
        see = None
        for termdef in soup.find_all(class_='termdefinition'):
            for term_node in termdef.find_all('dl', limit=1):
                # We're inside the definition node.
                dt = term_node.find('dt')
                if dt:
                    term = dt.text
                dd = term_node.find('dd')
                if dd:
                    p = dd.find('p')
                    if p:
                        definition = p.text
                    else:
                        strong = dd.find('strong')
                        if strong and clean_text(strong.text).lower() == 'see':
                            a = dd.find('a')
                            see = clean_text(a.text)
                    source_node = dd.find('ul', class_='source')
                    if source_node:
                        source = source_node.find('li').text
            for ul in termdef.find_all('ul'):
                label = ul.find('label')
                if label and 'see also' in label.text.lower():
                    for li in ul.find_all('li'):
                        a = li.find('a')
                        if a and '/cold/term/' in a['href']:
                            related_terms.append(clean_text(a.text))
        if term:
            item = {
                'term': clean_text(term),
                'definition': clean_text(definition),
                'source': clean_text(source),
                'related_terms': related_terms,
                'url': orig_url,
                'see': see
            }
            print 'Found term: %s' % item
            items.append(item)
            save_items()
    except:
        print_exc()

    if pending_links:
        print '%s more to fetch' % len(pending_links)
        reactor.callLater(delay_sec, fetch_one)
    else:
        print 'Done, no more pages'
        reactor.stop()


def fetch_one():
    while 1:
        if not pending_links:
            print 'Done, no more pages'
            reactor.stop()
            return
        try:
            url = str(pending_links.pop())
            print 'Fetching %s' % url
            visited_links.add(md5(url.encode('utf8')).digest())
            getPage(url).addCallbacks(callback=on_page,
                                      errback=on_error,
                                      callbackArgs=(url,))
            return
        except:
            pass


def on_error(error):
    print 'Error: %s' % error
    if pending_links:
        print '%s more to fetch' % len(pending_links)
        reactor.callLater(delay_sec, fetch_one)
    else:
        print 'Done, no more pages'
        reactor.stop()


def clean_text(text):
    if not text:
        return ''
    t = text.replace('\n', ' ')
    t = t.replace('\r', ' ')
    while '  ' in t:
        t = t.replace('  ', ' ')
    return t.strip()


if __name__ == '__main__':
    pending_links.append(INITIAL_URL)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    fetch_one()
    reactor.run()
