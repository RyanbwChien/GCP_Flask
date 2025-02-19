# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:08:12 2025

@author: user
"""

def add_data_totable(ID,NAME,time, user_msg, reply_msg):
    import pymysql
    try:
        db_login = {
            'host':"ryan01.cju2uo8uoepj.us-east-1.rds.amazonaws.com",
            'port':3306,
            "user":"Ryan",
            "password":"220721623ABC",
            "charset": "utf8mb4"
            }
        conn = pymysql.connect(**db_login)
        cur = conn.cursor()
        cur.execute("Use RyanDB")
        
        sql_command = """Insert into Line_member ( \
          `USER ID`, \
          `USERNAME`, \
          `CREATE_TIME`, \
          `USER_MSG`, \
          `SYS_REPLY_MSG`
        ) values (%s, %s, %s, %s, %s);"""
        
        cur.execute(sql_command, (ID, NAME, time, user_msg, reply_msg))
        
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(e)