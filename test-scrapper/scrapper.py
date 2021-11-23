import requests
from bs4 import BeautifulSoup

def get_res():
    url = 'https://quotes.toscrape.com/'
    res = requests.get(url)
    sp = BeautifulSoup(res.text, 'lxml')
    tags = sp.findAll('span', class_='tag-item')
    quotes = sp.findAll('span', class_='text')
    authors = sp.findAll('small', class_='author')
    print(tags[0])
    # for i, k in enumerate(quotes):
    #     print(f'{i+1}. {k.text} by: {authors[i].text}')
if __name__ == '__main__':
    get_res()