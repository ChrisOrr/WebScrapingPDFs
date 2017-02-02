from bs4 import BeautifulSoup
import requests

def MakeSoup(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    return soup

def SearchSoup(soup):
    for link in soup.find_all('a'):
        if '.pdf' in link.get('href'):
            print(link['href'])

soup = MakeSoup('http://www.rewardinglearning.org.uk/microsites/mathematics/gce/past_papers/index.asp')

SearchSoup(soup)