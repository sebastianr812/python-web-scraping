import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titleline > a')
subtexts = soup.select('.subtext')

links2 = soup2.select('.titleline > a')
subtexts2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtexts + subtexts2


def sort_stories_by_votes(li):
    return sorted(li, key=lambda ele: ele['votes'], reverse=True)


def create_custom_hn(links, subtexts):
    hn = []

    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        curr_votes = subtexts[index].select('.score')
        if len(curr_votes):
            points = int(curr_votes[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({
                    'title': title,
                    'link': href,
                    'votes': points
                })
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
