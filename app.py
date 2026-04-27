import streamlit as st
import pandas as pd
from datetime import datetime
import os
import requests

# 1. إعدادات الصفحة والتنسيق الملكي (22px)
st.set_page_config(page_title="YOU Payment System", layout="centered", page_icon="💰")

# 2. الثوابت والأمان (يتم جلبها من Secrets)
TELEGRAM_BOT_TOKEN = st.secrets.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = st.secrets.get("TELEGRAM_CHAT_ID")
ADMIN_PASSWORD = st.secrets.get("ADMIN_PASSWORD", "ashraf2026")
ORDERS_FILE = 'you_orders.csv'

# 3. واجهة المستخدم والتصميم الملكي (CSS)
st.markdown("""
    <style>
        /* الخلفية والخطوط العامة */
        .stApp, [data-testid="stMainBlockContainer"] { background-color: #000000; color: #ffffff; }
        p, li, span, label, input, .stSelectbox, .stSlider { font-size: 22px !important; }
        
        /* العناوين */
        h1, h2, h3 { color: #00d4ff !important; text-align: center; font-weight: bold; margin-bottom: 20px; }
        
        /* البطاقات الإحصائية */
        .stMetric { background-color: #111111 !important; border: 1px solid #0056b3 !important; border-radius: 10px; padding: 15px; }
        
        /* الأزرار */
        .stButton>button { 
            width: 100%; 
            background-color: #0056b3 !important; 
            color: white !important; 
            border-radius: 10px; 
            height: 55px; 
            font-size: 22px; 
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover { background-color: #00d4ff !important; color: black !important; }
        
        /* القائمة الجانبية */
        [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 1px solid #111111; }
        
        /* التنبيهات */
        .stInfo { background-color: #1A1A1A; border: 1px solid #00d4ff; color: #ffffff; }
        .stSuccess { background-color: #002200; color: #ffffff; border: 1px solid #00ff00; }
    </style>
    """, unsafe_allow_html=True)

# 4. الدوال المساعدة
def send_telegram_notification(message):
    """إرسال إشعار فوري لهاتفك عبر تلجرام عند حدوث عملية جديدة."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        st.error(f"خطأ في إرسال تلجرام: {e}")

def save_transaction(service, method, sender, amount):            
    """دالة حفظ العمليات في ملف CSV لضمان استمرار البيانات."""
    file_path = ORDERS_FILE
    new_data = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d %H:%M"), service, method, sender, amount]], 
                             columns=['التوقيت', 'الخدمة', 'الوسيلة', 'المرسل', 'المبلغ'])
    if not os.path.isfile(file_path):
        new_data.to_csv(file_path, index=False, encoding='utf-8-sig')
    else:
        new_data.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8-sig')

# 5. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("<h1 style='font-size: 40px;'>YOU</h1>", unsafe_allow_html=True)
    st.title("القائمة الرئيسية")
    menu = st.radio("انتقل إلى:", ["🌟 خدمات YOU", "💳 طلب خدمة دفع", "🔐 لوحة التحكم"])
    st.markdown("---")
    st.info("نظام YOU - اشتري عالمياً، ادفع محلياً")
    st.caption("تطوير م. أشرف حسن © 2026")

# 6. محتوى الصفحات
if menu == "🌟 خدمات YOU":
    st.header("🌟 منصة YOU للخدمات الرقمية")
    st.markdown("""
    <div style="background-color: #111111; padding: 25px; border-radius: 15px; border-left: 5px solid #00d4ff; margin-bottom: 25px;">
        <p style="text-align: right;">مرحباً بك يا هندسة. نظام YOU يوفر لك أسهل طريقة لشحن الحسابات الدولية وشراء خدمات الذكاء الاصطناعي بالعملة المحلية.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🤖 أدوات AI")
        st.write("• ChatGPT Plus\n• Midjourney\n• Claude.ai")
    with col2:
        st.subheader("🛍️ المتاجر")
        st.write("• Amazon Global\n• Google Play\n• Apple Store")

elif menu == "💳 طلب خدمة دفع":
    st.header("💳 طلب شحن رصيد / خدمة")
    with st.form("payment_form", clear_on_submit=True):
        sender = st.text_input("رقم الموبايل (المرتبط بالمحفظة)")
        service_type = st.selectbox("نوع الخدمة المطلوبة", 
                                    ["شحن محفظة YOU", "اشتراك ChatGPT", "رصيد Google Play", "Amazon Card"])
        amount = st.number_input("المبلغ المطلوب (بالجنيه المصري)", min_value=10.0, step=50.0)
        payment_method = st.radio("وسيلة التحويل التي ستستخدمها", ["فودافون كاش", "إنستا باي (InstaPay)"])
        
        submitted = st.form_submit_button("إرسال طلب الدفع الآن")
        if submitted:
            if sender and amount > 0:
                # حفظ في الملف
                save_transaction(service_type, payment_method, sender, amount)
                
                # إرسال تلجرام
                msg = f"<b>💰 طلب دفع جديد</b>\n\n<b>الخدمة:</b> {service_type}\n<b>المبلغ:</b> {amount} ج.م\n<b>المرسل:</b> {sender}\n<b>الوسيلة:</b> {payment_method}"
                send_telegram_notification(msg)
                
                st.success("✅ تم استلام طلبك بنجاح. جاري المراجعة والتنفيذ الآن.")
            else:
                st.error("❌ يرجى إدخال رقم الموبايل والمبلغ بشكل صحيح.")

elif menu == "🔐 لوحة التحكم":
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        
    if not st.session_state.authenticated:
        with st.form("admin_login"):
            st.subheader("🔐 دخول المسؤول")
            password = st.text_input("كلمة مرور الإدارة", type="password")
            if st.form_submit_button("دخول"):
                if password == ADMIN_PASSWORD:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("❌ كلمة المرور غير صحيحة")
    else:
        st.title("📊 إدارة العمليات")
        if st.button("تس
