import streamlit as st
import numpy as np
from scipy.stats import norm, t


def run():
    st.header("Chương 7: Kiểm định giả thuyết thống kê")
    st.markdown("---")

    # --- PHẦN 1: CƠ SỞ LÝ THUYẾT ---
    st.subheader("Phần 1. Các khái niệm cơ bản")

    with st.expander("📝 1. Giả thuyết và Đối thuyết"):
        st.write("""
        - **Giả thuyết không ($H_0$):** Giả thuyết về một vấn đề nào đó (thường là dấu bằng).
        - **Đối thuyết ($H_1$):** Giả thuyết ngược lại với $H_0$.
        - **Mức ý nghĩa ($\\alpha$):** Xác suất mắc sai lầm loại I (bác bỏ $H_0$ khi $H_0$ đúng). Thường chọn 0.05 hoặc 0.01.
        """)

    with st.expander("⚖️ 2. Quy tắc quyết định"):
        st.write("""
        Để kiểm định, ta tính **Giá trị quan sát ($T_{qs}$)** từ mẫu, sau đó so sánh với **Miền bác bỏ ($W_{\\alpha}$)**:
        - Nếu $T_{qs} \\in W_{\\alpha}$: Bác bỏ $H_0$, chấp nhận $H_1$.
        - Nếu $T_{qs} \\notin W_{\\alpha}$: Chưa đủ cơ sở bác bỏ $H_0$.
        """)

    # --- PHẦN 2: KIỂM ĐỊNH TRUNG BÌNH (1 TỔNG THỂ) ---
    st.divider()
    st.subheader("Phần 2. Kiểm định Trung bình $\\mu$")

    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown("**Các cặp giả thuyết:**")
        st.write("1. $H_0: \\mu = \\mu_0$; $H_1: \\mu \\neq \\mu_0$ (2 phía)")
        st.write("2. $H_0: \\mu = \\mu_0$; $H_1: \\mu > \\mu_0$ (phía phải)")
        st.write("3. $H_0: \\mu = \\mu_0$; $H_1: \\mu < \\mu_0$ (phía trái)")

    with col2:
        st.info("**Tiêu chuẩn kiểm định:**")
        st.latex(r"Z = \frac{\overline{x} - \mu_0}{\sigma / \sqrt{n}} \text{ (Nếu biết } \sigma \text{)}")
        st.latex(r"T = \frac{\overline{x} - \mu_0}{s / \sqrt{n}} \text{ (Nếu chưa biết } \sigma \text{)}")

    # --- PHẦN 3: CÔNG CỤ KIỂM ĐỊNH TỰ ĐỘNG ---
    st.divider()
    st.subheader("🛠️ Máy tính kiểm định nhanh")

    test_type = st.selectbox("Chọn loại bài toán",
                             ["Kiểm định Trung bình (1 mẫu)", "Kiểm định Tỉ lệ (1 mẫu)"],
                             key="ch7_test_type")

    c1, c2, c3 = st.columns(3)
    alpha = c1.number_input("Mức ý nghĩa (α)", 0.01, 0.20, 0.05, step=0.01, key="ch7_alpha")
    side = c2.selectbox("Loại kiểm định", ["2 phía (≠)", "Phía phải (>)", "Phía trái (<)"], key="ch7_side")

    if test_type == "Kiểm định Trung bình (1 mẫu)":
        n = c3.number_input("Kích thước mẫu (n)", value=100, min_value=1, key="ch7_n_mu")
        col_in1, col_in2, col_in3 = st.columns(3)
        mu0 = col_in1.number_input("Giá trị giả thuyết (μ0)", value=50.0)
        x_bar = col_in2.number_input("Trung bình mẫu (x̄)", value=52.0)
        std = col_in3.number_input("Độ lệch chuẩn (s hoặc σ)", value=8.0)

        # Tính toán
        t_stat = (x_bar - mu0) / (std / np.sqrt(n))

        if n >= 30:
            if side == "2 phía (≠)":
                crit = norm.ppf(1 - alpha / 2)
                p_val = 2 * (1 - norm.cdf(abs(t_stat)))
                reject = abs(t_stat) > crit
            elif side == "Phía phải (>)":
                crit = norm.ppf(1 - alpha)
                p_val = 1 - norm.cdf(t_stat)
                reject = t_stat > crit
            else:
                crit = -norm.ppf(1 - alpha)
                p_val = norm.cdf(t_stat)
                reject = t_stat < crit
        else:
            df = n - 1
            if side == "2 phía (≠)":
                crit = t.ppf(1 - alpha / 2, df)
                p_val = 2 * (1 - t.cdf(abs(t_stat), df))
                reject = abs(t_stat) > crit
            elif side == "Phía phải (>)":
                crit = t.ppf(1 - alpha, df)
                p_val = 1 - t.cdf(t_stat, df)
                reject = t_stat > crit
            else:
                crit = -t.ppf(1 - alpha, df)
                p_val = t.cdf(t_stat, df)
                reject = t_stat < crit

    else:  # Kiểm định tỉ lệ
        n = c3.number_input("Kích thước mẫu (n)", value=100, min_value=1, key="ch7_n_p")
        col_in1, col_in2 = st.columns(2)
        p0 = col_in1.number_input("Tỉ lệ giả thuyết (p0)", 0.0, 1.0, 0.5)
        f = col_in2.number_input("Tỉ lệ mẫu (f)", 0.0, 1.0, 0.55)

        t_stat = (f - p0) / np.sqrt(p0 * (1 - p0) / n)
        if side == "2 phía (≠)":
            crit = norm.ppf(1 - alpha / 2)
            p_val = 2 * (1 - norm.cdf(abs(t_stat)))
            reject = abs(t_stat) > crit
        elif side == "Phía phải (>)":
            crit = norm.ppf(1 - alpha)
            p_val = 1 - norm.cdf(t_stat)
            reject = t_stat > crit
        else:
            crit = -norm.ppf(1 - alpha)
            p_val = norm.cdf(t_stat)
            reject = t_stat < crit

    # Hiển thị kết quả
    st.info(f"**Giá trị thống kê quan sát:** {t_stat:.4f}")
    if reject:
        st.error(f"KẾT LUẬN: BÁC BỎ H0 (p-value = {p_val:.4f})")
        st.write(f"Vì giá trị quan sát nằm trong miền bác bỏ (giá trị tới hạn: {crit:.4f})")
    else:
        st.success(f"KẾT LUẬN: CHƯA ĐỦ CƠ SỞ BÁC BỎ H0 (p-value = {p_val:.4f})")
        st.write(f"Vì giá trị quan sát không nằm trong miền bác bỏ.")

    # --- PHẦN 4: SO SÁNH 2 TỔNG THỂ ---
    st.divider()
    st.subheader("Phần 3. So sánh hai tổng thể")
    with st.expander("🔗 So sánh hai Tỉ lệ ($p_1$ và $p_2$)"):
        st.write("Giả thuyết $H_0: p_1 = p_2$.")
        st.write("Sử dụng tỉ lệ chung $\\overline{f} = \\frac{n_1f_1 + n_2f_2}{n_1 + n_2}$")
        st.latex(
            r"Z = \frac{f_1 - f_2}{\sqrt{\overline{f}(1-\overline{f})(\frac{1}{n_1} + \frac{1}{n_2})}} \sim N(0,1)")

    st.markdown("---")

    # --- PHẦN 1: KIỂM ĐỊNH DÙNG MỘT MẪU ---
    st.subheader("1. Các kiểm định dùng một mẫu (One-Sample Tests)")
    st.write("Dùng để so sánh tham số của một tổng thể (kỳ vọng, tỉ lệ) với một giá trị giả thuyết cho trước.")

    with st.expander("🔍 Kiểm định trung bình tổng thể (So sánh μ với μ0)"):
        st.markdown("""
        Áp dụng khi cần kiểm tra xem giá trị trung bình thực tế có đúng như công bố hay không (Ví dụ: Trọng lượng sản phẩm, năng suất giống cây trồng).
        """)
        st.latex(r"G_{qs} = \frac{\overline{x} - \mu_0}{s_{hc}} \sqrt{n}")
        st.write("- Nếu $n \\geq 30$: Tra bảng phân phối chuẩn $U_{\\alpha}$.")
        st.write("- Nếu $n < 30$: Tra bảng phân phối Student $t(n-1)$.")

    with st.expander("📊 Kiểm định tỉ lệ tổng thể (So sánh p với p0)"):
        st.markdown("""
        Áp dụng khi cần kiểm tra tỉ lệ phế phẩm, tỉ lệ khách hàng hài lòng.
        """)
        st.latex(r"U_{qs} = \frac{f - p_0}{\sqrt{p_0(1-p_0)}} \sqrt{n}")
        st.info("💡 Điều kiện: $n$ đủ lớn ($np_0 > 5$ và $n(1-p_0) > 5$).")

    # --- PHẦN 2: KIỂM ĐỊNH DÙNG NHIỀU MẪU ---
    st.divider()
    st.subheader("2. Các kiểm định dùng nhiều mẫu (Multi-Sample Tests)")
    st.write("Dùng để so sánh các tham số giữa hai hoặc nhiều nhóm độc lập với nhau.")

    with st.expander("⚖️ So sánh hai trung bình (μ1 và μ2)"):
        st.write("Dùng để xem hai phương pháp sản xuất, hai loại giống cây trồng có cho năng suất khác nhau hay không.")
        st.latex(r"U_{qs} = \frac{\overline{x}_1 - \overline{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}")
        st.write("- Thường dùng khi mẫu lớn hoặc đã biết phương sai.")

    with st.expander("🔗 So sánh hai tỉ lệ (p1 và p2)"):
        st.write("Dùng để so sánh tỉ lệ thành công của hai chiến dịch marketing hoặc hai nhóm thử nghiệm lâm sàng.")
        st.latex(r"U_{qs} = \frac{f_1 - f_2}{\sqrt{\bar{f}(1-\bar{f})(\frac{1}{n_1} + \frac{1}{n_2})}}")
        st.caption("Trong đó $\\bar{f}$ là tỉ lệ chung của cả hai mẫu.")

    # --- PHẦN 3: CÔNG CỤ THỰC HÀNH KIỂM ĐỊNH ---
    st.divider()
    st.subheader("🛠️ Thực hành: Kiểm định trung bình Một mẫu")
    st.write("Giả sử bạn cần kiểm tra trọng lượng trung bình của một lô hàng.")

    col1, col2 = st.columns(2)
    with col1:
        mu_0 = st.number_input("Giá trị giả thuyết (μ0)", value=500.0)
        alpha = st.selectbox("Mức ý nghĩa (α)", [0.01, 0.05, 0.10], index=1)

    with col2:
        x_bar = st.number_input("Trung bình mẫu quan sát", value=495.0)
        s_hc = st.number_input("Độ lệch chuẩn hiệu chỉnh (s_hc)", value=10.0)
        n = st.number_input("Kích thước mẫu", value=40)

    if st.button("Tiến hành Kiểm định"):
        # Tính giá trị quan sát
        u_qs = ((x_bar - mu_0) / s_hc) * np.sqrt(n)

        # Tra giá trị tới hạn (Kiểm định 2 phía)
        u_alpha = stats.norm.ppf(1 - alpha / 2)

        st.write(f"**Kết quả:**")
        st.write(f"- Giá trị quan sát $U_{{qs}}$: `{u_qs:.4f}`")
        st.write(f"- Miền bác bỏ: $|U_{{qs}}| > {u_alpha:.4f}$")

        if abs(u_qs) > u_alpha:
            st.error("KẾT LUẬN: Bác bỏ giả thuyết H0. Có sự khác biệt có ý nghĩa thống kê.")
        else:
            st.success("KẾT LUẬN: Chưa đủ bằng chứng để bác bỏ H0. Sự khác biệt có thể do ngẫu nhiên.")

    # --- TỔNG KẾT KHÓA HỌC ---
    st.sidebar.success("🎉 Chúc mừng bạn đã hoàn thành 10 bài học!")
    st.sidebar.info("""
    **Lưu ý cuối cùng:** 
    Kiểm định giả thuyết giúp chúng ta quản lý rủi ro khi đưa ra quyết định dựa trên dữ liệu mẫu. Hãy luôn xem xét cả ý nghĩa thực tế bên cạnh ý nghĩa thống kê!
    """)