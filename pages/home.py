import streamlit as st

# --- CONFIGURATION & PAGE SETUP ---
# Set the page title and layout
st.set_page_config(page_title="Portfolio | John Earl", layout="wide")

# --- Custom CSS for Styling, Readability, and Round Image ---
# st.markdown("""
#     <style>
#         /* Base Theme */
#         .stApp {
#             background-color: #121212; /* Deep dark background */
#             color: #E0E0E0; /* Light gray text */
#         }
        
#         /* 1. ROUND IMAGE STYLING */
#         /* Target the image element within the first column (profile section) */
#         [data-testid="column"] img {
#             border-radius: 100% !important; 
#             object-fit: cover;
#             width: 250px; 
#             height: 250px;
#             border: 5px solid #00A8E8; /* Optional: A nice blue ring */
#             margin: 0 auto; /* Center the image within its column */
#             display: block; /* Ensure margin auto works */
#         }

#         /* 2. Custom Header Styling (Left-Aligned and Modern) */
#         h1, h2, h3 {
#             color: #00A8E8; /* Bright professional blue */
#             text-align: left; /* Keep titles left-aligned */
#         }
#         h2 {
#              color: #E0E0E0; /* Use light grey for the secondary pitch */
#         }
        
#         /* 3. Button Styling (for the links) */
#         div.stButton > button {
#             background-color: #262626;
#             color: #E0E0E0;
#             border: 1px solid #363636;
#             border-radius: 8px;
#             padding: 10px 20px;
#             font-size: 1.1rem;
#             width: 100%; 
#         }
#         div.stButton > button:hover {
#             background-color: #363636;
#             border-color: #00A8E8;
#         }
        
#         /* 4. Increase readability in containers (Soft Skills/Hobbies) */
#         [data-testid="stContainer"] {
#             border-radius: 10px;
#             padding: 20px;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
#         }

#         /* 5. Ensure profile text is vertically centered with image */
#         [data-testid="column"] > div {
#             display: flex;
#             flex-direction: column;
#             justify-content: center;
#             height: 100%;
#         }

#     </style>
#     """, unsafe_allow_html=True)

with st.container(horizontal_alignment="center"):
    # Use columns to put the image and text next to each other
    profile, description = st.columns([1, 2], vertical_alignment="center")

    with profile:
        # Image will be round due to CSS above
        try:
            st.image("Resource/Earl.png", width=250)
        except FileNotFoundError:
            # Placeholder styling to maintain space if image is missing
            st.markdown(
                '<div style="text-align: center; font-size: 100px; border-radius: 50%; background-color: #262626; width: 250px; height: 250px; line-height: 250px; margin: 0 auto;">👨‍💻</div>', 
                unsafe_allow_html=True
            )
            st.caption("Image Placeholder")

    with description:
        # Content will be aligned next to the image
        st.markdown(
            "<h1 style='text-alignment: center;'> Hello World!</h1>"
            "<h4> I'm John Earl C. Echavez</h4>"
            ,unsafe_allow_html=True
        )
        
st.divider()

#Achievement Section

with st.container():
    st.header("About My Journey")
    achievements, about_me = st.columns(2)
    st.markdown(""" 



""")

    with achievements:
        st.subheader("🏆 Achievements & Milestones")
        st.markdown("""
            - **Dean's List:** (2 Year Consistent)
            - **Talisay City Scholar**
            - **DSPC Radio Broadcaster (2nd Runner up)**
                    """)
        
        st.subheader("Soft Skills")
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                st.write("🗣️ Communication") 
        with col2:
            with st.container(border=True):
                st.write("🙏 Compassion") 
        with col3:
            with st.container(border=True):
                st.write("🤔 Critical Thinking") 

    with about_me:
        st.subheader("👋 Introduction")
        st.markdown(
            """
            Hello! I’m John Earl, a passionate and aspiring software developer who loves building creative and practical solutions through code. 
            I enjoy learning new technologies, exploring how systems work, and improving my skills one project at a time. 
            My goal is to grow into a well-rounded developer who can create meaningful applications that make a difference.
            """
        )
        st.info("I am currently seeking opportunities in Software Development and Data Analytics.")
        
st.divider()

# --- 3. HOBBIES SECTION ---

st.header("💡 Hobbies and Interests")

hobbies1, hobbies2, hobbies3, hobbies4 = st.columns([1, 1, 1, 1])

with hobbies1:
    with st.container(border=True):
        st.markdown('<h3 style="text-align: center; color: #E0E0E0;">Reading Tech Blogs</h3>', unsafe_allow_html=True)
        st.write("Hobby 1 description placeholder.")
with hobbies2:
    with st.container(border=True):
        st.markdown('<h3 style="text-align: center; color: #E0E0E0;">Gaming (Strategy)</h3>', unsafe_allow_html=True)
        st.write("Hobby 2 description placeholder.")
with hobbies3:
    with st.container(border=True):
        st.markdown('<h3 style="text-align: center; color: #E0E0E0;">DIY Electronics</h3>', unsafe_allow_html=True)
        st.write("Hobby 3 description placeholder.")
with hobbies4:
    with st.container(border=True):
        st.markdown('<h3 style="text-align: center; color: #E0E0E0;">Coding Challenges</h3>', unsafe_allow_html=True)
        st.write("Hobby 4 description placeholder.")

st.divider()

# --- 4. REACH OUT AND CONNECT SECTION ---

st.header("🔗 Reach Out and Connect")
st.write("Find me on social media and professional networks below.")

link1, link2, link3 = st.columns(3)

with link1:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YourUsername)", unsafe_allow_html=True)
    st.text("GitHub (Projects)")
with link2:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/YourUsername)", unsafe_allow_html=True)
    st.text("LinkedIn (Professional)")
with link3:
    st.markdown("[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@example.com)", unsafe_allow_html=True)
    st.text("Email (Contact)")

# --- Final Footer ---
st.markdown("""
<div style="text-align: center; padding-top: 50px; font-size: 0.9em; color: #6e6e6e;">
    <p>Portfolio by John Earl | Built with Streamlit 2024</p>
</div>
""", unsafe_allow_html=True)