import streamlit as st
from PIL import Image

st.set_page_config(page_title="test",page_icon=":shark:",layout="wide")
st.markdown('#Hello world')

st.sidebar.write("this is main page")

im = Image.open('dell.png')
st.image(im,width=100)
