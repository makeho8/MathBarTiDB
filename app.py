# my app
import streamlit as st

# 1. Page Config
st.set_page_config(page_title="The Math Bar", page_icon="☕", layout="wide")

#import password
#password.check_password

# ============================================
# 🚀 THE APP CONTENT (Only runs if Logged In)
# ============================================

# 2. The Backpack (Session State)
# --- INITIALIZE SCORES ---
if "xp" not in st.session_state:
    # Instead of just 0, we track every subject separately
    st.session_state.xp = {
        "Advanced Math": 0,
        "Specialized Math": 0,
        "Prob & Stats": 0,
        "Discrete Math": 0,
        "Linear Algebra": 0,
        "Calculus 1": 0,
        "Calculus 2": 0
    }

# Helper to calculate Total XP (Sum of all subjects)
total_xp = sum(st.session_state.xp.values())

# 3. --- SIDEBAR (Detailed Subject Breakdown) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4796/4796558.png", width=100)
    st.header("🎓 Student Profile")

    # A. Calculate Total for a summary
    total_xp = sum(st.session_state.xp.values())
    st.metric("🌟 Total XP", total_xp, help="Sum of all subject scores")

    st.divider()

    # B. SUBJECT BREAKDOWN (The Loop)
    st.subheader("📊 Subject Scores")

    # We loop through the dictionary to show each subject independently
    for subject, score in st.session_state.xp.items():
        # Create a 2-column layout for neatness (Name on left, Score on right)
        c1, c2 = st.columns([3, 1])
        with c1:
            st.write(f"**{subject}**")
            # Visual progress bar (capped at 100 for visual style)
            progress_val = min(score, 100)
            st.progress(progress_val)
        with c2:
            st.write(f"{score}")

    st.divider()

    # C. RESET BUTTON (Specific to the Dictionary)
    if st.button("🔄 Reset All"):
        # Reset every subject back to 0
        for key in st.session_state.xp:
            st.session_state.xp[key] = 0
        st.rerun()

    st.write("---")
    st.write("Select a topic above to start practicing!")

# 4. Main Content -----------------------
st.title("☕ Welcome to The Math Bar")

# A cleaner, more inspiring intro
st.markdown("""
### 🚀 Your Digital Campus for Advanced Mathematics
Ready to upgrade your skills? You are in the right place.
* **📚 Learn:** Master 7 specialized math modules with interactive graphs.
* **🤖 Ask:** Get instant answers from our **Hybrid AI Tutor** (Online & Offline).
* **📊 Track:** Watch your **Skill Radar** grow as you complete quizzes.
""")

st.info("💡 **Pro Tip:** Check the Sidebar to see your current **Level** and **XP Breakdown**!")


# --- MAIN MENU ---
st.divider()
# 📚 SECTION 1: STUDY MODULES (The 7 Subjects)
st.subheader("📚 Study Modules")

# Row 1: The Core Math
c1, c2, c3 = st.columns(3)
with c1: st.page_link("pages/1_🚀_Advanced_Math.py", label="Advanced Math", icon="🚀", use_container_width=True)
with c2: st.page_link("pages/2_🌀_Specialized_Math.py", label="Specialized Math", icon="🌀", use_container_width=True)
with c3: st.page_link("pages/3_🎲_Prob_Stats.py", label="Prob & Stats", icon="🎲", use_container_width=True)

# Row 2: Logic & Linear
c4, c5, c6 = st.columns(3)
with c4: st.page_link("pages/4_🧩_Discrete_Math.py", label="Discrete Math", icon="🧩", use_container_width=True)
with c5: st.page_link("pages/5_📐_Linear_Algebra.py", label="Linear Algebra", icon="📐", use_container_width=True)
with c6: st.page_link("pages/6_📈_Calculus_Single.py", label="Calculus Single", icon="📈", use_container_width=True)

# Row 3: Advanced Calculus (Just one item, so we center it or keep it left)
c7, c8, c9 = st.columns(3)
with c7: st.page_link("pages/7_🧊_Calculus_Multi.py", label="Calculus Multi", icon="🧊", use_container_width=True)
# c8 and c9 are empty to keep the grid alignment

st.divider()

# 🏆 SECTION 2: STUDENT HUB (The 3 Tools)
st.subheader("🏆 Student Hub")

# Now we have exactly 5 tools, so they fit perfectly in one row!
t1, t2, t3, t4, t5 = st.columns(5)

with t1:
    st.page_link("pages/8_🏆_Leaderboard.py", label="Leaderboard", icon="🏆", use_container_width=True)
    st.caption("See who is top of the class.")

with t2:
    st.page_link("pages/10_📊_My_Stats.py", label="My Stats", icon="📊", use_container_width=True)
    st.caption("Track your skill radar.")

with t3:
    st.page_link("pages/9_🤖_AI_Tutor.py", label="AI Tutor", icon="🤖", use_container_width=True)
    st.caption("Ask Gemini or GPT4All.")

with t4:
    st.page_link("pages/99_Test_AI.py", label="Test AI Tutor", icon="🩺", use_container_width=True)
    st.caption("Ask models available.")

with t5:
    st.page_link("pages/98_🧑🏻‍🏫_Teacher_Dashboard.py", label="Teacher Dashboard", icon="🧑🏻‍🏫", use_container_width=True)
    st.caption("Teacher Data Analysis.")

