![image](https://user-images.githubusercontent.com/44546284/119443617-85cc0480-bd47-11eb-97d1-ac433eaf1dec.png)


# SITHAR

Here's is the app that we created to generate text using ##*LSTM*## . We used the lyrics of the songs sung by Sithara Ramakrishnan,an Indian Playback singer . 




The text data was created by webscrapping and uploaded in kaggle.
The dataset used .: https://www.kaggle.com/cicykagnes/sithara-song-generator


# Go to the app :

https://share.streamlit.io/cicykagnes/sithar_text_generation/main/sithar_frnt.py

# Team Id :  BFH/8606943178/2021

## Contributers : 
  Cicy K Agnes : https://www.linkedin.com/in/cicykagnes/
  Akthar Naveed : https://www.linkedin.com/in/akthar-naveed-v-921039201/
  Anagha Mohan : https://www.linkedin.com/in/anagha-mohan-4b21a21b4/
                  

# Files :
1. sithar_frnt.py
             The streamlit code for the front end.
             
2. sithar_nlp.py
              Training model
3. sithar_home_bg.jpeg
     about_bg.jpeg
     text_gen_bg.jpeg
              Background images of the app
              

# *Sithar_nlp.py : Definition of functions*

1. Import necessary libraries like NumPy,TensorFlow, etc…..
          
     Libraries used :
                  
                    
          numpy
          streamlit
          tensorflow
          docx
          regex
                  

2. Code contains a class called data_processing which is used for a batch of training examples from a document containing songs.It converts every charaters into lower case letters

3. Methods in data_processing :

         1) getText: which loads data from the document and returns the songs after arranging songs in paragraphs.
 
         2) clean_text: which remove nonalphabetic characters in the songs 

         3) data_xy: this function takes an index and makes x and y dataset, in x contain sequence_length of characters which comes after the given index and y contains elements             of x after x has been shifted one step in the right direction

         4) data_generator: this function generates a batch_size of training examples and returns it at every iteration of an infinite while loop

4. MyModel class is used to build a model. It has a method called forward which returns a compiled model and model contains layers

                1)Embedding layer

                2)bidirectional lstm layer

                3) dropout layer

                4) lstm layer

                5)dropout layer

                6)dense layer

                7)dropout layer

                8)dense layer

5 . Prediction class is used to predict which takes arguments as a model, tokenizer, index to words dictionary in its __init__method.

   It contains a method called pred_next_word which takes the user input and convert that into an index using a dictionary use the trained model to predict the probabilities     over the entire words in the dictionary then select one index and convert it into a word using the dictionary

6 . Train_model is used to train the model. this creates the objects of data_processing and MyModel classes using train the model and saves it in the drive, it returns model and     index to word dictionary and object of tokenizer.  
7 . Then the train_model function is called to get the model and passe the returned values into the method of prediction class object called pred_next_word which is called 20   times to create a paragraph of 20 words through inputting the returned value again into the model in the next iteration.





# Web app and deployment :

   Sithar is created using a tool called streamlit. There are 3 pages namely , home , text generation and about .
   Home displays the name of our app . It has a button to check how to use the app.
   Text generation page has a text input box ,where the user can input the keyword to generate the text.
   The about page has links to the source code , the dataset and to contact the creators .

# Walkthrough video and Code Explanation : 

https://www.loom.com/share/4155ebbd27bb4939a9b55a8f9e2c6c70
