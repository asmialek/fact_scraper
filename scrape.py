from user_agent import generate_user_agent
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

i = 0

def find_facts(page_link):
    page_response = get(page_link, timeout=5, headers=headers)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    # print(page_content.prettify())
    for ol in page_content.select('ol'):
        for li in ol.select('li'):
            if 'adsbygoogle' not in li.text:
                globals()['i'] += 1
                print(globals()['i'], li.text)
                pass

    next_page_link = page_content.find('div',
                                           attrs={'class': 'page-links2'})
    for a in next_page_link.select('a'):
        if 'Next' in a.find('span', attrs={'class': 'page-number'}).text:
            next_page_link = a['href']
    find_facts(next_page_link)


page_link = 'https://www.thefactsite.com/2010/09/300-random-animal-facts.html'
page_link = 'https://www.thefactsite.com/2012/01/100-random-facts-about-space.html'

headers = {'User-Agent': generate_user_agent(device_type="desktop",
                                             os=('mac', 'linux'))}

find_facts(page_link)
