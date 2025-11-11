import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

pg = st.navigation([
    st.Page(page="pages/home.py", title="🏠 Home"),
    st.Page(page="pages/background.py", title="👨‍💻 Background"),
    st.Page(page="pages/portfolio.py", title="📬 Portfolio"),
],position="top")

pg.run()