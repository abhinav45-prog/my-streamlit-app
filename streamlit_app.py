import streamlit as st

st.set_page_config(page_title="BMI App", page_icon="👋", layout="centered")

pg_1 = st.Page("calculator.py", title="BMI Calculator")
pg_2 = st.Page("practice2.py", title="Pizza Order")

pg = st.navigation([pg_1, pg_2])
pg.run()