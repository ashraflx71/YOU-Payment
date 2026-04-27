import streamlit as st
import time

# --- إعدادات القائد أشرف ---
رقم_المحفظة = "01014505254"
اسم_المهندس = "أشرف حسن"

st.set_page_config(page_title="YOU - المحرك الفعال", page_icon="🔍", layout="centered")

# 1. تهيئة ذاكرة المحرك (عشان يفضل شغال وما يمسحش البيانات)
if 'service_query' not in st.session_state:
    st.session_state.service_query = ""

# 2. كود التصميم الملكي (إخفاء المشتتات وجعل البحث هو البطل)
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #000; color: #fff; direction: rtl; }
    
    /* ستايل محرك البحث الاحترافي */
    .stTextInput input {
        background-color: #111 !important;
        color: #25d366 !important; /* لون الخط أخضر لزيادة الروح */
        border: 2px solid #333 !important;
        border-radius: 50px !important;
        padding: 25px !important;
        font-size: 20px !important;
    }
    .stTextInput input:focus { border-color: #25d366 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔍 محرك منصة YOU")
st.write("اكتب الخدمة التي تريدها وسنقوم بتفعيلها لك فوراً.")

# --- 3. محرك البحث الفعال ---
# الدالة التي تجعل الأزرار المقترحة "تكتب" داخل محرك البحث
def set_search(name):
    st.session_state.service_query = name

# عرض المقترحات (تذكير للعميل)
cols = st.columns(4)
if cols[0].button("ChatGPT ⚡"): set_search("ChatGPT Plus")
if cols[1].button("Netflix 🎬"): set_search("Netflix Premium")
if cols[2].button("هدية 🎁"): set_search("طلب هدية خاصة")
if cols[3].button("PUBG 🎮"): set_search("شحن شدات ببجي")

# حقل البحث الرئيسي (مربوط بذاكرة النظام)
query = st.text_input("ماذا تريد أن تشحن اليوم؟", 
                     value=st.session_state.service_query, 
                     key="main_search",
                     placeholder="🔍 ابحث عن أي خدمة هنا...")

# تحديث الذاكرة بما يكتبه العميل يدوياً
st.session_state.service_query = query

# --- 4. منطق العمل (يظهر فقط إذا كان هناك نص في البحث) ---
if query:
    st.markdown(f"### ⚡ جاري معالجة طلب: **{query}**")
    
    # نموذج البيانات
    with st.container():
        email = st.text_input("📧 أدخل البريد الإلكتروني المستهدف:", key="user_email")
        amount = st.number_input("💰 القيمة المراد شحنها (بالجنيه المصري):", min_value=0, key="user_amount")
        
        if email and amount > 0:
            st.markdown("---")
            st.markdown(f"""
            <div style="background: #0a0a0a; border-right: 5px solid #25d366; padding: 20px; border-radius: 15px;">
                <p>خطوة الدفع لخدمة <b>{query}</b>:</p>
                <p>حول مبلغ <b>{amount} ج.م</b> إلى محفظة فودافون كاش:</p>
                <h2 style="color: #25d366; text-align: center; letter-spacing: 2px;">{رقم_المحفظة}</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # رفع الإيصال (الربط النهائي)
            proof = st.file_uploader("📤 ارفع صورة إيصال التحويل لتأكيد طلبك:", type=['png', 'jpg', 'jpeg'])
            
            if proof:
                if st.button("🚀 إرسال الطلب للتنفيذ الفوري"):
                    with st.spinner('جاري ربط طلبك بنظام المهندس أشرف...'):
                        time.sleep(2)
                        order_id = f"YOU-{int(time.time())}"
                        st.success(f"✅ تم استلام طلبك بنجاح!")
                        st.balloons()
                        st.info(f"رقم الطلب الخاص بك هو: #{order_id}")
                        st.write("سيتم تفعيل الخدمة خلال دقائق.")

else:
    st.info("💡 ابدأ بكتابة اسم الخدمة أو اختر من المقترحات أعلاه.")

st.markdown("---")
st.caption(f"منصة YOU | تدار بواسطة م. {اسم_المهندس} 2026")
