import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import sqlite3 
import hashlib
import subprocess
import sys

conn = sqlite3.connect('database.db')
c = conn.cursor()

conn2 = sqlite3.connect('NGdatabase.db')
c2 = conn2.cursor()

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def create_user():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_user(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def check_login_user(username,password):
    c2.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c2.fetchall()
    return data

def main():
    #st.title("ログイン画面")
    st.sidebar.title('ログイン・サインアップ')
    menu = ["ログイン","サインアップ"]
    choice = st.sidebar.selectbox("メニュー",menu)
    if choice == "ログイン":
        #st.subheader("ログイン画面です")
        username = st.sidebar.text_input("ユーザー名を入力してください")
        password = st.sidebar.text_input("パスワードを入力してください",type='password')
        if st.sidebar.button('ログイン'):
            create_user()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                password = username
                result2 = check_login_user(username,password)
                if result2:
                    st.sidebar.title("{}は利用権がありません".format(username))
                    st.snow
                    st.toast('ログイン失敗', icon='😂')
                else:
                    st.sidebar.title("{}でログインしました".format(username)) 
                    st.title("トピック")
                    st.balloons()
                    st.toast('ログイン成功', icon='😍')

                    st.markdown("""

                    ##
                    ##
                    ###### ①池田糖化のHPに掲載されている「田中 大貴」他社へヘッドハンティングされ退職済
                     [田中 大貴](https://jp.linkedin.com/in/%E5%A4%A7%E8%B2%B4-%E7%94%B0%E4%B8%AD-ba7a831b6)
                    """)
                    image = Image.open('./data/tanaka.jpg')       
                    st.image(image,width=700)
                    st.markdown("""

                    ##
                    ###### ②池田糖化東京本社の開発部門の中堅「初鹿 啓之」他社へヘッドハンティングされ退職済
                     """)
                    image = Image.open('./data/hatsushika.jpg')       
                    st.image(image,width=700)
                    st.markdown("""

                    ##
                    ###### ③池田糖化人事部「山岡 弘典」副部長より部長へ昇進
                    [山岡 弘典](https://jp.linkedin.com/in/%E5%BC%98%E5%85%B8-%E5%B1%B1%E5%B2%A1-45777316a)
                                
                    """)

                    image = Image.open('./data/yamaoka.jpg')       
                    st.image(image,width=700)
                    st.markdown("""

                    ##
                    ###### 

                                
                    """)
                    
                    st.markdown("""
                    ##
                    ###### ④開発部門で池田HPに掲載されている中堅「赤木 孝成」他社へヘッドハンティングされ退職
                    [池田HP "赤木 孝成"](https://nakagawatomohiro.pythonanywhere.com/nippo/%E8%B5%A4%E6%9C%A8%20%E5%AD%9D%E6%88%90%EF%BC%9A%E7%A0%94%E7%A9%B6%E9%96%8B%E7%99%BA%E3%81%AE%E5%A3%B0%EF%BD%9C%E7%A0%94%E7%A9%B6%E9%96%8B%E7%99%BA%EF%BD%9C%E6%B1%A0%E7%94%B0%E7%B3%96%E5%8C%96%E5%B7%A5%E6%A5%AD%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE/)
                                
                    """)

                    image = Image.open('./data/2kai7.jpg')       
                    st.image(image,width=700)
                    st.markdown("""

                    ##
                    ###### 

                                
                    """)

                    
                    st.success('随時更新中．．．', icon="✅")

            else:
                st.warning("ユーザー名かパスワードが間違っています")
                st.snow()
                st.toast('ログイン失敗', icon='😂')

    elif choice == "サインアップ":
        st.subheader("新しいアカウントを作成します")
        new_user = st.text_input("ユーザー名を入力してください")
        new_password = st.text_input("パスワードを入力してください",type='password')
        if st.button("サインアップ"):
            create_user()
            add_user(new_user,make_hashes(new_password))
            st.success("アカウントの作成に成功しました")
            st.info("ログイン画面からログインしてください")
            st.balloons()
            st.toast('サインアップ成功', icon='😍')
            
if __name__ == '__main__':
    main()
