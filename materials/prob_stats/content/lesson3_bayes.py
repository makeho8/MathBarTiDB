import streamlit as st
import math


def run():
    st.header("Bài 3: Công thức Bayes và Thử nghiệm Bernoulli")
    st.markdown("---")

    # --- PHẦN 1: CÔNG THỨC XÁC SUẤT ĐẦY ĐỦ ---
    st.subheader("1. Hệ đầy đủ và Công thức xác suất đầy đủ")

    with st.expander("📖 Lý thuyết về Hệ đầy đủ"):
        st.write("Các biến cố $H_1, H_2, \\dots, H_n$ được gọi là một **hệ đầy đủ** nếu:")
        st.markdown("""
        1. Các biến cố xung khắc từng đôi: $H_i \\cap H_j = \\varnothing$ với $i \\neq j$.
        2. Tổng các biến cố bao trùm không gian mẫu: $\\sum_{i=1}^n H_i = \\Omega$.
        3. Xác suất mỗi biến cố dương: $P(H_i) > 0$.
        """)

    with st.expander("📐 Công thức xác suất đầy đủ"):
        st.write("Nếu có hệ đầy đủ $\\{H_i\\}$, xác suất của một biến cố $A$ bất kỳ được tính bằng:")
        st.latex(r"P(A) = \sum_{i=1}^{n} P(H_i) \cdot P(A|H_i)")
        st.info(
            "💡 **Ý nghĩa:** Dùng để tính xác suất của một biến cố khi nó có thể xảy ra trong nhiều tình huống (nhóm) khác nhau.")

    # Ví dụ chi tiết 1
    st.markdown("#### 🔍 Ví dụ 1: Sản xuất tại phân xưởng")
    st.write("""
    Một nhà máy có 3 máy cùng sản xuất một loại linh kiện. 
    - Máy 1 sản xuất 50% sản phẩm, tỉ lệ phế phẩm là 2%.
    - Máy 2 sản xuất 30% sản phẩm, tỉ lệ phế phẩm là 3%.
    - Máy 3 sản xuất 20% sản phẩm, tỉ lệ phế phẩm là 5%.

    **Câu hỏi:** Lấy ngẫu nhiên 1 sản phẩm, tính xác suất sản phẩm đó là phế phẩm?
    """)
    if st.checkbox("Xem lời giải Ví dụ 1"):
        st.write("""
        - Gọi $H_i$ là biến cố sản phẩm do máy $i$ sản xuất. $\\{H_1, H_2, H_3\\}$ là hệ đầy đủ.
        - $P(H_1)=0.5; P(H_2)=0.3; P(H_3)=0.2$.
        - Gọi $A$ là biến cố lấy được phế phẩm. 
        - $P(A|H_1)=0.02; P(A|H_2)=0.03; P(A|H_3)=0.05$.
        """)
        pa = (0.5 * 0.02) + (0.3 * 0.03) + (0.2 * 0.05)
        st.success(f"Kết quả: $P(A) = 0.01 + 0.009 + 0.01 = {pa:.3f}$")

    # --- PHẦN 2: CÔNG THỨC BAYES ---
    st.divider()
    st.subheader("2. Công thức Bayes (Xác suất hậu nghiệm)")

    st.write("""
    Công thức Bayes dùng để "cập nhật" niềm tin. Sau khi biết biến cố $A$ đã xảy ra, ta muốn biết khả năng $A$ rơi vào nhóm $H_k$ nào nhất.
    """)
    st.latex(r"P(H_k|A) = \frac{P(H_k) \cdot P(A|H_k)}{P(A)}")

    st.markdown("#### 🔍 Ví dụ 2: Hồi tưởng nguồn gốc (Tiếp tục ví dụ 1)")
    st.write("**Câu hỏi:** Biết sản phẩm lấy ra là phế phẩm. Khả năng cao nhất là do máy nào sản xuất?")
    if st.checkbox("Xem lời giải Ví dụ 2"):
        st.write("- Áp dụng Bayes cho máy 3: $P(H_3|A) = (0.2 \\times 0.05) / 0.029 \\approx 0.345$.")
        st.write("- Áp dụng Bayes cho máy 1: $P(H_1|A) = (0.5 \\times 0.02) / 0.029 \\approx 0.344$.")
        st.info(
            "Mặc dù máy 1 sản xuất nhiều nhất, nhưng máy 3 có tỉ lệ lỗi cao nên xác suất gây ra lỗi là tương đương nhau.")

    # --- PHẦN 3: CÔNG THỨC BERNOULLI ---
    st.divider()
    st.subheader("3. Công thức Bernoulli")

    with st.expander("🎯 Thử nghiệm Bernoulli"):
        st.write("""
        Một phép thử được gọi là thử nghiệm Bernoulli nếu:
        - Chỉ có hai kết quả: **Thành công (S)** với xác suất $p$ và **Thất bại (F)** với xác suất $q = 1-p$.
        - Các phép thử độc lập với nhau.
        """)
        st.latex(r"P_n(k) = C_n^k \cdot p^k \cdot q^{n-k}")
        st.write("Trong đó: $n$ là tổng số phép thử, $k$ là số lần thành công.")

    st.markdown("#### 🔍 Ví dụ 3: Xạ thủ bắn súng")
    st.write(
        "Một xạ thủ bắn 5 viên đạn vào bia. Xác suất trúng mỗi lần là 0.8. Tính xác suất để xạ thủ trúng đúng 3 viên?")
    if st.checkbox("Xem lời giải Ví dụ 3"):
        n, k, p = 5, 3, 0.8
        res = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
        st.latex(r"P_5(3) = C_5^3 \cdot 0.8^3 \cdot 0.2^2")
        st.success(f"Kết quả: {res:.4f}")

    # --- PHẦN 4: NGUYÊN LÝ XÁC SUẤT NHỎ ---
    st.divider()
    st.subheader("4. Liên hệ thực tế: Nguyên lý xác suất nhỏ")
    st.write("""
    Trong các thử nghiệm lặp lại (Bernoulli), nếu xác suất $p$ cực kỳ nhỏ, theo **nguyên lý xác suất nhỏ**, 
    biến cố đó được coi là không xảy ra trong một vài lần thử đầu tiên. 
    """)
    st.warning(
        "Ghi chú: Nếu một biến cố có xác suất rất nhỏ thì trong một phép thử biến cố đó coi như không xảy ra.")

    # --- CÔNG CỤ TÍNH TOÁN ---
    st.sidebar.subheader("🛠️ Máy tính Bernoulli")
    n_in = st.sidebar.number_input("Số phép thử (n)", 1, 100, 10)
    k_in = st.sidebar.number_input("Số lần thành công (k)", 0, n_in, 3)
    p_in = st.sidebar.slider("Xác suất thành công (p)", 0.0, 1.0, 0.5)

    if st.sidebar.button("Tính P_n(k)"):
        prob = math.comb(n_in, k_in) * (p_in ** k_in) * ((1 - p_in) ** (n_in - k_in))
        st.sidebar.code(f"P({k_in}) = {prob:.6f}")