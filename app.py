import streamlit as st

# --- إعدادات القائد ---
رقم_الواتساب = "201280208018"
اسم_المهندس = "أشرف حسن"

st.set_page_config(page_title=f"منصة YOU | {اسم_المهندس}", page_icon="🌟", layout="centered")

# --- كود CSS الملكي المطور ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; direction: rtl; }
    html, body, [class*="css"] { direction: rtl; text-align: right; font-family: 'Tahoma'; font-size: 22px; }
    .royal-card {
        background: #0a0a0a;
        border-right: 6px solid #007bff;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        border: 1px solid #1a1a1a;
    }
    .stButton>button {
        width: 100%;
        background-color: #007bff;
        color: white;
        border-radius: 25px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- واجهة المستخدم ---
st.title("🌟 منصة YOU - بوابة الشحن المباشر")

st.markdown(f"""
<div class="royal-card">
    <h3>مرحباً بك يا هندسة 🛠️</h3>
    <p>اختر الخدمة، أدخل بياناتك، وسيتم تنفيذ طلبك فوراً.</p>
</div>
""", unsafe_allow_html=True)

# قائمة الخدمات
services = {
    "ChatGPT Plus ⚡": 1200, # مثال للسعر
    "Claude.ai Pro 🧠": 1150,
    "Midjourney 🎨": 950,
    "خدمة مخصصة 🌐": 0
}

selected_service = st.selectbox("ما هي الخدمة التي تريد شحنها؟", list(services.keys()))

if selected_service:
    st.markdown("---")
    st.subheader(f"📝 طلب شحن: {selected_service}")
    
    with st.form("order_form"):
        email = st.text_input("الإيميل المراد شحنه (أو الحساب)")
        payment_method = st.radio("اختر وسيلة الدفع:", ["فودافون كاش", "إنستا باي (InstaPay)", "أخرى"])
        notes = st.text_area("ملاحظات إضافية")
        
        submit = st.form_submit_button("إتمام الطلب وإرسال التفاصيل")
        
        if submit:
            if email:
                # تجهيز رسالة احترافية تتبعت للمهندس أشرف
                order_msg = f"طلب جديد من منصة YOU%0A" \
                            f"----------------------%0A" \
                            f"الخدمة: {selected_service}%0A" \
                            f"الإيميل: {email}%0A" \
                            f"وسيلة الدفع: {payment_method}%0A" \
                            f"ملاحظات: {notes}"
                
                wa_url = f"https://wa.me/{رقم_الواتساب}?text={order_msg}"
                
                st.success("✅ تم تجهيز بيانات الطلب بنجاح!")
                st.markdown(f'''
                    <a href="{wa_url}" target="_blank" style="text-decoration: none;">
                        <div style="background-color: #25d366; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold;">
                            اضغط هنا لتأكيد الدفع مع المهندس أشرف عبر الواتساب
                        </div>
                    </a>
                ''', unsafe_allow_html=True)
            else:
                st.error("من فضلك أدخل الإيميل المطلوب شحنه.")

st.markdown("---")
st.caption(f"تطوير المهندس {اسم_المهندس} | 2026")
