#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install streamlit


# In[3]:


import streamlit as st
import joblib
import numpy as np


# In[4]:


st.title("House prediction app")
st.image("wallpaper.jpg")


# In[5]:


House_size=st.number_input("Please enter House Size:")
Bedrooms=st.number_input('Please enter No of Bedrooms:')


# In[6]:


model = joblib.load("mul_linear.pkl")


# In[7]:


if st.button("Predict"):
    features = np.array([[House_size,Bedrooms]])
    output= model.predict(features)
    st.write(f"The price of the house is {output[0]}")


# In[ ]:




