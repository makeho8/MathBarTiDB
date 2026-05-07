import streamlit as st
import hashlib
from sqlalchemy import text

# 1. Page Config
st.set_page_config(page_title="The Math Bar", page_icon="☕", layout="wide")

# Connect to TiDB
conn = st.connection("mariadb", type="sql")


def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()


# --- INITIALIZE AUTH STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = "student"

# ============================================
# 🔒 THE LOGIN / REGISTER SCREEN
# ============================================
if not st.session_state.logged_in:
    st.title("Welcome to MathBar ☕")
    st.subheader("Please Login or Register to continue.")

    tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])

    # --- LOGIN TAB ---
    with tab1:
        log_user = st.text_input("Username", key="log_u")
        log_pass = st.text_input("Password", type="password", key="log_p")
        if st.button("Login", type="primary"):
            with conn.session as s:
                query = text("SELECT * FROM users WHERE username=:u AND password_hash=:p")
                result = s.execute(query, {"u": log_user, "p": hash_pass(log_pass)}).mappings().first()

                if result:
                    st.session_state.logged_in = True
                    st.session_state.username = result["username"]
                    st.session_state.role = result["role"]

                    if st.session_state.role == "student":
                        # Load XP for students
                        st.session_state.xp = {
                            "Advanced Math": result["xp_adv_math"],
                            "Specialized Math": result["xp_spec_math"],
                            "Prob & Stats": result["xp_prob_stats"],
                            "Discrete Math": result["xp_disc_math"],
                            "Linear Algebra": result["xp_lin_alg"],
                            "Calculus 1": result["xp_calc1"],
                            "Calculus 2": result["xp_calc2"]
                        }
                    st.success(f"Welcome back, {result['username']}!")
                    st.rerun()
                else:
                    st.error("❌ Invalid Username or Password")

    # --- REGISTER TAB ---
    with tab2:
        reg_role = st.radio("I am a:", ["Student", "Teacher"])
        reg_user = st.text_input("New Username", key="reg_u")
        reg_pass = st.text_input("New Password", type="password", key="reg_p")

        # Only ask for Course/Class if they are a student
        if reg_role == "Student":
            course_options = ["Calculus Semester 1", "Advanced Linear Algebra", "Discrete Math 101"]
            class_options = ["Class LQA", "Class LQB", "Class LQC", "Section 01"]
            reg_course = st.selectbox("Select Your Course", course_options)
            reg_class = st.selectbox("Select Your Class", class_options)
        else:
            reg_course = "N/A"
            reg_class = "N/A"

        if st.button("Create Account"):
            with conn.session as s:
                exists = s.execute(text("SELECT username FROM users WHERE username=:u"), {"u": reg_user}).first()
                if exists:
                    st.warning("⚠️ Username already taken. Choose another.")
                else:
                    insert_query = text("""
                        INSERT INTO users (username, password_hash, role, course_name, class_name) 
                        VALUES (:u, :p, :r, :course, :class)
                    """)
                    s.execute(insert_query, {
                        "u": reg_user,
                        "p": hash_pass(reg_pass),
                        "r": reg_role.lower(),
                        "course": reg_course,
                        "class": reg_class
                    })
                    s.commit()
                    st.success("✅ Account created! Please log in on the Login tab.")

    st.stop()  # Stop the rest of the app from rendering


# ============================================
# 🚀 MAIN APP (Logged In)
# ============================================

def save_xp_to_db():
    if st.session_state.role == "student":
        with conn.session as s:
            s.execute(text("""
                UPDATE users SET 
                xp_adv_math = :a, xp_spec_math = :sm, xp_prob_stats = :p, 
                xp_disc_math = :d, xp_lin_alg = :l, xp_calc1 = :c1, xp_calc2 = :c2
                WHERE username = :u
            """), {
                "a": st.session_state.xp["Advanced Math"],
                "sm": st.session_state.xp["Specialized Math"],
                "p": st.session_state.xp["Prob & Stats"],
                "d": st.session_state.xp["Discrete Math"],
                "l": st.session_state.xp["Linear Algebra"],
                "c1": st.session_state.xp["Calculus 1"],
                "c2": st.session_state.xp["Calculus 2"],
                "u": st.session_state.username
            })
            s.commit()


# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4796/4796558.png", width=100)
    st.header(f"👋 {st.session_state.username} ({st.session_state.role.capitalize()})")

    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

    if st.session_state.role == "student":
        if st.button("💾 Save My Progress"):
            save_xp_to_db()
            st.success("Saved to TiDB!")

        total_xp = sum(st.session_state.xp.values())
        st.subheader(f"🌟 Total XP: {total_xp}")
        st.divider()
        for subject, score in st.session_state.xp.items():
            st.write(f"**{subject}:** {score} XP")

# --- ROUTING BASED ON ROLE ---
if st.session_state.role == "teacher":
    st.title("👨‍🏫 Teacher Portal")
    st.info("Welcome to MathBar! As a teacher, you have access to the dashboard.")
    st.page_link("pages/98_🧑🏻‍🏫_Teacher_Dashboard.py", label="Open Teacher Dashboard", icon="📊")
    st.caption("Teacher Data Analysis.")
    st.page_link("pages/99_Test_AI.py", label="Test AI Tutor", icon="🩺", use_container_width=True)
    st.caption("Ask models available.")

elif st.session_state.role == "student":
    st.title("📚 Math Chapters")
    # Keep your existing page links for Chapter 1-7 here!
    # Example:
    st.page_link("pages/1_🚀_Advanced_Math.py", label="Advanced Math", icon="🚀", use_container_width=True)
    st.page_link("pages/2_🌀_Specialized_Math.py", label="Specialized Math", icon="🌀", use_container_width=True)
    st.page_link("pages/3_🎲_Prob_Stats.py", label="Prob & Stats", icon="🎲", use_container_width=True)
    st.page_link("pages/4_🧩_Discrete_Math.py", label="Discrete Math", icon="🧩", use_container_width=True)
    st.page_link("pages/5_📐_Linear_Algebra.py", label="Linear Algebra", icon="📐", use_container_width=True)
    st.page_link("pages/6_📈_Calculus_Single.py", label="Calculus Single", icon="📈", use_container_width=True)
    st.page_link("pages/7_🧊_Calculus_Multi.py", label="Calculus Multi", icon="🧊", use_container_width=True)

    st.divider()
    st.subheader("🏆 Student Hub")
    t1, t2, t3 = st.columns(3)
    with t1:
        st.page_link("pages/8_🏆_Leaderboard.py", label="Leaderboard", icon="🏆")
        st.caption("See who is top of the class.")
    with t2:
        st.page_link("pages/10_📊_My_Stats.py", label="My Stats", icon="📊")
        st.caption("Track your skill radar.")
    with t3:
        st.page_link("pages/9_🤖_AI_Tutor.py", label="AI Tutor", icon="🤖", use_container_width=True)
        st.caption("Ask Gemini or GPT4All.")
