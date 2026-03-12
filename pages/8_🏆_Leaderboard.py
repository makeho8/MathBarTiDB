import streamlit as st
import pandas as pd
import mysql.connector 
from datetime import datetime

st.set_page_config(page_title="Leaderboard", page_icon="🏆")
st.title("🏆 Hall of Fame")

# --- 0. SAFETY CHECK (Fixes the AttributeError) ---
if 'xp' not in st.session_state:
    st.session_state.xp = 0

# --- 1. DIRECT CONNECTION FUNCTION ---
def get_connection():
    try:
        # We grab credentials manually from secrets.toml
        creds = st.secrets["mariadb"]
        
        conn = mysql.connector.connect(
            user=creds["user"],
            password=creds["password"],
            host=creds["host"],
            port=creds["port"],
            database=creds["database"]
        )
        return conn
    except Exception as e:
        # If connection fails, return None so the app doesn't crash
        return None

# --- 2. CALCULATE XP ---
raw_xp = st.session_state.xp

if isinstance(raw_xp, dict):
    total_score = sum(raw_xp.values())
else:
    total_score = int(raw_xp)

st.info(f"🌟 Your Total XP: **{total_score}**")

# --- 3. SUBMIT SCORE ---
with st.form("save_score_form"): # Renamed to ensure uniqueness
    st.write("### 💾 Save Your Score")
    name = st.text_input("Enter your Name:", max_chars=15)
    submitted = st.form_submit_button("Submit Score")
    
    if submitted:
        if not name:
            st.warning("Enter a name!")
        elif total_score == 0:
            st.warning("Play first!")
        else:
            conn = get_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    date_now = datetime.now().strftime("%Y-%m-%d %H:%M")
                    
                    # SQL Query
                    query = "INSERT INTO leaderboard (player_name, xp_score, submission_date) VALUES (%s, %s, %s)"
                    values = (name, total_score, date_now)
                    
                    cursor.execute(query, values)
                    conn.commit()
                    
                    st.success(f"✅ {name} saved!")
                    cursor.close()
                    conn.close()
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Save Failed: {e}")
            else:
                st.error("⚠️ Connection failed. Check your database password in secrets.toml")

# --- 4. DISPLAY LEADERBOARD ---
st.divider()
st.subheader("🌍 Top Players")

conn = get_connection()
if conn:
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, player_name, xp_score, submission_date FROM leaderboard ORDER BY xp_score DESC")
        rows = cursor.fetchall()
        
        if rows:
            df = pd.DataFrame(rows, columns=["ID", "Name", "XP", "Date"])
            
            # Create Public View
            public_df = df.copy()
            public_df.insert(0, 'Rank', range(1, 1 + len(public_df)))
            public_df = public_df[['Rank', 'Name', 'XP', 'Date']]
            
            st.dataframe(public_df, hide_index=True, use_container_width=True)
        else:
            st.info("Leaderboard is empty.")
            df = pd.DataFrame()
            
        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"⚠️ Read Error: {e}")
else:
    st.warning("⚠️ Database not connected. Check secrets.toml")

# --- 5. 👮 ADMIN ZONE ---
st.divider()
with st.expander("👮 Admin Zone (Delete Scores)"):
    st.warning("⚠️ Use System ID to delete.")
    
    # We use 'locals()' to check if 'df' exists safely
    if 'df' in locals() and not df.empty:
        st.dataframe(df, hide_index=True)
    
    col1, col2 = st.columns(2)
    with col1:
        delete_id = st.number_input("System ID to Delete:", min_value=1, step=1)
    with col2:
        admin_pass = st.text_input("Admin Password:", type="password")
    
    if st.button("🗑️ Delete Score"):
        # Access admin password safely
        if "admin" in st.secrets:
            real_pass = st.secrets["admin"]["password"]
            if admin_pass == real_pass:
                conn = get_connection()
                if conn:
                    try:
                        cursor = conn.cursor()
                        cursor.execute("DELETE FROM leaderboard WHERE id = %s", (delete_id,))
                        conn.commit()
                        st.success(f"✅ ID {delete_id} deleted!")
                        cursor.close()
                        conn.close()
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.error("❌ Wrong Password!")
        else:
            st.error("❌ Admin password not configured in secrets.toml")