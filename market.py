# market_data.py
# market_data.py 모듈을 생성하여 환전고시환율과 달러인덱스를 가져오는 함수를 정의합니다.
# 이 모듈은 main.py에서 임포트되어 사용됩니다.

# 필요한 라이브러리와 모듈을 임포트합니다.
import requests
from bs4 import BeautifulSoup

# ⭐ 내가 만든 모듈을 임포트합니다. ⭐
from menu01 import get_exchange_rate
from menu02 import get_dollar_index
# from func-get_dollar_index import get_dollar_index


# # 환율 정보를 가져오는 함수 정의
# # 이 함수는 currency_code (통화 코드, 예: 'USD')를 입력받아 해당 통화의 상세 환율 정보를 가져옵니다.
# def get_exchange_rate(currency_code):
#     url = 'https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_' + currency_code + 'KRW'
#     response = requests.get(url)
#     html_content = response.text
#     soup = BeautifulSoup(html_content, 'html.parser')

#     country = soup.find('h2').get_text().replace(' ', '')
#     rate_info = soup.find('p', class_='no_today').get_text().replace('\n', '')
#     change_icon = soup.find('span', class_='ico')

#     CRED = '\033[91m'   # ANSI Escape 코드
#     CBLUE   = '\33[34m' 
#     CEND = '\033[0m'
#     if change_icon:
#         if 'up' in change_icon['class']:
#             # change_sign = CRED + '▲' + CEND # 텔레그램 봇은 색상을 지원하지 않으므로, ANSI Escape 코드를 제거합니다.
#             change_sign = '▲'
#         elif 'down' in change_icon['class']:
#             # change_sign = CBLUE + '▼' + CEND
#             change_sign = '▼'
#         elif 'same' in change_icon['class']:
#             change_sign = ''

#     exday_info = soup.find('p', class_='no_exday').get_text().replace('\n', '').replace('전일대비', '')
#     return f"{country:8} ({currency_code}) {rate_info:12} 전일대비 {change_sign} {exday_info}"
#     # print(country, currency_code, "실시간 환율", rate_info, '｜ 전일대비', change_sign, exday_info)

# # 달러 인덱스를 가져오는 함수 정의
# # 이 함수는 달러 인덱스의 상세 정보를 가져옵니다.
# def get_dollar_index():
#     url = 'https://finance.naver.com/marketindex/worldExchangeDetail.naver?marketindexCd=FX_USDX&fdtc=4'
#     response = requests.get(url)
#     html_content = response.text
#     soup = BeautifulSoup(html_content, 'html.parser')

#     money = soup.find('h2').get_text().replace(' ', '')
#     rate_info = soup.find('p', class_='no_today').get_text().replace('\n', '')
#     change_icon = soup.find('span', class_='ico')

#     CRED = '\033[91m'   # ANSI Escape 코드
#     CBLUE   = '\33[34m' 
#     CEND = '\033[0m'
#     if change_icon:
#         if 'up' in change_icon['class']:
#             # change_sign = CRED + '▲' + CEND
#             change_sign = '▲'   # 텔레그램 봇은 컬러를 지원하지 않으므로, ANSI Escape 코드를 제거합니다.
#         elif 'down' in change_icon['class']:
#             # change_sign = CBLUE + '▼' + CEND
#             change_sign = '▼'
#         elif 'same' in change_icon['class']:
#             change_sign = ''

#     exday_info = soup.find('p', class_='no_exday').get_text().replace('\n', '').replace('전일대비', '')

#     return f"{money:8} {rate_info:10} 전일대비 {change_sign} {exday_info}"