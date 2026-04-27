import streamlit as st
import time

# --- إعدادات القائد أشرف (المحرك السريع) ---
رقم_المحفظة = "01014505254"
اسم_المهندس = "أشرف حسن"

st.set_page_config(page_title="YOU - شحن فوري", page_icon="⚡", layout="centered")

# CSS فائق الخفة لضمان سرعة التحميل على الموبايل
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000; color: #fff; direction: rtl; }}
    .fast-card {{
        background: #111;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #007bff;
        margin-bottom: 10px;
    }}
    .pay-btn {{
        background-color: #25d366 !important;
        color: white !important;
        font-weight: bold;
        width: 100%;
        border-radius: 25px;
        padding: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ منصة YOU: طلب فوري")

# 1. محرك البحث (الطلب السريع)
query = st.text_input("🔍 ابحث عن خدمتك (ChatGPT, Netflix, هدايا...):", placeholder="اكتب هنا...")

if query:
    st.markdown(f'<div class="fast-card">📦 أنت تطلب الآن: <b>{query}</b></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("📧 الإيميل المستهدف:")
    with col2:
        amount = st.number_input("💰 المبلغ (ج.م):", min_value=0)

    if email and amount > 0:
        st.markdown(f"""
        <div class="fast-card" style="border-color: #25d366; text-align: center;">
            <p>حول <b>{amount} ج.م</b> فودافون كاش إلى:</p>
            <h2 style="color: #25d366; margin: 0;">{رقم_المحفظة}</h2>
        </div>
        """, unsafe_allow_html=True)

        # رفع الإيصال (الخطوة الأخيرة)
        proof = st.file_uploader("📸 ارفع إيصال التحويل (فوري):", type=['png', 'jpg', 'jpeg'])

        if proof:
            if st.button("🚀 تنفيذ الطلب الآن"):
                with st.spinner('جاري التأكيد...'):
                    # أتمتة العملية: إظهار رقم الطلب فوراً
                    order_id = f"YOU-{int(time.time())}"
                    st.success(f"✅ تم الاستلام! رقم طلبك: #{order_id}")
                    st.balloons()
                    st.info("المهندس أشرف بدأ في تنفيذ طلبك حالاً.")
else:
    st.markdown("""
    <div style="text-align: center; color: #888; padding: 20px;">
        💡 اكتب أي خدمة أو اختر من المقترحات لبدء الشحن فوراً
    </div>
    """, unsafe_allow_html=True)
    
    # أزرار وصول سريع (لمسة واحدة)
    st.write("🚀 وصول سريع:")
    c1, c2, c3 = st.columns(3)
    if c1.button("ChatGPT"): st.rerun()
    if c2.button("Netflix"): st.rerun()
    if c3.button("PUBG"): st.rerun()

st.markdown("---")
st.caption(f"تفعيل فوري | إدارة م. {اسم_المهندس} 2026")
