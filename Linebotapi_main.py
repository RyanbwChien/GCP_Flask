
import sys
# sys.path.append(r"C:\Users\user\ryanlinechatbot2")
# sys.path.append(r"C:\Users\user\ryanlinechatbot2\package\Ryan")
from flask import Flask, request, abort
from linebot.models import MessageEvent, TextMessage, ImageMessage
from linebot import LineBotApi, WebhookHandler
# import package
from package import *           # 匯入處理器      
# import inspect
# import inspect
# # 列出套件內的所有函數
# functions = [name for name, obj in inspect.getmembers( package, inspect.isfunction)]

# print("套件中的函數有：")
# for func in functions:
#     print(func)


access_token = '7nbeHQXUhTmL0boi/XUfEnF+FbIpw5c9pCvf5oODmi3xhokSbceUNOd0AsPscwuHusHfLj5p9ixA9IWzTJQW+iIKytefUcXae6JpeX7QK67cGb8ucUgATY/oaj+NPhGbUiAd3f3t3JBnqT7/LOUdBQdB04t89/1O/w1cDnyilFU='
secret = 'e117059ff2261b2c0e6640403208b939'

line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(secret)

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']  # 簽名驗證
    body = request.get_data(as_text=True)            # 接收請求的內容

    try:
        handler.handle(body, signature)  # 處理來自 LINE 的請求
    except Exception as e:
        print("Error:", e)
        abort(400)  # 請求失敗返回 400
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def even(event):

    Ryan_response_b = Ryan_handle_text_message_b(event, line_bot_api)
    Ryan_response_a = Ryan_handle_text_message_a(event, line_bot_api)
    Vicky_response_a = Vicky_handle_text_message_a(event, line_bot_api)
    April_response_a = April_handle_text_message_a(event, line_bot_api)
    Daryl_response_a = Daryl_handle_text_message_a(event, line_bot_api)
    Eva_response_a = Eva_handle_text_message_a(event, line_bot_api)

    
    total = [Ryan_response_a,Ryan_response_b,Vicky_response_a,April_response_a,Daryl_response_a,Eva_response_a] 
    if total == [None]*6:
        return 
    
    responses = [item for item in total if item is not None][0]
    # 合併回覆訊息

    if responses:
        line_bot_api.reply_message(event.reply_token, responses)

@handler.add(MessageEvent, message=ImageMessage)
def even(event):

    Ryan_image_response_a = Ryan_handle_image_message_a(event, line_bot_api)

    
    responses = [item for item in [Ryan_image_response_a] if item is not None][0]
    # 合併回覆訊息
    if responses == []:
        return 
    if responses:
        line_bot_api.reply_message(event.reply_token, responses)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
