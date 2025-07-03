from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from flex_templates import get_flex_message
import config

app = Flask(__name__)
line_bot_api = LineBotApi(config.CHANNEL_ACCESS_TOKEN)
line_handler = WebhookHandler(config.CHANNEL_SECRET)

@app.route('/')
def home():
    return 'Hello World'

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text.strip()
    if text == '123':
        flex_msg = get_flex_message('01', alt="咖啡館推薦")
        line_bot_api.reply_message(event.reply_token, flex_msg)
    elif text == '333':
        flex_msg = get_flex_message('02', alt="漢堡推薦")
        line_bot_api.reply_message(event.reply_token, flex_msg)
    elif text == '456':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到456了'))
    elif text == '789':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到789了'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))

if __name__ == "__main__":
    print("=" * 80)
    print("🚀 Flask + Line Bot 伺服器啟動！")
    print("請確認 ngrok/反向代理/LINE Webhook 皆已設置")
    print("按 Ctrl+C 可隨時關閉伺服器")
    print("=" * 80)
    app.run()
