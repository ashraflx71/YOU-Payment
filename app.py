import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="YOU - بوابة الدفع الذكية",
    page_icon="💳",
    layout="centered"
)

# تخصيص المظهر (CSS) ليتناسب مع ذوقك الملكي (أسود، أزرق، أبيض)
st.markdown("""
    <style>
    /* الخلفية العامة والتكست */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* العناوين */
    h1, h2, h3 {
        color: #007bff !important;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }

    /* النصوص الكبيرة */
    .big-font {
        font-size: 22px !important;
        font-weight: bold;
        color: #ffffff;
        text-align: right;
        direction: rtl;
    }

    /* تخصيص الحقول والأزرار */
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 10px;
        width: 100%;
        height: 50px;
        font-size: 18px;
    }

    div[data-baseweb="input"] {
        background-color: #1a1a1a;
        color: white;
        border: 1px solid #007bff;
    }
    
    /* محاذاة العناصر لليمين (عربي) */
    .rtl {
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

# واجهة التطبيق
def main():
    st.markdown("<h1>YOU Payment Gateway</h1>", unsafe_allow_html=True)
    st.markdown("<p class='big-font' style='text-align:center;'>بوابتك الآمنة للمشتريات الدولية بالعملة المحلية</p>", unsafe_allow_html=True)
    
    st.divider()

    # خيارات الخدمة
    st.markdown("<div class='rtl'>اختر الخدمة المطلوبة:</div>", unsafe_allow_html=True)
    option = st.selectbox("", ["شحن رصيد Google Play", "شراء من Amazon Global", "اشتراكات AI الرقمية"])

    # مدخلات المستخدم
    st.markdown("<div class='rtl'>المبلغ المطلوب (بالدولار):</div>", unsafe_allow_html=True)
    amount_usd = st.number_input("", min_value=1.0, step=1.0)
    
    # حساب تقريبي (مثال)
    exchange_rate = 50.0 # سعر الصرف الافتراضي
    total_egp = amount_usd * exchange_rate

    st.markdown(f"""
        <div class='rtl' style='background-color: #1a1a1a; padding: 20px; border-radius: 10px; border-left: 5px solid #007bff;'>
            <p class='big-font'>الإجمالي بالجنيه المصري:</p>
            <h2 style='color: #ffffff;'>{total_egp:,.2f} ج.م</h2>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    
    if st.button("إتمام عملية الدفع"):
        st.success("جاري تحويلك لبوابة الدفع المحلية...")

if __name__ == "__main__":
    main()
