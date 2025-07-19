# main.py
# 이 파일은 텔레그램 봇을 구현하는 메인 스크립트입니다.
# 텔레그램 봇 API를 사용하여 메시지를 처리하고 응답하는 기능을 포함합니다.

# 필요한 라이브러리와 모듈을 임포트합니다.
from config import API_TOKEN
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.apihelper import ApiException

# ⭐ 새로 만든 모듈을 임포트합니다. ⭐
import market_data # market_data.py 파일을 임포트

# pyTelegramBotAPI 라이브러리의 TeleBot 클래스를 사용하여 새로운 텔레그램 봇 객체를 생성합니다.
bot = TeleBot(token=API_TOKEN)

# /start 또는 /help 명령어를 처리하는 핸들러입니다.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        bot.send_message(message.chat.id, "안녕하세요! 저는 텔레그램 봇입니다.")
    except bot.apihelper.ApiException as e:
        print(f"API 오류 발생 (send_welcome): {e}")
    except Exception as e:
        print(f"알 수 없는 오류 발생 (send_welcome): {e}")

# 인라인 버튼을 생성합니다.
# 버튼을 클릭하면 각각의 콜백 데이터가 전송됩니다.
# 이 버튼들은 사용자가 봇과 상호작용할 수 있는 인터페이스
keyboard = [ # 한줄에 2개의 버튼을 배치 합니다.
    [InlineKeyboardButton("환전고시환율", callback_data='1'), InlineKeyboardButton("달러인덱", callback_data='2')]
]
inline_keyboard = InlineKeyboardMarkup(keyboard =keyboard)

# /market 명령어를 처리하는 핸들러입니다.
@bot.message_handler(commands=['market'])
def send_market(message):
    try:
        bot.send_message(message.chat.id, "Market Indicators\n\nExchange Rate \nDollar Index \n\n", reply_markup=inline_keyboard)
    except ApiException as e:
        print(f"API 오류 발생 (send_market): {e}")
    except Exception as e:
        print(f"알 수 없는 오류 발생 (send_market): {e}")

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    try:
        if call.data == '1':
            bot.answer_callback_query(call.id, "환전고시환율을 가져오는 중입니다...")
            # market_data 모듈의 함수를 호출하여 데이터를 가져옵니다.
            exchange_rate_data = market_data.get_exchange_rate()
            # 가져온 데이터를 사용자에게 보냅니다.
            bot.send_message(call.message.chat.id, exchange_rate_data)  
        elif call.data == '2':
            bot.answer_callback_query(call.id, "달러인덱를 가져오는 중입니다.")
            # market_data 모듈의 함수를 호출하여 데이터를 가져옵니다.
            dollar_index_data = market_data.get_dollar_index()
            # 가져온 데이터를 사용자에게 보냅니다. 
            bot.send_message(call.message.chat.id, dollar_index_data)                             
        else:
            bot.answer_callback_query(call.id, "알 수 없는 선택입니다.")
    except ApiException as e:
        print(f"API 오류 발생 (handle_query): {e}")
    except Exception as e:
        print(f"알 수 없는 오류 발생 (handle_query): {e}")





# 모든 텍스트 메시지를 받아서 그대로 다시 보내주는 핸들러입니다. (메아리 기능)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        bot.reply_to(message, message.text)
    except ApiException as e:
        # 사용자가 봇을 차단했거나, 그룹에 메시지를 보낼 권한이 없는 등
        # 다양한 API 관련 예외를 처리합니다.
        print(f"API 오류 발생 (echo_all): {e}")
    except Exception as e:
        # 그 외 예측하지 못한 모든 오류를 처리합니다.
        print(f"알 수 없는 오류 발생 (echo_all): {e}")


# 봇이 메시지를 지속적으로 받아 처리하는 기능을 시작합니다.
# infinity_polling은 연결 오류 발생 시 자동으로 재시작을 시도합니다.
# timeout과 long_polling_timeout을 설정하여 봇의 응답성을 조절합니다
if __name__ == '__main__':
    print("텔레그램 봇을 시작합니다...")
    try:
        # infinity_polling은 연결 오류 발생 시 자동으로 재시작을 시도합니다.
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        # 봇 시작 중 발생하는 치명적인 오류를 처리합니다.
        print(f"봇 시작 중 심각한 오류 발생: {e}")