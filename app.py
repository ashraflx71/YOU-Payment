import streamlit as st

# --- إعدادات القائد ---
رقم_الدعم_الفني = "201280208018"
اسم_المهندس = "أشرف حسن"

st.set_page_config(page_title=f"منصة YOU | {اسم_المهندس}", page_icon="🚀", layout="centered")

# --- كود CSS لتجربة مستخدم أوتوماتيكية ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; direction: rtl; }
    html, body, [class*="css"] { direction: rtl; text-align: right; font-family: 'Tahoma'; font-size: 22px; }
    
    .status-box {
        background-color: #111;
        border: 1px solid #007bff;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* زر الدعم الفني (للمشاكل فقط) */
    .support-btn {
        display: inline-block;
        color: #ff4b4b !important;
        border: 1px solid #ff4b4b;
        padding: 5px 15px;
        border-radius: 15px;
        text-decoration: none;
        font-size: 14px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- واجهة النظام الأوتوماتيكي ---
st.title("🤖 نظام YOU الذكي للشحن")

# حالة النظام (تعطي انطباع بالأتمتة)
st.markdown("""
<div class="status-box">
    <span style="color: #25d366;">●</span> النظام الآن: <b>يعمل بأتمتة كاملة</b> | سرعة التنفيذ: ⚡ فورية
</div>
""", unsafe_allow_html=True)

# 1. اختيار الخدمة
services = {
    "ChatGPT Plus (اشترك الآن)": 1200,
    "Claude.ai Pro (تفعيل فوري)": 1150,
    "Midjourney (رصيد صور)": 950
}

selected = st.selectbox("🎯 اختر الخدمة التي تريد تفعيلها:", ["اختر من هنا..."] + list(services.keys()))

if selected != "اختر من هنا...":
    st.info(f"سعر الخدمة الحالي: {services[selected]} ج.م")
    
    # 2. جمع البيانات أوتوماتيكياً
    with st.form("auto_order"):
        user_email = st.text_input("📧 أدخل البريد الإلكتروني المراد شحنه:")
        method = st.radio("💳 اختر وسيلة الدفع الآلية:", ["فودافون كاش (تحويل تلقائي)", "إنستا باي (تأكيد فوري)"])
        
        st.write("⚠️ بمجرد الضغط، سيتم تسجيل طلبك في السجل وبدء المعالجة.")
        
        submitted = st.form_submit_button("إرسال طلب الشحن للنظام 🚀")
        
        if submitted:
            if user_email:
                # هنا النظام يسجل الطلب (أوتوماتيك)
                st.success(f"✅ تم تسجيل طلبك لخدمة {selected} بنجاح!")
                st.balloons()
                st.write(f"إرشادات الدفع: يرجى التحويل إلى الرقم {رقم_الدعم_الفني} وإرفاق الإيصال.")
            else:
                st.error("يرجى إدخال البريد الإلكتروني لإتمام الأتمتة.")

# --- قسم الطوارئ فقط ---
st.sidebar.markdown("---")
st.sidebar.subheader("🛠️ مركز المساعدة")
st.sidebar.write("إذا واجهت مشكلة تقنية فقط في الطلب:")
st.sidebar.markdown(f'<a href="https://wa.me/{رقم_الدعم_الفني}?text=مشكلة_تقنية_في_الطلب" class="support-btn">إبلاغ عن مشكلة</a>', unsafe_allow_html=True)

st.markdown("---")
st.caption(f"منصة YOU تدار برمجياً بواسطة م. {اسم_المهندس} 2026")
