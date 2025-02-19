# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:26:57 2025

@author: user
"""



from linebot.models import  TextMessage, ImageMessage

def Daryl_handle_text_message_a(event,line_bot_api):
    if isinstance(event.message, TextMessage):
        text = event.message.text
        if "daryl" in text.lower():
            return(TextMessage(text="Hello from Daryl!"))
