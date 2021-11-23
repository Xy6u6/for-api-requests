import requests
from bs4 import BeautifulSoup


def get_top_ten_tegs():
    url = 'https://quotes.toscrape.com'
    res = requests.get(url)
    sp = BeautifulSoup(res.text, 'lxml')
    tags = sp.find('div', {"class": 'col-md-4 tags-box'}).find_all('a', class_='tag')
    urls = [url + str(i.get('href')) for i in tags]
    return urls


def get_quotes(url):
    res = requests.get(url)
    sp = BeautifulSoup(res.text, 'lxml')
    tag = sp.find('h3').find('a').text
    quotes = sp.findAll('span', class_='text')
    authors = sp.findAll('small', class_='author')
    for l, k in enumerate(quotes):
        with open(f'list of {tag} sentences.txt', 'a') as f:
            f.write(f'{l + 1}. {k.text} by: {authors[l].text} \n')
    if check_next_page(url):
        nextpage = check_next_page(url)
        get_quotes(nextpage)
    else:
        return


def check_next_page(url):
    res = requests.get(url)
    sp = BeautifulSoup(res.text, 'lxml')
    try:
        nextpage = sp.find('li', class_='next').find('a').get('href')
        return nextpage
    except AttributeError:
        return False
    return True


if __name__ == '__main__':
    url = 'https://quotes.toscrape.com/tag/love'
    get_quotes(url)
