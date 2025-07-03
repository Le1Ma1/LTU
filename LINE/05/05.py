from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage ,StickerSendMessage
import random,config
app = Flask(__name__)

line_bot_api = LineBotApi(config.CHANNEL_ACCESS_TOKEN)
line_handler = WebhookHandler(config.CHANNEL_SECRET)

@app.route('/')
def home():
    return 'Hello World'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#https://developers.line.biz/en/docs/messaging-api/sticker-list/#sticker-definitions

reply_arr=[
    TextMessage(text='hello123'),
    StickerSendMessage(package_id=446,sticker_id=1988),
    TextMessage(text='hello345')
]


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    getA=event.message.text
    if getA =='123':
        line_bot_api.reply_message(event.reply_token, reply_arr)
    elif getA =='456':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到456了'))
    elif getA =='789':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到789了'))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()