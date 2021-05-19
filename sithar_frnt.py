import streamlit as st
import base64

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences

st.set_page_config(page_title ="Sithar",
                    initial_sidebar_state="collapsed",
                    page_icon="🎼")
tabs = ["Home","Generate music","About"]
page = st.sidebar.radio("Navigation",tabs)

if page =="Home":
    main_bg = "sithar_bg_home.jpeg"
    main_bg_ext = "jpg"

    st.markdown(
    f"""
    <style>
    
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }}

    </style>
    """,
    unsafe_allow_html=True
    )

    html_temp = """ 
        <div style="border:5px red;background-color: #A9A9A9;border-radius: 100px;border-style: outset;"> 
        <h1 style ="font-family:Courier New;font-weight:bold;font-size:80px;color:black;font-style:normal;text-align:center;">S I T H A R</h1> 
        </div> 
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("Sithar is a web app using NLP for generating lyrics in Manglish.Click on How to use the app below to try out our work.")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")

    with st.beta_expander('How to use the app'):
        html_temp = """ 
                <div> 
                <h3 style ="color:black;text-align:center;">1. Go to the top left corner and click on the arrow to go to navigation menu. </h3> 
                <h3 style ="color:black;text-align:center;">2. To generate the text go to 'Text generation' page and input the keyword in Manglish.A sequence of 20 words will be generated. </h3>
                <h3 style ="color:black;text-align:center;">3. To know about the web page and the source code used go to 'About' page. </h3>
                </div> 
                """
        st.markdown(html_temp, unsafe_allow_html=True)
    
if page == 'Generate music':
    main_bg = "sithar_bg.jpeg"
    main_bg_ext = "jpeg"

    st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }}

    </style>
    """,
    unsafe_allow_html=True
    )
    st.header("Generate Music")
    user_input = st.text_input("Input the keyword",' ')
    

if page=="About":
    col1, col2, col3 = st.beta_columns(3)

    with col1:
       st.header("Authors")
       st.markdown(""" **[Cicy K Agnes](https://www.linkedin.com/in/cicykagnes/)**""")
       st.markdown(""" **[Akthar Naveed](https://www.linkedin.com/in/akthar-naveed-v-921039201)**""")
       st.markdown(""" **[Anagha Mohan](https://www.linkedin.com/in/anagha-mohan-4b21a21b4/)**""")
    
    
    with col2:
        st.header("Dataset used")
        st.markdown("""**[Sithara song generator](https://www.kaggle.com/cicykagnes/sithara-song-generator)**""")
    
    with col3:
        st.header("Dates and source code")
        st.text(" ")
        st.markdown("""**[Source code](https://github.com/cicykagnes/sithar)**""")
        st.write("Created : 19/05/2021")
        st.write("Last updated: 19/05/2021")