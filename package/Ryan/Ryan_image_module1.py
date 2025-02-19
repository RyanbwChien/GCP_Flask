# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:27:48 2025

@author: user
"""

# handlers/handler_b.py
from linebot.models import TextMessage, ImageMessage
import time

def Ryan_handle_image_message_a(event,line_bot_api):
    if isinstance(event.message, ImageMessage):
        message_type = "image"
        image_id = event.message.id
        image_content = line_bot_api.get_message_content(image_id)
        user_id = event.source.user_id
        # 2. 獲取用戶名稱
        profile = line_bot_api.get_profile(user_id)
        user_name = profile.display_name
        # 3. 獲取訊息發送時間
        timestamp = event.timestamp / 1000.0
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    # 打印出訊息內容和用戶資訊
        print(f"Message Type: {message_type}")
        print(f"User Name: {user_name}")
        print(f"User ID: {user_id}")
        print(f"Timestamp: {formatted_time}")
        print(f"text: {image_content }")
        return(TextMessage(text="Recive photo from Ryan!"))
            
