from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import config
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

def build_five_message():
    return [TextSendMessage(text=t) for t in ('111', '222', '333', '444', '555')]

@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text.strip()

    if text =='123':
        line_bot_api.reply_message(event.reply_token, build_five_message())
    elif text in ('456', '789'):
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text = f'收到{text}了')
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text=text)
        )


if __name__ == "__main__":
    app.run()