# func-get_oil_gold_price.py
# 이 파일은 유가와 금 시세를 가져오는 함수를 정의합니다.
# pandas 라이브러리를 사용하여 웹 페이지에서 데이터를 읽어옵니다.

# 참고
#   https://wikidocs.net/186281 판다스 read_html(), BeautifulSoup find() 로 스크래핑 하는 방법을 잘 설명하고 있습니다.

import pandas as pd

# 유가 시세를 가져오는 함수
def get_oil_price():
    url = 'https://finance.naver.com/marketindex/?tabSel=gold#tab_section'

    oil_gold_lists = pd.read_html(url, match='휘발유', encoding='cp949') # cp949 인코딩은 한글을 지원합니다.
    df = oil_gold_lists[0] # 유가시세 테이블

    # display.unicode.east_asian_width 옵션은 유니코드 동아시아 문자 너비를 계산하여 텍스트 너비를 조정하는 데 사용됩니다.
    # 이 옵션을 활성화하면(True) pandas는 동아시아 문자를 2칸으로 계산하여 세로줄 정렬을 맞출 수 있습니다.
    pd.set_option('display.unicode.east_asian_width', True) # 한글 출력 설정

    return df
# 금 시세를 가져오는 함수
def get_gold_price():
    url = 'https://finance.naver.com/marketindex/?tabSel=gold#tab_section'

    oil_gold_lists = pd.read_html(url, match='백금', encoding='cp949') # cp949 인코딩은 한글을 지원합니다.
    df = oil_gold_lists[0] # 금시세 테이블

    # display.unicode.east_asian_width 옵션은 유니코드 동아시아 문자 너비를 계산하여 텍스트 너비를 조정하는 데 사용됩니다.
    # 이 옵션을 활성화하면(True) pandas는 동아시아 문자를 2칸으로 계산하여 세로줄 정렬을 맞출 수 있습니다.
    pd.set_option('display.unicode.east_asian_width', True) # 한글 출력 설정

    return df


# 데이터 프레임을 html 테이블로 변환하여 출력할 수 있습니다.
# df=get_oil_price()
# html_table = df.to_html()
# print(html_table) # 유가시세 출력

# 텔레그램 봇으로 출력
# bot.send_message(chat_id=CHAT_ID, text=html_table, parse_mode=telegram.ParseMode.HTML)


print(get_oil_price()) # 유가시세 출력
print()
print(get_gold_price()) # 금시세 출력

