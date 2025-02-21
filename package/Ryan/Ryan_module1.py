# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:26:57 2025

@author: user
"""

import requests
import json
import pymysql
import openai
import time
import numpy as np
import dotenv
from .add_data_to_mysql_table import add_data_totable 
from .ask_openai import ask_openai
from linebot.models import  TextMessage, ImageMessage
import os

# dotenv.load_dotenv()

openai.api_key = os.environ["openai_apikey"]

link_msg = ["請直接輸入或轉貼要查詢是否為詐騙的訊息", "請直接輸入或轉貼要查詢是否為詐騙的LINE ID、網站或電話（帶+號即為境外來電，請留意）","開啟連結","請直接輸入或轉貼您要詢問的問題","最新消息"]
user_states = {}

def Ryan_handle_text_message_a(event,line_bot_api):
    global user_states
    # 1. 獲取用戶 ID
    user_id = event.source.user_id
    # 2. 獲取用戶名稱
    profile = line_bot_api.get_profile(user_id)
    user_name = profile.display_name
    # 3. 獲取訊息發送時間
    timestamp = event.timestamp / 1000.0
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    if user_id not in user_states:
        user_states[user_id] = ""
    
        
    if isinstance(event.message, TextMessage):

        user_id = event.source.user_id
        message_type = "text"
        msg = event.message.text
        
        if msg.lower()  in ["april", "vicky", "eva","daryl"]:
            return 
        
        if "bye" in msg.lower():
            return 
        
        if msg in link_msg:
            if msg == "請直接輸入或轉貼要查詢是否為詐騙的訊息":
                user_states[user_id] = "模式一"
                reply = ""
            if msg == "最新消息":
                user_states[user_id] = "模式5"
                reply = "內政部統計110年詐騙案件發生情形，依序為「假投資」、「解除分期付款」及「假網拍」3種手法最多"
                return(TextMessage(text=reply))

                user_states[user_id] = "" 
            if msg == "請直接輸入或轉貼您要詢問的問題":
                user_states[user_id] = "模式4"
                reply = ""
                

            # else: 
            #     user_states[user_id] = ""

        else:
            if user_states[user_id] == "模式一":
                prob = round(np.random.rand() *100)
                
                match prob:
                    case prob if prob <= 35:
                        risk_assessment = "該訊息風險較低，但請保持警覺，避免提供個人敏感資料。"
                    case prob if prob > 35 and prob <= 55:
                        risk_assessment = "該訊息風險為中度，可能包含詐騙元素，請小心處理。"
                    case prob if prob > 55 and prob <= 70:
                        risk_assessment = "該訊息判定為中高風險詐騙，請提高警惕並避免任何回應。"
                    case prob if prob > 70 and prob < 85:
                        risk_assessment = "這是一則高風險詐騙訊息，千萬提高警覺！"
                    case prob if prob >= 85:
                        risk_assessment = "這是一則極高風險的詐騙訊息，請勿回應或點擊任何連結"
                
                reply = f"詐騙機率是{prob}%，{risk_assessment}"
                return(TextMessage(text=reply))
                user_states[user_id] = "" 
            elif user_states[user_id] == "模式4":
                try:                                  # 印出內容
                    reply = ask_openai(msg)
                except:
                    reply = msg
                return(TextMessage(text=reply))

                user_states[user_id] = "" 
            else:
                try:                                  # 印出內容
                    reply = ask_openai(msg)
                except:
                    reply = msg
                return(TextMessage(text=reply))

        user_msg = msg
        reply_msg = reply
        add_data_totable(user_id, user_name, formatted_time, user_msg, reply_msg)
