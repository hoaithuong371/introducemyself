import streamlit as st
from PIL import Image
from pathlib import Path

# --- PATH SETTINGS ---
# Since Streamlit does not support __file__, directly set paths for assets and CSS.
css_file = "styles/main.css"
profile_pic = "assets/profile-pic.webp"
# schedule_pic = "assets/schedule-pic.png"  # Uncomment if you want this image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Profile | Hoai Thuong Le"
PAGE_ICON = "🐱"
NAME = "Hoai Thuong Le"
DESCRIPTION = """
Student of VNUHCM-University of Science – VNUHCM-US.
"""
EMAIL = "20280094@student.hcmus.edu.vn"
PHONE = "0372267703"
ADDRESS = "1 Nguyen Canh Di St, Tan Binh District, HCM City"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Sidebar menu options
st.sidebar.success("Select a page under!")
menu = ["Overview", "Schedule", "Inforgraphic"]
choice = st.sidebar.selectbox(" ", menu)

# --- Overview Page ---
if choice == "Overview":
    with st.spinner("Loading Overview..."):  # Spinner during loading
        # --- Load CSS & Profile Pic ---
        try:
            with open(css_file) as f:
                st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
        except FileNotFoundError:
            st.warning(f"CSS file '{css_file}' not found!")
        
        try:
            profile_pic = Image.open(profile_pic)
        except FileNotFoundError:
            st.warning(f"Profile picture '{profile_pic}' not found!")

        # --- HERO SECTION ---
        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.image(profile_pic, use_container_width=False)

        with col2:
            st.title(NAME)
            st.write("📫", EMAIL)
            st.write(DESCRIPTION)
            st.write("📞", PHONE)
            st.write("📍", ADDRESS)
            
        # --- HARD SKILLS ---
        st.write('\n')
        st.subheader("HARD SKILLS")
        st.write("👩‍💻", "PYTHON, C++/C#, R, MATLAB")
        st.write("📊", "MATH & STATISTICS")
        st.write("🔎", "RESEARCH")

        # --- HOBBIES ---
        st.write('\n')
        st.subheader("HOBBIES")
        st.write(
            """
        - ✔️ Lying on the floor.
        - ✔️ Listen to music; especially rap, indie, pop music, classic music.
        - ✔️ Watch a movie. My fav movie genre is action movie.
        - ✔️ Playing chess & Chinese chess.
        - ✔️ Hang out with my friends.
        """
        )
        
        # --- DISADVANTAGES ---
        st.write('\n')
        st.subheader("DISADVANTAGES")
        st.write(
            """
        - Not good at communication.
        - My English is not so good but I'm trying to improve.
        - Sometimes I'm feeling a little lazy.
        - I procrastinate when it's time to work and study.
        - Not good at time management.
        """
        )

# --- Schedule Page ---
if choice == "Schedule":
    try:
        schedule_pic = Image.open("assets/schedule-pic.webp") 
        schedule_pic = schedule_pic.resize((800, 800))
        st.image(schedule_pic, caption="My schedule", use_container_width=True)
    except FileNotFoundError:
        st.warning("Schedule image not found!")

# --- Infographic Page ---
if choice == "Inforgraphic":
    try:
        info_pic = Image.open("assets/LEHOAITHUONG.webp") 
        st.image(info_pic, caption="My infographic", use_container_width=True)
    except FileNotFoundError:
        st.warning("Infographic image not found!")

