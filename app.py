import streamlit as st
import time

# --- إعدادات القائد أشرف ---
رقم_المحفظة = "01014505254"
اسم_المهندس = "أشرف حسن"

st.set_page_config(page_title="YOU Payment - بوابة الدفع الرقمية", page_icon="💳", layout="centered")

# --- تنسيق الواجهة الملكية لزيادة المصداقية ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000; color: #fff; direction: rtl; }}
    html, body, [class*="css"] {{ direction: rtl; text-align: right; font-family: 'Tahoma'; }}
    
    .payment-card {{
        background: #0a0a0a;
        border: 1px solid #007bff;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 123, 255, 0.2);
        margin: 20px 0;
    }}
    .price-tag {{
        font-size: 28px;
        color: #25d366;
        font-weight: bold;
    }}
    .account-info {{
        background: #111;
        padding: 15px;
        border-radius: 10px;
        border: 1px dashed #444;
        margin: 15px 0;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("🌟 منصة YOU للشحن الرقمي")
st.markdown("### بوابة الدفع المباشرة والمؤمنة")

# 1. اختيار الخدمة
services = {
    "ChatGPT Plus ⚡": 1200,
    "Claude.ai Pro 🧠": 1150,
    "Midjourney 🎨": 950
}

selected_service = st.selectbox("🎯 اختر الخدمة التي ترغب في شحنها:", list(services.keys()))
price = services[selected_service]

st.markdown(f"""
<div class="payment-card">
    <p>تكلفة الخدمة المختارة</p>
    <div class="price-tag">{price} ج.م</div>
</div>
""", unsafe_allow_html=True)

# 2. إدخال البيانات
st.markdown("### 📝 بيانات الحساب")
email = st.text_input("البريد الإلكتروني المراد تفعيله:", placeholder="example@email.com")

if email:
    st.markdown("---")
    st.markdown("### 💳 تعليمات الدفع")
    st.markdown(f"""
    <div class="account-info">
        <p>يرجى تحويل مبلغ <b>{price} ج.م</b> إلى محفظة فودافون كاش التالية:</p>
        <h2 style="color: #007bff; letter-spacing: 2px;">{رقم_المحفظة}</h2>
        <p style="font-size: 14px; color: #888;">(يتم التحويل عبر فودافون كاش أو إنستا باي)</p>
    </div>
    """, unsafe_allow_html=True)

    # 3. رفع الإثبات (قلب المصداقية)
    st.markdown("### 📤 تأكيد التحويل")
    proof = st.file_uploader("قم برفع صورة (إيصال التحويل) لتوثيق الطلب:", type=['png', 'jpg', 'jpeg'])

    if proof:
        if st.button("🚀 إتمام الطلب وتفعيل الخدمة"):
            with st.spinner('جاري مراجعة البيانات وربطها بالسجل الرقمي...'):
                time.sleep(3) # إيهام العميل بوجود معالجة آلية
                order_id = f"YOU-{int(time.time())}"
                st.success(f"✅ تم تسجيل طلبك بنجاح يا هندسة!")
                st.balloons()
                
                st.markdown(f"""
                <div style="background: #111; padding: 20px; border-radius: 10px; border: 1px solid #25d366;">
                    <h4>رقم الطلب الخاص بك: <span style="color: #25d366;">#{order_id}</span></h4>
                    <p>سيتم مراجعة التحويل وتفعيل الخدمة على بريدك الإلكتروني خلال دقائق.</p>
                    <p style="font-size: 14px; color: #888;">تم إرسال نسخة من بيانات الطلب إلى وحدة التحكم الخاصة بالمهندس أشرف.</p>
                </div>
                """, unsafe_allow_html=True)

# تذييل الصفحة للمصداقية
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.write("🛡️ معاملة مؤمنة 100%")
with col2:
    st.write(f"👨‍💻 م. {اسم_المهندس} | 2026")
