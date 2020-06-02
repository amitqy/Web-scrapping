import requests
from bs4 import BeautifulSoup as bs
import pprint as pp

res = requests.get('https://news.ycombinator.com/news')

soup = bs(res.text, 'html.parser')

links = (soup.select('.storylink'))
votes = soup.select('.score')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'])


def create_custom_hn(links, subtext):
    hn = []
    i = 0
    for i in range(len(links)):
        title = links[i].getText()
        href = links[i].get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 59:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pp.pprint(create_custom_hn(links, subtext))
