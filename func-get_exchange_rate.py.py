import requests
from bs4 import BeautifulSoup

# 환율 정보를 가져오는 함수 정의
# 이 함수는 currency_code (통화 코드, 예: 'USD')를 입력받아 해당 통화의 상세 환율 정보를 가져옵니다.
def get_exchange_rate(currency_code):
    url = 'https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_' + currency_code + 'KRW'
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    country = soup.find('h2').get_text().replace(' ', '')
    rate_info = soup.find('p', class_='no_today').get_text().replace('\n', '')
    change_icon = soup.find('span', class_='ico')

    CRED = '\033[91m'   # ANSI Escape 코드
    CBLUE   = '\33[34m' 
    CEND = '\033[0m'
    if change_icon:
        if 'up' in change_icon['class']:
            change_sign = CRED + '▲' + CEND
        elif 'down' in change_icon['class']:
            change_sign = CBLUE + '▼' + CEND
        elif 'same' in change_icon['class']:
            change_sign = ''

    exday_info = soup.find('p', class_='no_exday').get_text().replace('\n', '').replace('전일대비', '')

    return f"{country:8} ({currency_code:3}) {rate_info:12} 전일대비 {change_sign:5} {exday_info}"
    # print(country, currency_code, "실시간 환율", rate_info, '｜ 전일대비', change_sign, exday_info)

# USD, EUR, JPY, CNY 환율 확인하기
# print(get_exchange_rate('USD'))
# print(get_exchange_rate('JPY'))
# print(get_exchange_rate('CNY'))
# print(get_exchange_rate('EUR'))