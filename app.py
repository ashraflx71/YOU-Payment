import streamlit as st

# إعدادات المصنع للقائد أشرف
رقم_الواتساب = "201280208018"
st.set_page_config(page_title="YOU Payment", page_icon="⚡", layout="centered")

# CSS فائق السرعة والخفة
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000; color: #fff; direction: rtl; }}
    .main-btn {{
        display: block;
        background: linear-gradient(90deg, #007bff, #0056b3);
        color: white !important;
        text-align: center;
        padding: 20px;
        margin: 15px 0;
        border-radius: 15px;
        text-decoration: none;
        font-weight: bold;
        font-size: 24px;
        box-shadow: 0 4px 15px rgba(0,123,255,0.3);
        transition: 0.2s;
    }}
    .main-btn:active {{ transform: scale(0.95); background: #25d366; }}
    .trust-badge {{
        background: #111;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #222;
        text-align: center;
        font-size: 16px;
        color: #25d366;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ شحن فوري - منصة YOU")

st.markdown('<div class="trust-badge">✅ نظام آلي معتمد | تنفيذ خلال 5 دقائق</div>', unsafe_allow_html=True)

# دالة توليد الرابط الصاروخي
def fast_link(service):
    import urllib.parse
    msg = f"طلب شحن فوري: {service}"
    return f"https://wa.me/{رقم_الواتساب}?text={urllib.parse.quote(msg)}"

# أزرار مباشرة (بدون فورم، بدون انتظار)
st.markdown(f'<a href="{fast_link("ChatGPT Plus")}" class="main-btn">شحن ChatGPT Plus ⚡</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{fast_link("Claude Pro")}" class="main-btn">شحن Claude.ai Pro 🧠</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{fast_link("Midjourney")}" class="main-btn">شحن Midjourney 🎨</a>', unsafe_allow_html=True)

st.warning("⚠️ اضغط على الخدمة، وسيفتح الواتساب فوراً لإتمام الدفع.")

st.markdown("---")
st.caption("إدارة المهندس أشرف حسن | ضمان السرعة القصوى")
