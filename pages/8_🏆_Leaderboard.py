import streamlit as st
import pandas as pd
from datetime import datetime
from sqlalchemy import text  # Thêm thư viện này để chạy lệnh Insert/Delete

st.set_page_config(page_title="Leaderboard", page_icon="🏆")
st.title("🏆 Hall of Fame")

# --- 0. SAFETY CHECK ---
if 'xp' not in st.session_state:
    st.session_state.xp = 0

# --- 1. CALCULATE XP ---
raw_xp = st.session_state.xp

if isinstance(raw_xp, dict):
    total_score = sum(raw_xp.values())
else:
    total_score = int(raw_xp)

st.info(f"🌟 Your Total XP: **{total_score}**")

# Khởi tạo kết nối chuẩn của Streamlit (Đồng bộ với cấu hình bảo mật mới)
conn = st.connection("mariadb", type="sql")

# --- 2. SUBMIT SCORE ---
with st.form("save_score_form"):
    st.write("### 💾 Save Your Score")
    name = st.text_input("Enter your Name:", max_chars=15)
    submitted = st.form_submit_button("Submit Score")

    if submitted:
        if not name:
            st.warning("Enter a name!")
        elif total_score == 0:
            st.warning("Play first!")
        else:
            try:
                date_now = datetime.now().strftime("%Y-%m-%d %H:%M")

                # Dùng conn.session để ghi dữ liệu an toàn
                with conn.session as s:
                    s.execute(
                        text(
                            "INSERT INTO leaderboard (player_name, xp_score, submission_date) VALUES (:name, :score, :date)"),
                        {"name": name, "score": total_score, "date": date_now}
                    )
                    s.commit()

                st.success(f"✅ {name} saved!")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Save Failed: {e}")

# --- 3. DISPLAY LEADERBOARD ---
st.divider()
st.subheader("🌍 Top Players")

try:
    # Lấy dữ liệu (ttl=0 để luôn lấy điểm mới nhất không bị lưu tạm)
    df = conn.query(
        "SELECT id, player_name as Name, xp_score as XP, submission_date as Date FROM leaderboard ORDER BY xp_score DESC",
        ttl=0)

    if not df.empty:
        public_df = df.copy()
        public_df.insert(0, 'Rank', range(1, 1 + len(public_df)))

        # Hiển thị bảng xếp hạng
        st.dataframe(public_df[['Rank', 'Name', 'XP', 'Date']], hide_index=True, use_container_width=True)
    else:
        st.info("Leaderboard is empty.")
except Exception as e:
    st.error(f"⚠️ Read Error: {e}")

# --- 4. 👮 ADMIN ZONE ---
st.divider()
with st.expander("👮 Admin Zone (Delete Scores)"):
    st.warning("⚠️ Use System ID to delete.")

    # Hiển thị bảng có chứa cột ID cho Admin xem
    try:
        if 'df' in locals() and not df.empty:
            st.dataframe(df, hide_index=True)
    except:
        pass

    col1, col2 = st.columns(2)
    with col1:
        delete_id = st.number_input("System ID to Delete:", min_value=1, step=1)
    with col2:
        admin_pass = st.text_input("Admin Password:", type="password")

    if st.button("🗑️ Delete Score"):
        if "admin" in st.secrets:
            real_pass = st.secrets["admin"]["password"]
            if admin_pass == real_pass:
                try:
                    with conn.session as s:
                        s.execute(
                            text("DELETE FROM leaderboard WHERE id = :id"),
                            {"id": delete_id}
                        )
                        s.commit()
                    st.success(f"✅ ID {delete_id} deleted!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.error("❌ Wrong Password!")
        else:
            st.error("❌ Admin password not configured in secrets.toml")