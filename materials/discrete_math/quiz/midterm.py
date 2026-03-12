import streamlit as st

def run():
    st.header("📝 Discrete Math: Mid-Term Exam")
    st.info("Pass this exam to earn +100 XP for the Leaderboard!")
    
    # Initialize score for this specific exam session
    score = 0
    
    # --- QUESTION 1 ---
    st.write("**Q1: Vector Addition**")
    st.latex(r"[1, 2] + [3, 4] = ?")
    a1 = st.radio("Select Answer Q1:", ["[4, 6]", "[3, 8]", "[2, 2]"], key="mid_q1")
    
    # --- QUESTION 2 ---
    st.write("**Q2: Scalar Multiplication**")
    st.latex(r"2 \cdot [5, -1] = ?")
    a2 = st.radio("Select Answer Q2:", ["[10, -2]", "[7, 1]", "[10, -1]"], key="mid_q2")

    st.divider()
    
    # --- SUBMIT BUTTON ---
    if st.button("Submit Exam"):
        # Check Answers
        if a1 == "[4, 6]": score += 1
        if a2 == "[10, -2]": score += 1
        
        # Grading Logic
        if score == 2:
            st.balloons()
            st.success(f"Perfect Score! You earned 100 XP.")
            
            # 🏆 CRITICAL: UPDATE THE GLOBAL LEADERBOARD
            if 'xp' not in st.session_state: 
                st.session_state.xp = 0
            st.session_state.xp["Discrete Math"] += 100
            
        elif score == 1:
            st.warning("You got 1/2 correct. Study more to earn XP.")
        else:
            st.error("Failed. Please review Chapter 1 & 2.")