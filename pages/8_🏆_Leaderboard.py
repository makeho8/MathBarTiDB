import streamlit as st
from datetime import datetime
from sqlalchemy import text

st.set_page_config(page_title="Leaderboard", page_icon="🏆")

# --- 1. KIỂM TRA ĐĂNG NHẬP ---
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Vui lòng đăng nhập tại trang chủ để xem bảng xếp hạng.")
    st.stop()

# --- 2. HEADER VÀ NÚT ĐĂNG XUẤT (Góc trên bên phải) ---
col_title, col_logout = st.columns([8, 2])
with col_title:
    st.title("🏆 Hall of Fame")
with col_logout:
    if st.button("🚪 Đăng xuất", key="logout_leaderboard", use_container_width=True):
        st.session_state.clear()
        st.rerun()

conn = st.connection("mariadb", type="sql")

# --- 3. NỘP ĐIỂM (CHỈ DÀNH CHO STUDENT) ---
if st.session_state.get("role") == "student":
    # Lấy XP an toàn
    raw_xp = st.session_state.get("xp", 0)
    total_score = sum(raw_xp.values()) if isinstance(raw_xp, dict) else int(raw_xp)

    st.info(f"🌟 Tổng XP của bạn: **{total_score}**")

    with st.form("save_score_form"):
        st.write(f"### 💾 Lưu điểm của {st.session_state.username}")
        submitted = st.form_submit_button("Publish My Score to Global Leaderboard")

        if submitted:
            if total_score == 0:
                st.warning("Hãy làm bài tập để kiếm XP trước!")
            else:
                try:
                    with conn.session as s:
                        exists = s.execute(
                            text("SELECT id FROM leaderboard WHERE player_name = :name"),
                            {"name": st.session_state.username}
                        ).first()

                        if exists:
                            s.execute(
                                text(
                                    "UPDATE leaderboard SET xp_score = :score, submission_date = :date WHERE player_name = :name"),
                                {"score": total_score, "date": datetime.now(), "name": st.session_state.username}
                            )
                        else:
                            s.execute(
                                text(
                                    "INSERT INTO leaderboard (player_name, xp_score, submission_date) VALUES (:name, :score, :date)"),
                                {"name": st.session_state.username, "score": total_score, "date": datetime.now()}
                            )
                        s.commit()
                    st.success("🎉 Đã cập nhật điểm lên Bảng Xếp Hạng!")
                except Exception as e:
                    st.error(f"⚠️ Lỗi lưu điểm: {e}")
else:
    st.info("👨‍🏫 Chế độ Giáo viên: Bạn có thể xem bảng xếp hạng bên dưới.")

# --- 4. HIỂN THỊ GLOBAL RANKINGS (ĐÃ FIX LỖI) ---
st.divider()
st.subheader("🌍 Global Rankings")

try:
    # SỬ DỤNG conn.query() THAY VÌ pd.read_sql
    query = "SELECT player_name, xp_score, submission_date FROM leaderboard ORDER BY xp_score DESC LIMIT 10"
    df = conn.query(query)

    if not df.empty:
        df.index = df.index + 1
        st.dataframe(
            df,
            column_config={
                "player_name": "Tên Học Sinh",
                "xp_score": st.column_config.NumberColumn("Tổng XP", format="%d ⭐"),
                "submission_date": st.column_config.DatetimeColumn("Ngày cập nhật", format="DD/MM/YYYY")
            },
            use_container_width=True
        )
    else:
        st.info("Bảng xếp hạng đang trống. Hãy là người đầu tiên!")
except Exception as e:
    st.error("⚠️ Không thể tải dữ liệu Bảng xếp hạng.")
    st.code(str(e))  # In ra lỗi chi tiết nếu vẫn còn vướng mắc ở TiDB