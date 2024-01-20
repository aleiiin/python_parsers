from bs4 import BeautifulSoup as bs
import requests as re
from time import sleep

COOKIES = {
    '_ym_uid': '1630083192668788025',
    '_ym_d': '1694960490',
    '_gcl_au': '1.1.1173001733.1704271466',
    '_ab_': '%7B%22search-sandbox%22%3A%22new_specs%22%7D',
    'rrpvid': '53331689521973',
    'rcuid': '65951e6f275702a24166358e',
    'cartUserCookieIdent_v3': '08d293c5f98471e393eeccf547ae0da1d6e67a8b58cf64730bcc8ba96e1eb206a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22bd9845f3-4a77-30de-b23b-7a3ef26e9508%22%3B%7D',
    'phonesIdentV2': 'b0b33956-9ef9-41e3-8d0b-4d99e2504318',
    'tmr_lvid': 'ab1eb7ab27899547c535c03e48567c83',
    'tmr_lvidTS': '1630083192099',
    'ab_catalog': 'homewithcatalog',
    '_gid': 'GA1.2.205101494.1705670002',
    'current_path': '605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
    'PHPSESSID': '350622977ac6338a0d66af9c088c5277',
    'lang': 'ru',
    '_csrf': '0843d6d8c9eb8444c6d5c4e3aaf3a8c77e74a78859331e643e0a841f9001a18da%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22PXbfU-ZckYoCqX_DZl3W8_GHCtm1ICOu%22%3B%7D',
    'city_path': 'moscow',
    '_ym_isad': '1',
    'tmr_detect': '1%7C1705743743609',
    'qrator_jsr': '1705746645.279.J304olLcNo0TmZqE-a3eebq57itdtcu7d7surpkk435afjlar-00',
    'qrator_jsid': '1705746645.279.J304olLcNo0TmZqE-fhgi2n2hdtkg0oblaau8o6gm4o1leksi',
    '_gat': '1',
    '_ga': 'GA1.1.1225245790.1704271471',
    '_ga_FLS4JETDHW': 'GS1.1.1705746645.5.1.1705746651.54.0.1871152462',
    '_ym_visorc': 'b',
}

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_ym_uid=1630083192668788025; _ym_d=1694960490; _gcl_au=1.1.1173001733.1704271466; _ab_=%7B%22search-sandbox%22%3A%22new_specs%22%7D; rrpvid=53331689521973; rcuid=65951e6f275702a24166358e; cartUserCookieIdent_v3=08d293c5f98471e393eeccf547ae0da1d6e67a8b58cf64730bcc8ba96e1eb206a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22bd9845f3-4a77-30de-b23b-7a3ef26e9508%22%3B%7D; phonesIdentV2=b0b33956-9ef9-41e3-8d0b-4d99e2504318; tmr_lvid=ab1eb7ab27899547c535c03e48567c83; tmr_lvidTS=1630083192099; ab_catalog=homewithcatalog; _gid=GA1.2.205101494.1705670002; current_path=605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; PHPSESSID=350622977ac6338a0d66af9c088c5277; lang=ru; _csrf=0843d6d8c9eb8444c6d5c4e3aaf3a8c77e74a78859331e643e0a841f9001a18da%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22PXbfU-ZckYoCqX_DZl3W8_GHCtm1ICOu%22%3B%7D; city_path=moscow; _ym_isad=1; tmr_detect=1%7C1705743743609; qrator_jsr=1705746645.279.J304olLcNo0TmZqE-a3eebq57itdtcu7d7surpkk435afjlar-00; qrator_jsid=1705746645.279.J304olLcNo0TmZqE-fhgi2n2hdtkg0oblaau8o6gm4o1leksi; _gat=1; _ga=GA1.1.1225245790.1704271471; _ga_FLS4JETDHW=GS1.1.1705746645.5.1.1705746651.54.0.1871152462; _ym_visorc=b',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23.11", "Not=A?Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

PARAMS = {
    'category': '17a8a01d16404e77',
}


def parse(url, headers, cookies, params):
    html = get_html(url, headers=headers, cookies=cookies, params=params)
    if html is not None:
        titles = html.find_all('a', {'class': "catalog-product__name ui-link ui-link_black"})
        reasons = html.find_all('div', {'class': "catalog-product__reasons"})
        for i in range(len(titles)):
            print(f'Телефон: {titles[i].text.strip()}\nИзменения: {reasons[i].text.strip()}', end='\n\n')

    return None


def get_html(url, headers, cookies, params):
    print(url)
    response = re.get(url, headers=headers, cookies=cookies, params=params)
    if response.status_code == 200:
        print('SUCCESS')
        sleep(20)
        html = bs(response.content, 'html.parser')

        return html
    else:
        print(f'ERROR: {response.status_code}')

        return None


def main(url, headers=HEADERS, cookies=COOKIES, params=PARAMS):
    parse(url, headers, cookies, params)


if __name__ == '__main__':
    main('https://www.dns-shop.ru/catalog/markdown/?category=17a8a01d16404e77', HEADERS, COOKIES, PARAMS)
