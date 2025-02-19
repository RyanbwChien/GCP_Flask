# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:09:39 2025

@author: user
"""

def ask_openai(message):
    import openai
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages = [
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "system", "content": "請盡量回覆的字數少於100字以內" },
        {
            "role": "user",
            "content": f"{message}",
        },
    ],
        # prompt = message,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.8,
        # handle_parsing_errors=True,
    )  
    answer = response.choices[0].message.content.strip()
    return answer