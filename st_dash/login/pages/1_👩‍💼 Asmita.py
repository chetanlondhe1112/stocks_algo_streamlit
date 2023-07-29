import streamlit as st

# CSS file
with open('css/homestyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("👩‍💼 ASMITA")