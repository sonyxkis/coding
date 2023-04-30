
import streamlit as st
import pandas as pd

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')


st.title('My Parents New Healthy Diner')

st.header('🥣 Breakfast Menu')

st.write('🥗 Omega 3 & Blueberry Oatmeal')
st.write('🐔 Kale, Spanich & Rocket Smoothie')
st.write('🥑🍞 Hard-Boiled Free-Range Egg')
   
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

st.dataframe(my_fruit_list)
