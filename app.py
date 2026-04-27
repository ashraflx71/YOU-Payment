import streamlit as st
import time

# --- إعدادات القائد أشرف ---
رقم_المحفظة = "01014505254"
اسم_المهندس = "أشرف حسن"

st.set_page_config(page_title="YOU - محرك شحن الخدمات", page_icon="🔍", layout="centered")

# --- التنسيق الملكي العصري ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000; color: #fff; direction: rtl; }}
    html, body, [class*="css"] {{ direction: rtl; text-align: right; font-family: 'Tahoma'; }}
    
    /* ستايل محرك البحث */
    .search-container {{
        background: #111;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #007bff;
        box-shadow: 0 0 20px rgba(0, 123, 255, 0.1);
        margin-bottom: 30px;
    }}
    
    /* بطاقات الخدمات المشهورة (أمازون ستايل) */
    .popular-tag {{
        display: inline-block;
        background: #222;
        color: #007bff;
        padding: 8px 15px;
        border-radius: 20px;
        margin: 5px;
        cursor: pointer;
        border: 1px solid #333;
        transition: 0.3s;
    }}
    .popular-tag:hover {{
        background: #007bff;
        color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("🔍 محرك منصة YOU للخدمات")
st.write("ابحث عن أي خدمة، موقع، أو لعبة تريد شحنها أونلاين.")

# --- 1. محرك البحث الذكي ---
with st.container():
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    
    # حقل البحث الرئيسي
    search_query = st.text_input("ما الذي تريد شحنه اليوم؟", placeholder="مثال: اشتراك نتفليكس، شدات ببجي، ChatGPT...")
    
    # قسم "تذكير" بالخدمات المشهورة (Popular Services)
    st.markdown("<small style='color: #888;'>خدمات شائعة حالياً:</small>", unsafe_allow_html=True)
    
    # قائمة الخدمات المشهورة كأزرار سريعة
    popular_services = ["ChatGPT Plus", "Netflix", "Spotify", "PUBG Mobile", "Amazon Prime", "Adobe Creative Cloud", "Roblox"]
    
    # عرض الخدمات المشهورة بشكل أفقي
    cols = st.columns(len(popular_services))
    for i, service in enumerate(popular_services):
        if st.button(service, key=f"btn_{i}"):
            search_query = service # بمجرد الضغط يتم ملء محرك البحث
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. معالجة الطلب بناءً على البحث ---
if search_query:
    st.markdown(f"### 📋 تفاصيل طلب شحن: **{search_query}**")
    
    col_a, col_b = st.columns(2)
    with col_a:
        amount = st.number_input("المبلغ المراد شحنه (تقريبياً):", min_value=0)
    with col_b:
        email = st.text_input("البريد الإلكتروني المستهدف:")

    # --- 3. خطوة الدفع (تظهر فقط عند الجدية) ---
    if amount > 0 and email:
        st.markdown("---")
        st.info("💡 نظام YOU: سيتم احتساب أفضل سعر صرف متاح فور تأكيد التحويل.")
        
        st.markdown(f"""
        <div style="background: #0a0a0a; border: 2px solid #25d366; padding: 20px; border-radius: 15px; text-align: center;">
            <p>لإتمام عملية البحث والشحن لـ <b>{search_query}</b></p>
            <p>يرجى تحويل المبلغ إلى محفظة فودافون كاش:</p>
            <h2 style="color: #25d366; letter-spacing: 2px;">{رقم_المحفظة}</h2>
        </div>
        """, unsafe_allow_html=True)

        proof = st.file_uploader("📤 ارفع إيصال التحويل لتفعيل الطلب أوتوماتيكياً:", type=['png', 'jpg', 'jpeg'])

        if proof:
            if st.button("🚀 تنفيذ الطلب الآن"):
                with st.spinner('جاري معالجة الطلب في محرك البحث...'):
                    time.sleep(2)
                    order_id = f"YOU-SRCH-{int(time.time())}"
                    st.success(f"✅ تم استلام طلب {search_query} بنجاح!")
                    st.balloons()
                    st.write(f"رقم التتبع الخاص بك: **#{order_id}**")

st.markdown("---")
st.caption(f"محرك YOU الذكي | إدارة م. {اسم_المهندس} 2026")
