import streamlit as st
import pandas as pd
import numpy as np

#Numpy genera 20 renglones y 3 columnas
chart_data = pd.DataFrame(np.random.randn(20,5), columns=['a','b','c','d','e'])

st.dataframe(chart_data)
st.line_chart(chart_data)