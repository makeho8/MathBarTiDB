import streamlit as st
import importlib  # Thư viện này giúp tự động gọi file Python theo tên

def display_content():
    # --- 0. Tạo nút chọn ngôn ngữ ở sidebar ---
    # Kiểm tra xem bộ nhớ đã lưu ngôn ngữ chưa, chưa có thì mặc định là VI
    if "lang" not in st.session_state:
        st.session_state.lang = "VI"

    # Xác định vị trí mặc định của nút gạt (0: Tiếng Việt, 1: English)
    default_index = 0 if st.session_state.lang == "VI" else 1

    # Hiển thị nút Radio ở thanh bên (sidebar)
    selected_lang = st.sidebar.radio(
        "🌐 Ngôn ngữ / Language",
        ["Tiếng Việt", "English"],
        index=default_index,
        key="prob_stats_lang_toggle"
    )

    # Cập nhật lại bộ nhớ khi người dùng bấm chọn
    st.session_state.lang = "VI" if selected_lang == "Tiếng Việt" else "EN"
    st.sidebar.divider()

    # 1. Lấy ngôn ngữ từ hệ thống
    lang = st.session_state.get("lang", "VI")

    # 2. Hiển thị tiêu đề Menu tùy theo ngôn ngữ
    if lang == "EN":
        st.sidebar.markdown("## 📖 Course Chapters")
        select_label = "Select Chapter:"
        error_msg = "Content for this chapter is being updated. Please try again later!"
    else:
        st.sidebar.markdown("## 📖 Danh sách chương")
        select_label = "Chọn chương học:"
        error_msg = "Nội dung chương này đang được cập nhật. Vui lòng quay lại sau!"

    # 3. Định nghĩa danh sách các chương (Mapping)
    # Lưu ý: Đường dẫn này phải khớp với cấu trúc thư mục thực tế
    if lang == "VI":
        chapters = {
            "Bài 1: Sự kiện ngẫu nhiên và xác suất": "materials.prob_stats.content.lesson1_events",
            "Bài 2: Xác suất có điều kiện": "materials.prob_stats.content.lesson2_cond_prob",
            "Bài 3: Công thức Bayes": "materials.prob_stats.content.lesson3_bayes",
            "Bài 4: Biến ngẫu nhiên & Hàm phân phối": "materials.prob_stats.content.lesson4_rv_dist",
            "Bài 5: Tham số đặc trưng": "materials.prob_stats.content.lesson5_parameters",
            "Bài 6: Các phân phối thường gặp": "materials.prob_stats.content.lesson6_common_dist",
            "Bài 7: BNN nhiều chiều": "materials.prob_stats.content.lesson7_multidim",
            "Bài 8: Mẫu ngẫu nhiên": "materials.prob_stats.content.lesson8_sampling",
            "Bài 9: Ước lượng tham số": "materials.prob_stats.content.lesson9_estimation",
            "Bài 10: Kiểm định giả thuyết": "materials.prob_stats.content.lesson10_testing"
        }
    else:
        # Tên hiển thị bằng tiếng Anh (Bạn có thể tạo các file _en tương ứng sau này)
        chapters = {
            "Chapter 1: Basic Probability": "materials.prob_stats.content.ch1_prob",
            "Chapter 2: Random Variables": "materials.prob_stats.content.ch2_vars",
            "Chapter 3: 2D Random Variables": "materials.prob_stats.content.ch3_2dvars",
            "Chapter 4: Limit Theorems": "materials.prob_stats.content.ch4_limit_theorems"
        }

    # 4. Dropdown cho sinh viên chọn chương
    choice = st.selectbox(select_label, list(chapters.keys()), key="prob_stats_sel")

    st.divider()

    # 5. Tự động tải và chạy file Python được chọn
    try:
        module_path = chapters[choice]
        # Tải module động
        module = importlib.import_module(module_path)
        # Gọi hàm run() trong mỗi file chương
        module.run()
    except ModuleNotFoundError:
        st.warning(error_msg)
    except Exception as e:
        st.error(f"Đã xảy ra lỗi khi tải nội dung: {e}")