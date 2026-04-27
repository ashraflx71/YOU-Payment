import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="YOU Payment", page_icon="🌟", layout="centered")

# كود CSS المخصص للواجهة الملكية
st.markdown("""
    <style>
    /* تغيير الخلفية للأسود العميق */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* تنسيق النصوص العربية وحجم الخط */
    html, body, [class*="css"]  {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 22px;
    }

    /* تصميم البطاقات الملكية */
    .royal-card {
        background: #0a0a0a;
        border-left: 5px solid #007bff;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 123, 255, 0.2);
    }

    /* تنسيق الأزرار بنمط النيون الأزرق */
    .stButton>button {
        width: 100%;
        background-color: transparent;
        color: #007bff;
        border: 2px solid #007bff;
        border-radius: 25px;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #007bff;
        color: white;
        box-shadow: 0 0 20px #007bff;
    }

    /* العناوين الزرقاء */
    h1, h2, h3 {
        color: #007bff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# محتوى المنصة
st.title("🌟 منصة YOU للخدمات الرقمية")

st.markdown(f"""
<div class="royal-card">
    <h3>مرحباً بك يا هندسة</h3>
    <p>نظام <b>YOU</b> يوفر لك أسهل طريقة لشحن الحسابات الدولية وشراء خدمات الذكاء الاصطناعي بالعملة المحلية.</p>
</div>
""", unsafe_allow_html=True)

st.header("🤖 أدوات الـ AI المتاحة")

# توزيع الخدمات في أعمدة للموبايل
col1, col2 = st.columns(2)

with col1:
    if st.button("ChatGPT Plus"):
        st.info("جاري تحويلك لخدمة شحن ChatGPT...")

with col2:
    if st.button("Midjourney"):
        st.info("جاري تحويلك لخدمة شحن Midjourney...")

with col1:
    if st.button("Claude.ai"):
        st.info("جاري تحويلك لخدمة شحن Claude...")

with col2:
    if st.button("خدمات أخرى"):
        st.info("استكشف باقي الخدمات...")

# تذييل الصفحة
st.markdown("---")
st.caption("تم التطوير بواسطة م. أشرف حسن | رؤية 2026 🚀")
