import streamlit as st

# إعدادات الصفحة لتناسب شاشة الموبايل
st.set_page_config(
    page_title="YOU Payment",
    page_icon="⚡",
    layout="centered"
)

# تخصيص التصميم المطور (Enhanced UI)
st.markdown("""
    <style>
    /* تنسيق الخلفية العامة */
    .stApp {
        background-color: #050505;
        color: #FFFFFF;
    }

    /* كارت الواجهة الرئيسي */
    .main-card {
        background: linear-gradient(145deg, #0a0a0a, #111111);
        border: 1px solid #0056b3;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 123, 255, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }

    /* العناوين الكبيرة 22px */
    .title-text {
        font-size: 28px;
        font-weight: 800;
        color: #007bff;
        margin-bottom: 10px;
    }

    .sub-text {
        font-size: 20px;
        color: #b0b0b0;
        margin-bottom: 30px;
    }

    /* تخصيص الأزرار */
    .stButton>button {
        background: linear-gradient(90deg, #007bff, #00c6ff);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
    }

    .stButton>button:hover {
        box-shadow: 0 0 20px rgba(0, 123, 255, 0.4);
        transform: translateY(-2px);
    }

    /* تحسين شكل الحقول */
    input {
        background-color: #121212 !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
    
    /* إخفاء القائمة العلوية لـ Streamlit لمظهر أكثر احترافية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def main():
    # الهيدر
    st.markdown("""
        <div class="main-card">
            <div class="title-text">YOU Payment</div>
            <div class="sub-text">بوابتك الرقمية للخدمات العالمية</div>
        </div>
    """, unsafe_allow_html=True)

    # محتوى التطبيق
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div style='text-align: right; font-size: 20px;'>نوع الخدمة</div>", unsafe_allow_html=True)
        service = st.selectbox("", ["Google Play", "Amazon", "Netflix", "ChatGPT Plus"], label_visibility="collapsed")

    with col2:
        st.markdown("<div style='text-align: right; font-size: 20px;'>القيمة ($)</div>", unsafe_allow_html=True)
        amount = st.number_input("", min_value=5, step=5, label_visibility="collapsed")

    st.markdown("---")

    # حساب السعر
    rate = 50.50  # تحديث يدوي للسعر أو ربطه بـ API
    total = amount * rate

    st.markdown(f"""
        <div style="background: rgba(0, 123, 255, 0.05); padding: 20px; border-radius: 15px; border-right: 5px solid #007bff;">
            <p style="text-align: right; font-size: 18px; color: #888;">الإجمالي المطلوب بالجنيه</p>
            <h1 style="text-align: right; color: #007bff; margin: 0;">{total:,.2f} EGP</h1>
        </div>
    """, unsafe_allow_html=True)

    st.write(" ")
    
    if st.button("تأكيد وطلب الآن"):
        st.balloons()
        st.info("جاري تجهيز طلبك وتوجيهك لإنهاء الدفع...")

if __name__ == "__main__":
    main()
