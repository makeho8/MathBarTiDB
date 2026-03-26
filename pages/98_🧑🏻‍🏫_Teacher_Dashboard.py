import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Teacher Dashboard", page_icon="👨‍🏫", layout="wide")

# --- 1. HỆ THỐNG ĐĂNG NHẬP (AUTHENTICATION) ---
# Kiểm tra xem giảng viên đã đăng nhập chưa
if "teacher_logged_in" not in st.session_state:
    st.session_state.teacher_logged_in = False

# Nếu chưa đăng nhập, hiển thị màn hình yêu cầu mật khẩu
if not st.session_state.teacher_logged_in:
    st.title("🔒 Khu vực dành riêng cho Giảng viên")
    st.info("Vui lòng nhập mật khẩu Giảng viên để truy cập Hệ thống phân tích.")

    pwd = st.text_input("Mật khẩu:", type="password")

    # Lấy mật khẩu từ Streamlit Secrets, nếu không có thì dùng mật khẩu mặc định
    try:
        correct_pwd = st.secrets["admin"]["password"]
    except:
        correct_pwd = "MathBarMaster"

    if st.button("Đăng nhập"):
        if pwd == correct_pwd:
            st.session_state.teacher_logged_in = True
            st.rerun()
        else:
            st.error("❌ Sai mật khẩu! Vui lòng thử lại.")

    # Dừng chạy toàn bộ code bên dưới nếu chưa đăng nhập thành công
    st.stop()

# --- 2. GIAO DIỆN CHÍNH CỦA TEACHER DASHBOARD ---
# Nút đăng xuất ở thanh bên (Sidebar)
if st.sidebar.button("🚪 Đăng xuất"):
    st.session_state.teacher_logged_in = False
    st.rerun()

st.title("👨‍🏫 Teacher Dashboard - Trung tâm Phân tích")
st.markdown("Theo dõi tiến độ, điểm kinh nghiệm (XP) và sự tham gia của sinh viên theo thời gian thực.")

# --- 3. LẤY DỮ LIỆU TỪ TIDB CLOUD ---
try:
    # Kết nối Database
    conn = st.connection("mariadb", type="sql")
    # Lấy dữ liệu bảng leaderboard (ttl=0 đảm bảo luôn tải dữ liệu mới nhất, không dùng bộ nhớ đệm)
    df = conn.query("SELECT * FROM leaderboard ORDER BY xp_score DESC", ttl=0)

    if df.empty:
        st.warning("📭 Chưa có sinh viên nào nộp điểm lên hệ thống.")
    else:
        # --- 4. THỐNG KÊ TỔNG QUAN (KEY METRICS) ---
        total_students = len(df)
        avg_xp = df["xp_score"].mean()
        top_student = df.iloc[0]["player_name"]

        st.subheader("📊 Tổng quan Lớp học")
        col1, col2, col3 = st.columns(3)
        col1.metric("👥 Tổng số Sinh viên", total_students)
        col2.metric("⭐ Điểm XP Trung bình", f"{avg_xp:.0f} XP")
        col3.metric("🏆 Sinh viên Dẫn đầu", top_student)

        st.divider()

        # --- 5. BIỂU ĐỒ & BẢNG DỮ LIỆU CHI TIẾT ---
        col_chart, col_data = st.columns([2, 1])

        with col_chart:
            st.subheader("📈 Phân bố Điểm XP")
            # Tạo biểu đồ cột thể hiện điểm của từng sinh viên
            chart_data = df.set_index("player_name")["xp_score"]
            st.bar_chart(chart_data, color="#FF4B4B")

        with col_data:
            st.subheader("📋 Danh sách Chi tiết")
            # Hiển thị bảng dữ liệu (Ẩn cột ID để nhìn sạch sẽ hơn)
            st.dataframe(
                df[["player_name", "xp_score", "submission_date"]],
                column_config={
                    "player_name": "Tên Sinh viên",
                    "xp_score": "Điểm XP",
                    "submission_date": "Thời gian nộp"
                },
                hide_index=True,
                use_container_width=True
            )

except Exception as e:
    st.error(f"⚠️ Không thể tải dữ liệu: {e}")

# --- 6. TẢI DỮ LIỆU EXCEL
st.divider()
st.subheader("📥 Xuất Dữ Liệu")
# Tạo một bộ nhớ đệm để lưu file Excel
buffer = io.BytesIO()
# Ghi dữ liệu từ DataFrame (df) vào file Excel trong bộ nhớ đệm
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Diem_MathBar', index=False)
# Nút tải xuống
st.download_button(
    label="Tải file Excel (.xlsx)",
    data=buffer.getvalue(),
    file_name="Danh_Sach_Diem_MathBar.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
