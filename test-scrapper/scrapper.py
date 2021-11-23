import requests
from bs4 import BeautifulSoup

def get_res():
    url = 'https://quotes.toscrape.com'
    res = requests.get(url)
    sp = BeautifulSoup(res.text, 'lxml')
    tags = sp.find('div', {"class": 'col-md-4 tags-box'}).find_all('a', class_='tag')
    for z, i in enumerate(tags):
        res = requests.get(f'{url}{i.get("href")}')
        sp = BeautifulSoup(res.text, 'lxml')
        quotes = sp.findAll('span', class_='text')
        authors = sp.findAll('small', class_='author')
        for l, k in enumerate(quotes):
            with open(f'{z+1} list of {tags[z].text} sentences.txt', 'a') as f:
             f.write(f'{l+1}. {k.text} by: {authors[l].text} \n')
if __name__ == '__main__':
    get_res()