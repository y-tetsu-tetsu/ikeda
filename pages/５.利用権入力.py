import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import sqlite3 
import hashlib
import subprocess
import sys

conn = sqlite3.connect('NGdatabase.db')
c = conn.cursor()

def create_user():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_user(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def main():
    #st.title("ログイン画面")
    st.sidebar.title('利用権登録・確認')
    menu = ["利用権確認","利用権登録"]
    choice = st.sidebar.selectbox("メニュー",menu)
    if choice == "利用権確認":
        #st.subheader("ログイン画面です")
        username = st.sidebar.text_input("ユーザー名を入力してください")
        password = st.sidebar.text_input("パスワードを入力してください",type='password')
        password = username
        if st.sidebar.button('ログイン'):
            create_user()
            result = login_user(username,password)
            if result:
                st.sidebar.title("{}で既に登録済みです".format(username))
                st.snow()
                st.toast('ログイン失敗', icon='😂')
            else:
                st.warning("入力されたユーザー名は登録されていません")
                st.toast('ログイン失敗', icon='😂')
                st.snow()

    elif choice == "利用権登録":
        st.subheader("利用権を作成します")
        new_user = st.text_input("ユーザー名を入力してください")
        new_password = st.text_input("パスワードを入力してください",type='password')
        new_password = new_user
        if st.button("サインアップ"):
            create_user()
            add_user(new_user,new_password)
            st.success("利用権登録に成功しました")
            st.info("続けてご使用ください")
            st.balloons()
            st.toast('利用権登録成功', icon='😍')
            
if __name__ == '__main__':
    main()


