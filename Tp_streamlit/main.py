
import streamlit as st

import pandas as pd
import numpy as np

st.title("🎥 Application Streamlit - Film préféré")

x = st.text_input("Quel est ton film préféré ?")
st.write(f"Ton film préféré est : {x}")


st.header("🎬 Liste de films")

data = pd.read_csv("movies.csv")
st.write(data)

st.subheader("📈 Exemple de graphiques aléatoires")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.bar_chart(chart_data)
st.line_chart(chart_data)
