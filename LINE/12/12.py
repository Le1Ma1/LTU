from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import config
import json, urllib.request, ssl

app = Flask(__name__)
line_bot_api = LineBotApi(config.CHANNEL_ACCESS_TOKEN)
line_handler = WebhookHandler(config.CHANNEL_SECRET)

def get_weather(city="臺北市"):
    API_KEY = config.CWA_API_KEY
    url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}&format=JSON'
    ssl._create_default_https_context = ssl._create_unverified_context
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    location = output['records']['location']

    for i in location:
        if i['locationName'] == city or i['locationName'] == city.replace('台','臺'):
            wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']
            maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']
            mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']
            pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']
            return f"{i['locationName']}未來8小時{wx8}，最高溫{maxt8}°C，最低溫{mint8}°C，降雨機率{pop8}%"
    return f"查無此城市：{city}，請用台灣縣市全名！"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text.strip()
    # 直接查詢天氣
    result = get_weather(user_text)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=result))

if __name__ == "__main__":
    app.run()