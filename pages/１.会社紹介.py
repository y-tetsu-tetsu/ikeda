import streamlit as st
from PIL import Image

st.title("会社紹介")



st.text('社　　名：池田糖化工業㈱')
st.text('本社住所：〒720-8638　広島県福山市桜馬場町2番28号')
st.text('')
st.text('')
st.text('箕島工場：〒721-8558　広島県福山市箕沖町97番地')

image = Image.open('./data/company.jpg')       
st.image(image,width=700)

st.markdown("""
- [会社HP](https://nakagawatomohiro.pythonanywhere.com/nippo/www.ikedatohka.co.jp/)

""")

#　動画
st.text('')
st.text('')
st.text('池田糖化工業株式会社って何をしている会社？.')
video_file = open('./data/池田糖化工業株式会社って何をしている会社？.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)

