import streamlit as st
import pandas as pd

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Background | John Earl", layout="wide")

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
    .main {
        padding: 0rem 3rem;
    }
    h1, h2, h3 {
        text-align: center;
        color: #2E86C1;
    }
    .section {
        padding: 1.5rem 0;
    }
    .progress-container {
        background-color: #EBF5FB;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🔍 Background Check")
st.divider()

# ---------------- ADDRESS SECTION ----------------
st.subheader("🏠 Home Address")
st.markdown("I currently live in **Cebu City, Philippines**, a vibrant and growing tech hub in the Visayas region. 🌴")

# Example: Map of Cebu (use approximate coordinates)
location_data = pd.DataFrame({
    'lat': [10.3157],
    'lon': [123.8854]
})
st.map(location_data, zoom=11)

st.info("📍 Location shown is approximate for privacy and demonstration purposes.")

st.divider()

# ---------------- EDUCATION SECTION ----------------
st.subheader("🎓 Education Progress")

# Education details
st.markdown("""
**Bachelor of Science in Information Technology**  
University of the Visayas  
_Expected Graduation: 2026_  
""")

st.markdown("#### Academic Milestones")
progress_col1, progress_col2 = st.columns(2)

with progress_col1:
    st.write("**Year 1:** Fundamentals of Programming ✅")
    st.progress(100)
    st.write("**Year 2:** Data Structures & Web Development ✅")
    st.progress(100)

with progress_col2:
    st.write("**Year 3:** Software Engineering & Database Systems (Ongoing)")
    st.progress(70)
    st.write("**Year 4:** Capstone Project & Internship (To be completed)")
    st.progress(20)

st.divider()

# ---------------- SKILL PROGRESS SECTION ----------------
st.subheader("🧠 Skill Development Progress")

col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Python** 🐍")
    st.progress(85)
    st.write("**Java** ☕")
    st.progress(75)
with col2:
    st.write("**HTML / CSS / JS** 🌐")
    st.progress(80)
    st.write("**Streamlit** ⚡")
    st.progress(90)
with col3:
    st.write("**Databases (SQL)** 💾")
    st.progress(70)
    st.write("**Git / GitHub** 🧩")
    st.progress(80)

st.divider()

# ---------------- PERSONAL INFO SECTION ----------------
st.subheader("👤 Personal Information")

colA, colB = st.columns(2)
with colA:
    st.write("**Full Name:** John Earl Echavez")
    st.write("**Birthdate:** March 10, 2004")
    st.write("**Nationality:** Filipino")
with colB:
    st.write("**Languages:** English, Filipino, Cebuano")
    st.write("**Personality Type:** INTP (The Thinker)")
    st.write("**Interests:** Technology, Music, Design, Games")

st.divider()

# ---------------- HIGHLIGHT SECTION ----------------
st.subheader("🌟 Highlights & Achievements")
with st.expander("See my Highlights"):
    st.markdown("""
    - 🥇 Placed in a regional programming competition  
    - 💻 Developed multiple web-based applications in Python and Java  
    - 🤝 Volunteered as a coding mentor for junior students  
    - 📚 Continuously learning new tools and frameworks  
    """)

st.divider()

# ---------------- EXTRA FUNCTIONALITY SECTION ----------------
st.subheader("📈 My Learning Goals Tracker")

goal1, goal2, goal3 = st.columns(3)
with goal1:
    st.metric(label="Projects Completed", value=12, delta="+3 since last term")
with goal2:
    st.metric(label="Certifications Earned", value=4, delta="+1 new badge")
with goal3:
    st.metric(label="Ongoing Courses", value=2, delta="Learning AI Basics 🤖")

st.divider()

st.success("Background information updated successfully! ✅")

