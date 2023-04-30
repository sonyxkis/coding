
import streamlit as st
import pandas as pd

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

st.dataframe(my_fruit_list)

st.title('My Parents New Healthy Diner')

st.header('🥣 Breakfast Menu')

st.write('🥗 Omega 3 & Blueberry Oatmeal')
st.text('🐔 Kale, Spanich & Rocket Smoothie')
st.text('🥑🍞 Hard-Boiled Free-Range Egg')
   
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
