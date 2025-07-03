from flask import Flask, request



from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage

import json
app = Flask(__name__)



@app.route("/")
def home():
  line_bot_api = LineBotApi('LINE_CHANNEL_ACCESS_TOKEN')
  try:
    msg = request.args.get('msg')
    #https://XXXX.ngrok-free.app/?msg=1
    if msg == '1':
      # 如果 msg 等於 1，發送文字訊息
      line_bot_api.push_message('User ID', TextSendMessage(text='hello'))
    elif msg == '2':
      # 如果 msg 等於 2，發送表情貼圖
      line_bot_api.push_message('User ID', StickerSendMessage(package_id=1, sticker_id=2))
    elif msg == '3':
      # 如果 msg 等於 3，發送圖片
      imgurl = 'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png'
      line_bot_api.push_message('User ID', ImageSendMessage(original_content_url=imgurl, preview_image_url=imgurl))
    elif msg == '4':
      # 如果 msg 等於 4，發送地址資訊
      line_bot_api.push_message('User ID', LocationSendMessage(title='總統府',
                                                address='100台北市中正區重慶南路一段122號',
                                                latitude='25.040319874750914',
                                                longitude='121.51162883484746'))
    else:
      msg = 'ok'
    return msg
  except:
    print('error')

if __name__ == "__main__":
    app.run()