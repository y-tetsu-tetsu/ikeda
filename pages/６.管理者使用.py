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

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data


def main():
    #st.title("ログイン画面")
    st.sidebar.title('ログイン')
    menu = ["ログイン"]
    choice = st.sidebar.selectbox("メニュー",menu)
    if choice == "ログイン":
        #st.subheader("ログイン画面です")
        username = st.sidebar.text_input("ユーザー名を入力してください")
        password = st.sidebar.text_input("パスワードを入力してください",type='password')
        if st.sidebar.button('ログイン'):
            create_user()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            if result and username == "admin":
               st.balloons()
               st.toast('ログイン成功', icon='😍')
               # データベースに接続する
               conn = sqlite3.connect('database.db')
               c = conn.cursor()

               # レコードをユーザー名の昇順で取得する
               st.title("database.db")
               for row in c.execute('SELECT * FROM userstable ORDER BY username ASC'):
                    st.success(row)

               # データベースへのアクセスが終わったら close する
               conn.close()

               # データベースに接続する
               conn = sqlite3.connect('NGdatabase.db')
               c = conn.cursor()

               # レコードをユーザー名の昇順で取得する
               st.title("NGdatabase.db")
               for row in c.execute('SELECT * FROM userstable ORDER BY username ASC'):
                    st.success(row)

               # データベースへのアクセスが終わったら close する
               conn.close()
                
            else:
               st.warning("ユーザー名かパスワードが間違っています")
               st.snow()
               st.toast('ログイン失敗', icon='😂')
           
if __name__ == '__main__':
    main()


