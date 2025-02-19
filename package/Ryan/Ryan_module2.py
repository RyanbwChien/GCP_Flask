# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:27:48 2025

@author: user
"""

# handlers/handler_b.py
from linebot.models import TextMessage, ImageMessage

def Ryan_handle_text_message_b(event,line_bot_api):
    if isinstance(event.message, TextMessage):
        text = event.message.text
        if "bye" in text.lower():
            return(TextMessage(text="Goodbye from Developer B!"))
            
