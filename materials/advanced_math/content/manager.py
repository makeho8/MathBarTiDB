import streamlit as st
import materials.advanced_math.content.ch1_matrices as ch1
import materials.advanced_math.content.ch2_series as ch2
import materials.advanced_math.content.ch3_multivar as ch3
import materials.advanced_math.content.ch4_diffeq as ch4

def display_content():
    st.sidebar.markdown("## 📖 Textbook Chapters")

    # Map friendly names to modules
    chapter_map = {
        "Chương 1: Định thức, Ma trận, Hệ PTTT": ch1,
        "Chương 2: Lý thuyết chuỗi": ch2,
        "Chương 3: Hàm nhiều biến số": ch3,
        "Chương 4: Phương trình vi phân": ch4
    }

    choice = st.selectbox("Select Chapter:", list(chapter_map.keys()), key="adv_content_sel")

    st.divider()
    # Run the selected module
    chapter_map[choice].run()