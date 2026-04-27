import streamlit as st
import time

# --- إعدادات القائد أشرف ---
رقم_المحفظة = "01014505254"
اسم_المهندس = "أشرف حسن"

st.set_page_config(page_title="YOU Payment - بوابة الشحن الشاملة", page_icon="🌍", layout="centered")

# --- التنسيق الملكي المفتوح ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000; color: #fff; direction: rtl; }}
    html, body, [class*="css"] {{ direction: rtl; text-align: right; font-family: 'Tahoma'; }}
    
    .status-badge {{
        background: #111;
        border: 1px solid #007bff;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        color: #007bff;
    }}
    .payment-box {{
        background: #0a0a0a;
        border: 1px solid #25d366;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 منصة YOU للشحن الدولي المفتوح")
st.markdown('<div class="status-badge">نظام دفع حر لجميع المواقع والبرامج والألعاب أونلاين</div>', unsafe_allow_html=True)

# 1. اختيار الخدمة (حرية الاختيار)
st.markdown("### 🛠️ ماذا تريد أن تشحن اليوم؟")
category = st.radio("اختر نوع الخدمة:", ["خدمات AI جاهزة", "برامج وألعاب", "اشتراكات مواقع أخرى (طلب خاص)"])

selected_service = ""
price = 0

if category == "خدمات AI جاهزة":
    options = {"ChatGPT Plus": 1200, "Claude Pro": 1150, "Midjourney": 950}
    selected_service = st.selectbox("اختر الخدمة:", list(options.keys()))
    price = options[selected_service]
    st.info(f"السعر التقديري: {price} ج.م")

elif category == "برامج وألعاب":
    selected_service = st.text_input("اكتب اسم البرنامج أو اللعبة (مثال: PUBG, Netflix, Adobe):")
    price = st.number_input("أدخل المبلغ المطلوب شحنه (بالدولار أو ما يعادله بالجنية):", min_value=1)
    st.warning("سيتم التواصل معك فوراً لتأكيد السعر النهائي حسب سعر الصرف اللحظي.")

else:
    selected_service = st.text_area("اكتب اسم الموقع أو الخدمة التي تريد دفع اشتراكها:")
    price = st.number_input("المبلغ المراد دفعه:", min_value=1)

# 2. بيانات التواصل والحساب
st.markdown("---")
st.markdown("### 📝 بيانات الطلب")
email = st.text_input("البريد الإلكتروني المراد تفعيل الخدمة عليه:", placeholder="user@example.com")
whatsapp_contact = st.text_input("رقم واتساب للمتابعة (اختياري):", placeholder="01xxxxxxxxx")

if email and price > 0:
    st.markdown("### 💳 إتمام الدفع")
    st.markdown(f"""
    <div class="payment-box">
        <p>يرجى تحويل المبلغ المتفق عليه إلى رقم فودافون كاش:</p>
        <h2 style="color: #25d366; letter-spacing: 2px;">{رقم_المحفظة}</h2>
        <p>بعد التحويل، ارفع الإيصال بالأسفل لتفعيل "رقم الطلب"</p>
    </div>
    """, unsafe_allow_html=True)

    # 3. تأكيد التحويل بالصور
    proof = st.file_uploader("📤 ارفع صورة إيصال التحويل هنا:", type=['png', 'jpg', 'jpeg'])

    if proof:
        if st.button("🚀 تأكيد الطلب وحجز الخدمة"):
            with st.spinner('جاري تسجيل طلبك في النظام العالمي لمنصة YOU...'):
                time.sleep(3)
                order_id = f"YOU-FREE-{int(time.time())}"
                st.success("✅ تم استلام طلبك بنجاح!")
                st.balloons()
                st.markdown(f"""
                <div style="background: #111; padding: 20px; border-radius: 10px; border: 1px solid #007bff; text-align: center;">
                    <h4>رقم العملية: <span style="color: #007bff;">#{order_id}</span></h4>
                    <p>الخدمة المطلوبة: <b>{selected_service}</b></p>
                    <p>سيتم مراجعة الطلب وتنفيذه خلال دقائق. شكرًا لثقتك في منصة YOU.</p>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
st.caption(f"بوابة YOU الشاملة | تحت إدارة م. {اسم_المهندس} 2026")
