import streamlit as st


st.tittle(' AutomeetAI James')

uploaded_file =st.file_uploader("Selecione o seu arquivo", accept_multiple_files=False, type=['mp4'])

mp4_filename = uploaded_file.name