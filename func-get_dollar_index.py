import requests
from bs4 import BeautifulSoup

# 환율 정보를 가져오는 함수 정의
# 이 함수는 currency_code (통화 코드, 예: 'USD')를 입력받아 해당 통화의 상세 환율 정보를 가져옵니다.
def get_dollar_index():
    url = 'https://finance.naver.com/marketindex/worldExchangeDetail.naver?marketindexCd=FX_USDX&fdtc=4'
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    money = soup.find('h2').get_text().replace(' ', '')
    rate_info = soup.find('p', class_='no_today').get_text().replace('\n', '')
    change_icon = soup.find('span', class_='ico')

    CRED = '\033[91m'   # ANSI Escape 코드
    CBLUE   = '\33[34m' 
    CEND = '\033[0m'
    if change_icon:
        if 'up' in change_icon['class']:
            # change_sign = CRED + '▲' + CEND
            change_sign = '▲'   # 텔레그램 봇은 컬러를 지원하지 않으므로, ANSI Escape 코드를 제거합니다.
        elif 'down' in change_icon['class']:
            # change_sign = CBLUE + '▼' + CEND
            change_sign = '▼'
        elif 'same' in change_icon['class']:
            change_sign = ''

    exday_info = soup.find('p', class_='no_exday').get_text().replace('\n', '').replace('전일대비', '')

    return f"{money:8} {rate_info:10} 전일대비 {change_sign} {exday_info}"


print(get_dollar_index())  # 테스트용으로 함수 호출