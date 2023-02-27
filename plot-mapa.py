import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1, 2) / [2000, 2000] + [25.67507, -100.31847], columns=['lat', 'lon'])


st.map(map_data)