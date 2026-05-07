import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.set_page_config(page_title="My Stats", page_icon="📊")

# --- 1. SAFETY CHECK (Crucial!) ---
# If the user refreshes this page directly, 'xp' might not exist yet.
# We re-initialize it here just in case.
# --- 1. SAFETY CHECK (Crucial!) ---
# Kiểm tra: Nếu xp chưa có, HOẶC xp không phải là dạng từ điển (dict) thì mới tạo lại
if "xp" not in st.session_state or not isinstance(st.session_state.xp, dict):
    st.session_state.xp = {
        "Advanced Math": 0,
        "Specialized Math": 0,
        "Prob & Stats": 0,
        "Discrete Math": 0,
        "Linear Algebra": 0,
        "Calculus 1": 0,
        "Calculus 2": 0
    }

st.title("📊 My Skill Matrix")

# --- 2. DATA PREPARATION ---
scores = st.session_state.xp
total_xp = sum(scores.values())
subjects = list(scores.keys())
values = list(scores.values())

# --- 3. TOP LEVEL METRICS ---
col1, col2, col3 = st.columns(3)
col1.metric("🌟 Total XP", total_xp)

# Find strongest and weakest subjects safely
if total_xp > 0:
    strongest = max(scores, key=scores.get)
    weakest = min(scores, key=scores.get)
else:
    strongest = "None yet"
    weakest = "None yet"

col2.metric("💪 Strongest Skill", strongest)
col3.metric("🌱 Needs Focus", weakest)

st.divider()

# --- 4. VISUALIZATION: RADAR CHART (The "Gamer" View) ---
st.subheader("🕸️ Skill Radar")

# We need to "close the loop" for a radar chart by repeating the first value at the end
values_closed = values + values[:1]
angles = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Draw the outline and fill
ax.plot(angles, values_closed, color='#FF4B4B', linewidth=2)
ax.fill(angles, values_closed, color='#FF4B4B', alpha=0.25)

# Fix the labels to match the angles
ax.set_xticks(angles[:-1])
ax.set_xticklabels(subjects, size=10)

# Clean up the grid
ax.set_yticklabels([]) # Hide the radial numbers for a cleaner look
ax.spines['polar'].set_visible(False) # Hide the outer circle border

st.pyplot(fig)

# --- 5. VISUALIZATION: BAR CHART (For precision) ---
with st.expander("📈 View Detailed Bar Chart"):
    st.bar_chart(scores)

# --- 6. RESET BUTTON ---
st.divider()
if st.button("🔄 Reset All Progress"):
    for key in st.session_state.xp:
        st.session_state.xp[key] = 0
    st.rerun()

