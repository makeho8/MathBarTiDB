import streamlit as st
import importlib  # Thư viện này giúp tự động gọi file Python theo tên

def display_content():
    # --- 0. Tạo nút chọn ngôn ngữ ở sidebar ---
    # Kiểm tra xem bộ nhớ đã lưu ngôn ngữ chưa, chưa có thì mặc định là VI
    if "lang" not in st.session_state:
        st.session_state.lang = "VI"

    # Xác định vị trí mặc định của nút gạt
    default_index = 0 if st.session_state.lang == "VI" else 1

    # Hiển thị nút Radio ở thanh bên (sidebar)
    selected_lang = st.sidebar.radio(
        "🌐 Ngôn ngữ / Language",
        ["Tiếng Việt", "English"],
        index=default_index
    )

    # Cập nhật lại bộ nhớ khi người dùng bấm chọn
    st.session_state.lang = "VI" if selected_lang == "Tiếng Việt" else "EN"
    st.sidebar.divider() # Thêm một đường kẻ ngang cho đẹp mắt
    # ------------------------------------------

    # 1. Lấy ngôn ngữ từ hệ thống (Nếu chưa có, mặc định là Tiếng Việt "VI")
    lang = st.session_state.get("lang", "VI")

    # 2. Hiển thị tiêu đề Menu tùy theo ngôn ngữ
    if lang == "EN":
        st.sidebar.markdown("## 📖 Textbook Chapters")
        select_label = "Select Chapter:"
    else:
        st.sidebar.markdown("## 📖 Các chương môn học")
        select_label = "Chọn Chương:"

    # 3. Tạo danh sách (Menu) các môn học ánh xạ tới TÊN FILE PYTHON tương ứng
    if lang == "VI":
        chapters = {
            "Chương 1: Định thức, Ma trận, Hệ PTTT": "materials.advanced_math.content.ch1_matrices_vi",
            "Chương 2: Lý thuyết chuỗi": "materials.advanced_math.content.ch2_series_vi",
            "Chương 3: Hàm nhiều biến số": "materials.advanced_math.content.ch3_multivar_vi",
            "Chương 4: Phương trình vi phân": "materials.advanced_math.content.ch4_diffeq_vi"
        }
    else:
        # Tên hiển thị bằng tiếng Anh, đường dẫn trỏ tới file đuôi _en
        chapters = {
            "Chapter 1: Determinants, Matrices, Systems": "materials.advanced_math.content.ch1_matrices_en",
            "Chapter 2: Series Theory": "materials.advanced_math.content.ch2_series_en",
            "Chapter 3: Functions of Several Variables": "materials.advanced_math.content.ch3_multivar_en",
            "Chapter 4: Differential Equations": "materials.advanced_math.content.ch4_diffeq_en"
        }

    # 4. Dropdown cho sinh viên chọn chương
    choice = st.selectbox(select_label, list(chapters.keys()), key="adv_content_sel")

    st.divider()

    # 5. Tự động tải và chạy file Python được chọn
    try:
        module_path = chapters[choice]
        # Hàm import_module sẽ tự động tìm đúng file Python trong thư mục và tải nó lên
        module = importlib.import_module(module_path)
        module.run()
    except ModuleNotFoundError:
        # Nếu bạn chưa kịp tạo file _en.py hoặc _vi.py, hệ thống sẽ báo lỗi thân thiện thay vì bị sập Web
        if lang == "EN":
            st.info("🚧 English content for this chapter is currently being translated. Please check back later!")
        else:
            st.info("🚧 Nội dung Tiếng Việt cho chương này đang được biên soạn. Vui lòng quay lại sau!")