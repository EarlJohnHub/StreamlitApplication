import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Skill Track | John Earl", layout="wide")

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
    .skill-box, .project-box {
        text-align: center;
        background-color: #F4F6F7;
        border-radius: 15px;
        padding: 1.2rem;
        box-shadow: 1px 1px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- PAGE HEADER ----------------
st.title("📈 Skill Track So Far")
st.markdown("Here’s a summary of my learning journey — the languages, tools, and projects I’ve worked on while improving my craft as a developer.")
st.divider()

# ---------------- LANGUAGES SECTION ----------------
st.subheader("💬 Languages Learned")

l1, l2, l3, l4, l5 = st.columns(5)

with l1:
    st.markdown('<div class="skill-box">🐍<br>Python<br><progress value="90" max="100"></progress><br>Advanced</div>', unsafe_allow_html=True)
with l2:
    st.markdown('<div class="skill-box">☕<br>Java<br><progress value="75" max="100"></progress><br>Intermediate</div>', unsafe_allow_html=True)
with l3:
    st.markdown('<div class="skill-box">💻<br>C++<br><progress value="65" max="100"></progress><br>Intermediate</div>', unsafe_allow_html=True)
with l4:
    st.markdown('<div class="skill-box">🌐<br>HTML / CSS<br><progress value="85" max="100"></progress><br>Proficient</div>', unsafe_allow_html=True)
with l5:
    st.markdown('<div class="skill-box">⚡<br>JavaScript<br><progress value="60" max="100"></progress><br>Learning</div>', unsafe_allow_html=True)

st.divider()

# ---------------- DATABASE SECTION ----------------
st.subheader("💾 Databases Learned")

db1, db2, db3, db4 = st.columns(4)
with db1:
    st.markdown('<div class="skill-box">🐘<br>PostgreSQL<br><progress value="70" max="100"></progress><br>Intermediate</div>', unsafe_allow_html=True)
with db2:
    st.markdown('<div class="skill-box">🧩<br>MySQL<br><progress value="80" max="100"></progress><br>Proficient</div>', unsafe_allow_html=True)
with db3:
    st.markdown('<div class="skill-box">🗂️<br>SQLite<br><progress value="65" max="100"></progress><br>Intermediate</div>', unsafe_allow_html=True)
with db4:
    st.markdown('<div class="skill-box">☁️<br>Firebase<br><progress value="50" max="100"></progress><br>Basic</div>', unsafe_allow_html=True)

st.divider()

# ---------------- TOOLS & FRAMEWORKS SECTION ----------------
st.subheader("🧰 Tools & Frameworks")

tool1, tool2, tool3, tool4 = st.columns(4)
with tool1:
    st.markdown('<div class="skill-box">🧑‍💻<br>Streamlit<br><progress value="90" max="100"></progress><br>Proficient</div>', unsafe_allow_html=True)
with tool2:
    st.markdown('<div class="skill-box">🖌️<br>Figma<br><progress value="75" max="100"></progress><br>Intermediate</div>', unsafe_allow_html=True)
with tool3:
    st.markdown('<div class="skill-box">🧠<br>TensorFlow<br><progress value="45" max="100"></progress><br>Learning</div>', unsafe_allow_html=True)
with tool4:
    st.markdown('<div class="skill-box">🐙<br>GitHub<br><progress value="80" max="100"></progress><br>Proficient</div>', unsafe_allow_html=True)

st.divider()

# ---------------- PROJECTS SECTION ----------------
st.subheader("💼 Projects Made So Far")

project1, project2 = st.columns(2)
with project1:
    st.markdown("""
        <div class="project-box">
            <h3>📊 Student Grade Analyzer</h3>
            <p>Built a Streamlit app that computes, visualizes, and analyzes student performance using Pandas and Matplotlib.</p>
            <p><b>Tools:</b> Python, Streamlit, Pandas</p>
        </div>
    """, unsafe_allow_html=True)

with project2:
    st.markdown("""
        <div class="project-box">
            <h3>💻 Portfolio Website</h3>
            <p>Developed an interactive portfolio website showcasing my projects, background, and contact links.</p>
            <p><b>Tools:</b> Streamlit, HTML/CSS, GitHub</p>
        </div>
    """, unsafe_allow_html=True)

project3, project4 = st.columns(2)
with project3:
    st.markdown("""
        <div class="project-box">
            <h3>📱 Simple To-Do App</h3>
            <p>A web-based task manager built using Flask and SQLite for tracking daily goals and productivity.</p>
            <p><b>Tools:</b> Python, Flask, SQLite</p>
        </div>
    """, unsafe_allow_html=True)

with project4:
    st.markdown("""
        <div class="project-box">
            <h3>🤖 AI Chat Assistant</h3>
            <p>A conversational bot prototype using OpenAI API to answer basic questions and assist in tasks.</p>
            <p><b>Tools:</b> Python, OpenAI API, Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------- LEARNING PROGRESS METRICS ----------------
st.subheader("📈 Learning Journey Overview")

metric1, metric2, metric3 = st.columns(3)
with metric1:
    st.metric(label="Total Programming Languages", value="5", delta="+1 from last term")
with metric2:
    st.metric(label="Projects Completed", value="8", delta="+3 this year")
with metric3:
    st.metric(label="Average Skill Proficiency", value="78%", delta="+6% growth")

st.divider()

# ---------------- EXPANDER SECTION ----------------
st.subheader("📚 Certificates & Achievements")
with st.expander("View My Certificates and Accomplishments"):
    st.markdown("""
    - 🎖️ **Python for Everyone** – Coursera  
    - 💼 **Web Development Basics** – FreeCodeCamp  
    - 🧠 **Machine Learning Introduction** – Kaggle Learn  
    - 🏅 **Best Mini Project (2024)** – University of the Visayas  
    """)

st.divider()
st.success("Keep learning, keep growing 🚀 — Your skill track continues!")
