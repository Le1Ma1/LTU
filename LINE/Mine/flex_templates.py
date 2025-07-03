def get_flex_message(key, alt="FLEX訊息"):
    from linebot.models import FlexSendMessage, TextSendMessage
    content = FLEX_TEMPLATES.get(key)
    if content:
        return FlexSendMessage(alt_text=alt, contents=content)
    else:
        return TextSendMessage(text="找不到這個 Flex 模板！")

flex_templates = {
    "01": {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://developers-resource.landpress.line.me/fx/img/01_1_cafe.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {"type": "uri", "uri": "https://line.me/"}
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
                        {"type": "icon", "size": "sm", "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"},
                        {"type": "icon", "size": "sm", "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"},
                        {"type": "icon", "size": "sm", "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"},
                        {"type": "icon", "size": "sm", "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"},
                        {"type": "icon", "size": "sm", "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"},
                        {"type": "text", "text": "4.0", "size": "sm", "color": "#999999", "margin": "md", "flex": 0}
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
                                {"type": "text", "text": "Place", "color": "#aaaaaa", "size": "sm", "flex": 1},
                                {"type": "text", "text": "Flex Tower, 7-7-4 Midori-ku, Tokyo", "color": "#666666", "size": "sm", "flex": 5}
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {"type": "text", "text": "Time", "color": "#aaaaaa", "size": "sm", "flex": 1},
                                {"type": "text", "text": "10:00 - 23:00", "color": "#666666", "size": "sm", "flex": 5}
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
                    "action": {"type": "uri", "label": "CALL", "uri": "https://line.me/"}
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {"type": "uri", "label": "WEBSITE", "uri": "https://line.me/"}
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
    },
    "02": {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://developers-resource.landpress.line.me/fx/img/01_2_restaurant.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {"type": "uri", "uri": "https://line.me/"}
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "action": {"type": "uri", "uri": "https://line.me/"},
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
                                {"type": "icon", "url": "https://developers-resource.landpress.line.me/fx/img/restaurant_regular_32.png"},
                                {"type": "text", "text": "$10.5", "weight": "bold", "margin": "sm", "flex": 0},
                                {"type": "text", "text": "400kcl", "size": "sm", "align": "end", "color": "#aaaaaa"}
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {"type": "icon", "url": "https://developers-resource.landpress.line.me/fx/img/restaurant_large_32.png"},
                                {"type": "text", "text": "$15.5", "weight": "bold", "margin": "sm", "flex": 0},
                                {"type": "text", "text": "550kcl", "size": "sm", "align": "end", "color": "#aaaaaa"}
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
                    "action": {"type": "uri", "label": "Add to Cart", "uri": "https://line.me/"}
                }
            ]
        }
    }
}
