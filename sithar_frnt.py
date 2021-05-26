import streamlit as st
import base64
import os
import numpy as np
import re
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model , load_model , model_from_json

st.set_page_config(page_title ="Sithar",
                    initial_sidebar_state="collapsed",
                    page_icon="🎼")
tabs = ["Home","Generate music","About"]
page = st.sidebar.radio("Navigation",tabs)

if page =="Home":
    main_bg = "345.jpg"
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
        <div style="border:5px black;border-style: outset;"> 
        <h1 style ="font-family:Courier New;font-weight:bold;font-size:80px;color:black;font-style:normal;text-align:center;">S I T H A R</h1> 
        </div> 
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.markdown("**| Sithar is a web app using NLP for generating lyrics in Manglish. Click on How to use the app below to try out our work. |**")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text("🤭 Sithar sure will make you laugh with the variety poems it writes. 🤭")
    st.text(" ")
    st.text(" ")
    st.text(" ")

    with st.beta_expander('How to use the app'):
        html_temp = """ 
                <div> 
                <h3 style ="color:black;text-align:center;">1. Go to the top left corner and click on the arrow to go to navigation menu. </h3> 
                <h3 style ="color:black;text-align:center;">2. To generate the text go to 'Text generation' page and input the keyword in Manglish. A sequence of 20 words will be generated. </h3>
                <h3 style ="color:black;text-align:center;">3. To know about the web page and the source code used go to 'About' page. </h3>
                </div> 
                """
        st.markdown(html_temp, unsafe_allow_html=True)
    
if page == 'Generate music':
    
    main_bg = "123.jpg"
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
    
    json_file = open('my_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("my_model.h5") 
    print("Loaded model from disk")

    loaded_model.summary()

    html_temp = """ 
        <div> 
        <h1 style ="color:brown;text-align:center;font-family:Courier New;font-weight:bold">|| GENERATE MUSIC ||</h1> 
        </div> 
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    #st.text("Use keywords to generate lyrics.For example, njan , ente , thedunnu , uyire ,")
    html_temp = """ 
        <div> 
        <h3 style ="color:brown;text-align:center">Use keywords to generate lyrics. For example, njan , ente ,chiri , thedunnu , uyire ,jeevitham ,sanjaaram , etc.. Please use the same keywords as mentioned in lower case letters or please visit the dataset to get more keywords.</h3> 
        <h4> For better experience in Mobile screens use light mode </h4>
        </div> 
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.text("")
    next_char = st.text_input("INPUT THE KEYWORD",'')
    res = any(ele.isupper() for ele in next_char)
    if res:
        st.write("**Please enter all lowercase letters.**")
    elif next_char != '':
        max_vocab=2101
        sequence_length = 256
    

        tokenizer = Tokenizer(num_words = max_vocab)
        text = (open("sithara_songs_data.txt").read())

        lower_data = text.lower()           
        split_data = lower_data.splitlines()      
        final = ''     
        def clean_text(text):
            text = re.sub(r',', '', text)
            text = re.sub(r'\'', '',  text)
            text = re.sub(r'\"', '', text)
            text = re.sub(r'\(', '', text)
            text = re.sub(r'\)', '', text)
            text = re.sub(r'\n', '', text)
            text = re.sub(r'“', '', text)
            text = re.sub(r'”', '', text)
            text = re.sub(r'’', '', text)
            text = re.sub(r'\.', '', text)
            text = re.sub(r';', '', text)
            text = re.sub(r':', '', text)
            text = re.sub(r'\-', '', text)
            return text

        for line in split_data:
           line = clean_text(line)  
           final += '\n' + line

        final_data = final.split('\n')       
        tokenizer.fit_on_texts(final_data)
        word2idx = tokenizer.word_index
        idx2word = dict(map(reversed, word2idx.items()))
        words = word2idx.keys()
        words_indexes = [word2idx[w] for w in words]
        len_word = len(words_indexes)
        
        
        def pred_next_word(inputs):
            temperature=1.0
            inputs=next_char
        
            input_ids =  word2idx[inputs]
            
            input_ids = np.array([[input_ids]], dtype=np.float32)
            predicted_logits = loaded_model.predict(input_ids)
            predicted_logits = predicted_logits[:, -1, :]
            predicted_logits = predicted_logits/temperature

            predicted_ids = tf.random.categorical(predicted_logits, num_samples=1)
            predicted_ids = tf.squeeze(predicted_ids, axis=-1)
            predicted_chars = idx2word[int(np.squeeze(np.squeeze(predicted_ids)))]
            return predicted_chars
                    
        result = [next_char]
        if not word2idx.__contains__(next_char):
            st.write("**This keyword is not in the dataset.Try another keyword to generate an epic poem 😉 **")
        else:
            st.write("**How long should your song be ?**")
            q= st.slider("Slide me to enter the length.",1,20)
            for n in range(q):
                next_char = pred_next_word(next_char)
                result.append(" ")
                result.append(next_char)

            result = tf.strings.join(result)
            st.write(result.numpy().decode('utf-8'), '\n\n' + '_'*80)
            

if page=="About":
  
    main_bg = "about_bg.jpeg"
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
        st.markdown("**Dates and source code**")
        st.text(" ")
        st.markdown("""**[Source code](https://github.com/cicykagnes/sithar)**""")
        st.write("Created : 19/05/2021")
        st.write("Last updated: 26/05/2021")
