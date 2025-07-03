from flask import Flask, request


from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage
import config, json
import json
app = Flask(__name__)

line_handler = WebhookHandler(config.CHANNEL_SECRET)

@app.route("/")
def home():
  line_bot_api = LineBotApi(config.CHANNEL_ACCESS_TOKEN)
  try:
    msg = request.args.get('msg')
    #https://18b0-2402-7500-958-fc0-887a-7e29-1db6-497b.ngrok-free.app/?msg=123
    if msg != None:
        line_bot_api.push_message('U0c1912507e4638f152abe93c76d9540e', TextSendMessage(text=msg))
        return msg
    else:
        return 'OK'
  except:
    print('error')

if __name__ == "__main__":
    app.run()