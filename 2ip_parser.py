from time import sleep
import requests as re
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


def get_html(url):
    response = re.get(url, headers={'user-agent': UserAgent().chrome})
    print('LOADING')
    if response.status_code == 200:
        print('SUCCESS')
        return response.content
    else:
        print(f'ERROR: {response.status_code}')
        return False


def main(url):
    html = get_html(url)
    if html:
        sleep(15)
        html = bs(html, 'html.parser')
        print(f'id: {html.find(id="d_clip_button").text.strip()}')
        print(' '.join(html.find_all('div', {'class': 'data_item copy-info-details'})[1].text.strip().split()))
        print(' '.join(html.find_all('div', {'class': 'data_item copy-info-details'})[3].text.strip().split()[:-1]))
        print(' '.join(html.find_all('div', {'class': 'data_item copy-info-details'})[4].text.strip().split()))
    else:
        print(html)


if __name__ == '__main__':
    main('https://2ip.ru/')
