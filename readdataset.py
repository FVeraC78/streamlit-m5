import streamlit as st
import pandas as pd

names = 'dataset.csv'

names_data = pd.read_csv(names)

st.title('Streamlit and Pandas')
st.dataframe(names_data)