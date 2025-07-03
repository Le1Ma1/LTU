#https://developers.line.biz/flex-simulator/


from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage ,StickerSendMessage, LocationSendMessage,FlexSendMessage 
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
'''
def p01():
    flex_message=FlexSendMessage(
        alt_text='hello',
        contents=
       
    )
    return flex_message
'''

def p02():
    flex_message=FlexSendMessage(
        alt_text='hello',
        contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://developers-resource.landpress.line.me/fx/img/01_2_restaurant.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://line.me/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "uri": "https://line.me/"
    },
    "contents": [
      {
        "type": "text",
        "text": "Brown's Burger",
        "size": "xl",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://developers-resource.landpress.line.me/fx/img/restaurant_regular_32.png"
              },
              {
                "type": "text",
                "text": "$10.5",
                "weight": "bold",
                "margin": "sm",
                "flex": 0
              },
              {
                "type": "text",
                "text": "400kcl",
                "size": "sm",
                "align": "end",
                "color": "#aaaaaa"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://developers-resource.landpress.line.me/fx/img/restaurant_large_32.png"
              },
              {
                "type": "text",
                "text": "$15.5",
                "weight": "bold",
                "margin": "sm",
                "flex": 0
              },
              {
                "type": "text",
                "text": "550kcl",
                "size": "sm",
                "align": "end",
                "color": "#aaaaaa"
              }
            ]
          }
        ]
      },
      {
        "type": "text",
        "text": "Sauce, Onions, Pickles, Lettuce & Cheese",
        "wrap": True,
        "color": "#aaaaaa",
        "size": "xxs"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "color": "#905c44",
        "margin": "xxl",
        "action": {
          "type": "uri",
          "label": "Add to Cart",
          "uri": "https://line.me/"
        }
      }
    ]
  }
}
       
    )
    return flex_message

def p01():
    flex_message=FlexSendMessage(
        alt_text='hello',
        contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://developers-resource.landpress.line.me/fx/img/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://line.me/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Brown Cafe",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
          },
          {
            "type": "text",
            "text": "4.0",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Place",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "Flex Tower, 7-7-4 Midori-ku, Tokyo",
                
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Time",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "10:00 - 23:00",
                
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "CALL",
          "uri": "https://line.me/"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "WEBSITE",
          "uri": "https://line.me/"
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
}
       
    )
    return flex_message


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    getA=event.message.text
    if getA =='123':
        Flex01=p01()
        line_bot_api.reply_message(event.reply_token,Flex01)
    elif getA == '333':
        Flex01=p02()
        line_bot_api.reply_message(event.reply_token,Flex01)
    elif getA =='456':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到456了'))
    elif getA =='789':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到789了'))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    print("=" * 80)
    print("🚀 Flask + Line Bot 伺服器啟動！")
    print("請確認 ngrok/反向代理/LINE Webhook 皆已設置")
    print("按 Ctrl+C 可隨時關閉伺服器")
    print("=" * 80)
    app.run()