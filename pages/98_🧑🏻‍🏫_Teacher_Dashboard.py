import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Teacher Dashboard", page_icon="👨‍🏫", layout="wide")

# --- 1. KIỂM TRA QUYỀN TRUY CẬP ---
if st.session_state.get("role") != "teacher":
    st.error("❌ Truy cập bị từ chối: Khu vực này chỉ dành cho Giáo viên.")
    st.stop()

# --- 2. HEADER VÀ NÚT LOGOUT (GÓC TRÊN PHẢI) ---
col_title, col_logout = st.columns([8, 2])
with col_title:
    st.title(f"👨‍🏫 Chào mừng, {st.session_state.username}")
with col_logout:
    st.write("")  # Tạo khoảng trống cho cân đối
    if st.button("🚪 Đăng xuất", key="logout_teacher", use_container_width=True):
        st.session_state.clear()
        st.rerun()

st.write("Quản lý lớp học và theo dõi tiến độ của sinh viên.")
st.divider()

conn = st.connection("mariadb", type="sql")

# --- 3. BỘ LỌC (FILTERS) ---
st.subheader("🗂️ Bộ lọc lớp học")
c1, c2 = st.columns(2)

# Lấy danh sách Khóa học và Lớp học để làm menu dropdown
try:
    # Lấy danh sách Course và Class từ DB
    courses_df = conn.query("SELECT DISTINCT course_name FROM users WHERE role='student'")
    classes_df = conn.query("SELECT DISTINCT class_name FROM users WHERE role='student'")

    course_list = ["Tất cả Khóa học"] + courses_df["course_name"].tolist()
    class_list = ["Tất cả Lớp"] + classes_df["class_name"].tolist()
except:
    course_list = ["Tất cả Khóa học"]
    class_list = ["Tất cả Lớp"]

with c1:
    selected_course = st.selectbox("Chọn Khóa học:", course_list)
with c2:
    selected_class = st.selectbox("Chọn Lớp học:", class_list)

# --- 4. TRUY VẤN DỮ LIỆU (FIX LỖI VALUEERROR) ---
# CHÚ Ý: query_str phải là chuỗi (string) thuần túy, không dùng hàm text() ở đây
query_str = """
    SELECT username, course_name, class_name,
    (xp_adv_math + xp_spec_math + xp_prob_stats + xp_disc_math + xp_lin_alg + xp_calc1 + xp_calc2) as total_xp 
    FROM users WHERE role = 'student'
"""
params = {}

if selected_course != "Tất cả Khóa học":
    query_str += " AND course_name = :course"
    params["course"] = selected_course

if selected_class != "Tất cả Lớp":
    query_str += " AND class_name = :class"
    params["class"] = selected_class

try:
    # FIX: Truyền trực tiếp string vào conn.query
    df = conn.query(query_str, params=params)

    if df.empty:
        st.info("Chưa có dữ liệu sinh viên cho lựa chọn này.")
    else:
        # --- 5. HIỂN THỊ BIỂU ĐỒ VÀ BẢNG ---
        col_chart, col_data = st.columns([2, 1])

        with col_chart:
            st.subheader("📈 Biểu đồ tổng XP")
            # Vẽ biểu đồ
            st.bar_chart(df.set_index("username")["total_xp"], color="#FF4B4B")

        with col_data:
            st.subheader("📋 Danh sách lớp")
            st.dataframe(
                df[["username", "course_name", "class_name", "total_xp"]],
                column_config={
                    "username": "Tên Sinh viên",
                    "course_name": "Khóa học",
                    "class_name": "Lớp",
                    "total_xp": "Tổng XP"
                },
                hide_index=True,
                use_container_width=True
            )

        # --- 6. XUẤT FILE EXCEL ---
        st.divider()
        st.subheader("📥 Xuất dữ liệu")
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Stats')

        st.download_button(
            label="Tải file Excel báo cáo",
            data=buffer.getvalue(),
            file_name=f"MathBar_Report_{selected_class}.xlsx",
            mime="application/vnd.ms-excel"
        )

except Exception as e:
    st.error(f"⚠️ Lỗi truy vấn dữ liệu: {e}")