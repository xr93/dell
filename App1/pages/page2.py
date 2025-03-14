import streamlit as st

from PIL import Image

st.markdown('#This is page two')

im = Image.open('dell.png')
st.image(im,width=100)