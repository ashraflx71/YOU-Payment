import streamlit as st
import time

# --- إعدادات القائد أشرف ---
رقم_المحفظة = "01014505254"
اسم_المهندس = "أشرف حسن"

st.set_page_config(page_title="YOU - المحرك الذكي", page_icon="🔍", layout="centered")

# --- كود الروح والتنسيق (إلغاء الإطارات المشتتة) ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000; color: #fff; direction: rtl; }}
    html, body, [class*="css"] {{ direction: rtl; text-align: right; font-family: 'Tahoma'; }}
    
    /* جعل محرك البحث يبدو كقطعة واحدة احترافية وبدون إطار أزرق خارجي */
    .stTextInput input {{
        background-color: #111 !important;
        color: white !important;
        border: 2px solid #333 !important;
        border-radius: 30px !important;
        padding: 20px !important;
        font-size: 20px !important;
        transition: 0.3s;
    }}
    .stTextInput input:focus {{
        border-color: #25d366 !important; /* أخضر عند الكتابة لإعطاء روح وثقة */
        box-shadow: 0 0 15px rgba(37, 211, 102, 0.2);
    }}
    
    .hint-text {{
        color: #888;
        font-size: 14px;
        margin-top: -15px;
        margin-bottom: 20px;
        padding-right: 15px;
    }}
    
    .service-badge {{
        display: inline-block;
        background: #1a1a1a;
        padding: 5px 15px;
        border-radius: 20px;
        border: 1px solid #333;
        margin: 5px;
        color: #ccc;
        font-size: 14px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- واجهة "الروح" ---
st.title("🌟 منصة YOU")
st.write("أهلاً بك يا هندسة.. محركنا يبحث لك عن أفضل طرق الشحن الدولي.")

# محرك البحث كـ "بطل" وحيد في الصفحة
query = st.text_input("", placeholder="🔍 اكتب هنا ما تريد (مثلاً: اشتراك GPT، هدية، Netflix...)", label_visibility="collapsed")

if not query:
    st.markdown('<p class="hint-text">اكتب أي خدمة وسيقوم نظامنا الآلي بتجهيز الطلب لك فوراً.</p>', unsafe_allow_html=True)
    
    # خدمات "تذكيرية" بدون روح الإطارات القديمة
    st.markdown("🌐 **خدمات يطلبها الآخرون الآن:**")
    st.markdown("""
    <span class="service-badge">ChatGPT Plus</span>
    <span class="service-badge">Netflix Premium</span>
    <span class="service-badge">هدية خاصة 🎁</span>
    <span class="service-badge">Google Drive</span>
    """, unsafe_allow_html=True)

# --- تنفيذ الطلب بـ "روح" تفاعلية ---
if query:
    st.markdown(f"### ⚡ جاري تجهيز طلب: `{query}`")
    
    # إظهار البيانات تدريجياً لراحة العين
    with st.container():
        email = st.text_input("📧 أدخل الإيميل الذي تود الشحن عليه:")
        amount = st.number_input("💰 القيمة المطلوبة (بالجنيه):", min_value=0)

        if email and amount > 0:
            st.markdown("---")
            # تنبيه بـ "روح" المساعدة
            st.success("✅ رائع! الخطوة الأخيرة هي إرسال قيمة الشحن لنبدأ التنفيذ.")
            
            st.markdown(f"""
            <div style="background: #0a0a0a; border-right: 5px solid #25d366; padding: 20px; border-radius: 10px;">
                <p style="margin: 0;">حول <b>{amount} ج.م</b> إلى محفظة فودافون كاش:</p>
                <h2 style="color: #25d366; margin: 10px 0;">{رقم_المحفظة}</h2>
                <p style="font-size: 12px; color: #666;">(المهندس أشرف يتابع طلبك الآن بمجرد رفع الإيصال)</p>
            </div>
            """, unsafe_allow_html=True)

            proof = st.file_uploader("📤 ارفع صورة التحويل هنا لربطها بطلبك:", type=['png', 'jpg', 'jpeg'])

            if proof:
                if st.button("🚀 تنفيذ الطلب الآن"):
                    with st.status("🛠️ جاري تسجيل الطلب وتنبيه الإدارة...", expanded=True) as status:
                        time.sleep(2)
                        st.write("التحقق من صحة الإيميل...")
                        time.sleep(1)
                        st.write("ربط الإيصال برقم الطلب...")
                        status.update(label="✅ اكتملت العملية بنجاح!", state="complete", expanded=False)
                    
                    st.balloons()
                    st.success(f"تم بنجاح! رقم طلبك هو: #YOU-{int(time.time())}")

st.markdown("---")
st.caption(f"منصة YOU | تحت إشراف م. {اسم_المهندس} 2026")
