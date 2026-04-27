import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="YOU Payment | م. أشرف حسن", page_icon="🌟", layout="centered")

# كود CSS المخصص للواجهة الملكية العربية
st.markdown("""
    <style>
    /* توجيه الصفحة للعربية وتغيير الخلفية للأسود */
    .stApp {
        background-color: #000000;
        color: #ffffff;
        direction: rtl;
    }
    
    /* تنسيق النصوص وحجم الخط الملكي */
    html, body, [class*="css"]  {
        direction: rtl;
        text-align: right;
        font-family: 'Tahoma', Geneva, sans-serif;
        font-size: 22px;
    }

    /* تصميم البطاقة الملكية المضيئة */
    .royal-card {
        background: #0a0a0a;
        border-right: 6px solid #007bff;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0, 123, 255, 0.2);
        border: 1px solid #1a1a1a;
    }

    /* أزرار النيون التفاعلية */
    .stButton>button {
        width: 100%;
        background-color: transparent;
        color: #007bff;
        border: 2px solid #007bff;
        border-radius: 30px;
        padding: 12px 20px;
        font-weight: bold;
        font-size: 20px;
        transition: 0.4s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #007bff;
        color: white;
        box-shadow: 0 0 25px #007bff;
        transform: scale(1.02);
    }

    /* العناوين الزرقاء الفخمة */
    h1, h2, h3 {
        color: #007bff !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# محتوى المنصة بالعربي
st.title("🌟 منصة YOU للخدمات الرقمية")

# رسالة الترحيب الشخصية
st.markdown(f"""
<div class="royal-card">
    <h3>مرحباً بك يا هندسة 🛠️</h3>
    <p>نظام <b>YOU</b> هو بوابتك الذكية لشحن الحسابات الدولية وشراء خدمات الذكاء الاصطناعي (AI) بالعملة المحلية بكل سهولة وأمان.</p>
</div>
""", unsafe_allow_html=True)

st.header("🤖 أدوات الذكاء الاصطناعي")

# توزيع الخدمات (مناسب جداً لعرض الموبايل)
col1, col2 = st.columns(2)

with col1:
    if st.button("ChatGPT Plus ⚡"):
        st.info("جاري تجهيز طلب شحن ChatGPT Plus...")

with col2:
    if st.button("Midjourney 🎨"):
        st.info("جاري تحويلك لخدمات التصميم الذكي...")

with col1:
    if st.button("Claude.ai 🧠"):
        st.info("بدء تفعيل خدمة Claude Pro...")

with col2:
    if st.button("خدمات أخرى 🌐"):
        st.info("استعرض باقي الخدمات المتاحة...")

# الفوتر (التوقيع الخاص بك)
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <p style='font-size: 16px; color: #888;'>تم التطوير بواسطة</p>
    <h4 style='color: #007bff; margin-top: -10px;'>المهندس أشرف حسن</h4>
    <p style='font-size: 14px;'>رؤية تقنية مستدامة 2026 🚀</p>
</div>
""", unsafe_allow_html=True)
