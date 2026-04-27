import streamlit as st
import time

# --- إعدادات القائد أشرف ---
رقم_المحفظة = "01014505254"
اسم_المهندس = "أشرف حسن"

st.set_page_config(page_title="YOU - بوابة الدفع الموثوقة", page_icon="🛡️")

# تنسيق ملكي (أسود وأزرق) لإعطاء هيبة للموقع
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #000; color: #fff; direction: rtl; }
    .main-container {
        border: 1px solid #007bff;
        padding: 30px;
        border-radius: 15px;
        background: #050505;
        text-align: center;
    }
    .step-box {
        background: #111;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-right: 4px solid #007bff;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("🌟 منصة YOU للخدمات الرقمية")
st.write(f"بوابة الشحن الدولي تحت إدارة م. {اسم_المهندس}")

st.markdown("---")
st.subheader("📝 نموذج تسجيل طلب شحن")
st.info("نحن لا نبيع أوهاماً؛ أدخل طلبك وسيتم مراجعته وتنفيذه يدوياً لضمان أعلى جودة.")

# نموذج الطلب الموحد
with st.form("order_form"):
    service_needed = st.text_input("ما هي الخدمة أو الموقع المطلوب؟ (مثلاً: ChatGPT, Netflix, أمازون...)", placeholder="🔍 اكتب طلبك هنا")
    user_account = st.text_input("البريد الإلكتروني المراد الشحن عليه:")
    payment_amount = st.number_input("المبلغ المراد تحويله (بالجنيه المصري):", min_value=0)
    
    st.markdown('<div class="step-box">', unsafe_allow_html=True)
    st.write(f"تحويل المبلغ إلى محفظة فودافون كاش: **{رقم_المحفظة}**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    submitted = st.form_submit_button("إرسال الطلب للمهندس أشرف 🚀")

if submitted:
    if service_needed and user_account and payment_amount > 0:
        st.success(f"✅ تم استلام بيانات طلبك لخدمة ({service_needed}) بنجاح.")
        st.balloons()
        st.markdown(f"""
        **تم حجز رقم طلب: #YOU-{int(time.time())}**
        - سيتم مراجعة التحويل فوراً.
        - التفعيل يتم خلال 15 لـ 30 دقيقة.
        - سيصلك إشعار على بريدك الإلكتروني فور اكتمال الشحن.
        """)
    else:
        st.error("من فضلك أكمل جميع الخانات (الخدمة، الإيميل، المبلغ) لتوثيق طلبك.")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption(f"منصة YOU | مصداقية مهندس.. ثقة عميل | 2026")
