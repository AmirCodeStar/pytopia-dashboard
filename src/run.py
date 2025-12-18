import streamlit as st
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

try:
    from StringIo import StringIO
except ImportError:
    from io import StringIO

st.title("🖥pytopia-dashboard")


with st.expander('statistics'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        data = json.load(uploaded_file)
        st.json(data)

with st.expander("chart"):
    fig, ax = plt.subplots()
    sns.histplot(np.random.randn(100), ax=ax)

    st.pyplot(fig)