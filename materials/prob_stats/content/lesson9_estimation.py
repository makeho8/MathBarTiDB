import streamlit as st
import numpy as np
from scipy import stats


def run():
    st.header("Bài 9: Ước lượng tham số và Nguyên tắc Kiểm định")
    st.markdown("---")

    # --- PHẦN 1: ƯỚC LƯỢNG ĐIỂM ---
    st.subheader("1. Ước lượng điểm (Point Estimation)")

    with st.expander("📝 Khái niệm"):
        st.write("""
        Ước lượng điểm là việc dùng một giá trị duy nhất tính từ mẫu để đại diện cho tham số chưa biết của tổng thể.
        """)
        st.markdown("""
        * **Ước lượng cho kỳ vọng ($\\mu$):** Dùng trung bình mẫu $\\overline{X}$.
        * **Ước lượng cho phương sai ($\\sigma^2$):** Dùng phương sai mẫu hiệu chỉnh $S^2_{hc}$.
        * **Ước lượng cho tỉ lệ ($p$):** Dùng tỉ lệ mẫu $f = m/n$.
        """)
        st.info("💡 Một ước lượng tốt cần đảm bảo tính **không chệch**, **hiệu quả** và **nhất quán**.")

    # --- PHẦN 2: ƯỚC LƯỢNG KHOẢNG ---
    st.subheader("2. Ước lượng khoảng (Interval Estimation)")

    st.write("""
    Vì ước lượng điểm khó có thể chính xác tuyệt đối, chúng ta xây dựng một khoảng giá trị $(a, b)$ sao cho tham số cần tìm nằm trong đó với một **độ tin cậy $1-\alpha$** cho trước (thường là 95% hoặc 99%).
    """)

    with st.expander("📐 Công thức tổng quát"):
        st.latex(r"\theta \in [\hat{\theta} - \epsilon, \hat{\theta} + \epsilon]")
        st.write("Trong đó $\\epsilon$ là **độ chính xác** (sai số biên).")
        st.markdown("""
        * **Trường hợp mẫu lớn ($n \\geq 30$):** Dùng phân phối chuẩn $U$ (hoặc $Z$).
        * **Trường hợp mẫu nhỏ, chưa biết $\\sigma$:** Dùng phân phối Student $t$.
        """)

    # --- PHẦN 3: NGUYÊN TẮC KIỂM ĐỊNH GIẢ THUYẾT ---
    st.divider()
    st.subheader("3. Các nguyên tắc chung của kiểm định giả thuyết")

    st.write("Kiểm định giả thuyết là việc sử dụng dữ liệu mẫu để đánh giá một giả định (giả thuyết) về tổng thể.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Cặp giả thuyết:**")
        st.write("- **Giả thuyết không ($H_0$):** Giả thuyết cần kiểm tra (thường là trạng thái bình thường).")
        st.write("- **Đối thuyết ($H_1$):** Giả thuyết ngược lại với $H_0$.")

    with col2:
        st.markdown("**Các loại sai lầm:**")
        st.error("- **Sai lầm loại I ($\\alpha$):** Bác bỏ $H_0$ khi $H_0$ đúng (Dương tính giả).")
        st.warning("- **Sai lầm loại II ($\\beta$):** Chấp nhận $H_0$ khi $H_0$ sai (Âm tính giả).")

    with st.expander("🚀 Quy trình thực hiện (5 bước)"):
        st.markdown("""
        1. **Lập cặp giả thuyết:** $H_0$ và $H_1$.
        2. **Chọn mức ý nghĩa $\\alpha$:** Xác suất mắc sai lầm loại I tối đa cho phép.
        3. **Chọn tiêu chuẩn kiểm định:** (Ví dụ: $U$ hoặc $t$) phù hợp với bài toán.
        4. **Xác định miền bác bỏ $W_{\\alpha}$:** Dựa trên $\\alpha$ và bảng tra cứu.
        5. **Tính giá trị quan sát $G_{qs}$ và kết luận:** Nếu $G_{qs} \\in W_{\\alpha}$ thì bác bỏ $H_0$, ngược lại chưa có cơ sở bác bỏ $H_0$.
        """)

    # --- PHẦN 4: CÔNG CỤ TÍNH KHOẢNG TIN CẬY ---
    st.divider()
    st.subheader("🛠️ Máy tính Khoảng tin cậy cho Trung bình")

    c1, c2, c3 = st.columns(3)
    x_mean = c1.number_input("Trung bình mẫu (x̄)", value=100.0)
    s_std = c2.number_input("Độ lệch chuẩn mẫu (s)", value=15.0)
    n_sample = c3.number_input("Kích thước mẫu (n)", value=50, min_value=1)
    conf_level = st.select_slider("Độ tin cậy (1-α)", options=[0.90, 0.95, 0.99], value=0.95)

    if st.button("Tính khoảng tin cậy"):
        alpha = 1 - conf_level
        # Dùng phân phối chuẩn cho mẫu lớn hoặc đã biết sigma
        z_score = stats.norm.ppf(1 - alpha / 2)
        margin_error = z_score * (s_std / np.sqrt(n_sample))

        lower = x_mean - margin_error
        upper = x_mean + margin_error

        st.success(f"Với độ tin cậy {conf_level * 100}%, giá trị kỳ vọng μ nằm trong khoảng:")
        st.latex(rf"{lower:.4f} < \mu < {upper:.4f}")
        st.info(f"Độ chính xác (sai số): {margin_error:.4f}")

    # --- SIDEBAR ---
    st.sidebar.info("""
    **Ghi chú:** 
    Trong y khoa, việc chọn $\alpha$ cực kỳ quan trọng để cân bằng giữa việc "bỏ sót người bệnh" và "chẩn đoán nhầm người khỏe".
    """)