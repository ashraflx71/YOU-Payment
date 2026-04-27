import streamlit as st
import urllib.parse

# --- إعدادات القائد ---
رقم_الواتساب = "201280208018"  # الرقم المحدث
اسم_المهندس = "أشرف حسن"

st.set_page_config(page_title=f"منصة YOU | {اسم_المهندس}", page_icon="🌟", layout="centered")

# --- كود CSS الملكي المطور ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000000; color: #ffffff; direction: rtl; }}
    
    html, body, [class*="css"]  {{
        direction: rtl; text-align: right; font-family: 'Tahoma'; font-size: 22px;
    }}

    .royal-card {{
        background: linear-gradient(145deg, #0a0a0a, #111);
        border-right: 6px solid #007bff;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0, 123, 255, 0.2);
        border: 1px solid #1a1a1a;
    }}

    .stButton>button {{
        width: 100%;
        background-color: transparent;
        color: #007bff;
        border: 2px solid #007bff;
        border-radius: 30px;
        padding: 15px 20px;
        font-weight: bold;
        font-size: 20px;
        transition: 0.3s ease;
        margin-top: 10px;
    }}
    .stButton>button:hover {{
        background-color: #007bff;
        color: white;
        box-shadow: 0 0 25px #007bff;
        transform: translateY(-3px);
    }}

    .whatsapp-float {{
        position: fixed;
        width: 65px;
        height: 65px;
        bottom: 30px;
        left: 30px;
        background-color: #25d366;
        color: #FFF;
        border-radius: 50px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    </style>
    
    <a href="https://wa.me/{رقم_الواتساب}" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35px">
    </a>
    """, unsafe_allow_html=True)

# --- المحتوى الرئيسي ---
st.title("🌟 منصة YOU للخدمات الرقمية")

st.markdown(f"""
<div class="royal-card">
    <h3>مرحباً بك يا هندسة 🛠️</h3>
    <p>اشحن حساباتك الدولية الآن بأمان تام عبر <b>فودافون كاش</b> أو <b>إنستا باي</b> بالعملة المحلية.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("🚀 اختر الخدمة لبدء الطلب فوراً")

def send_wa(service):
    msg = f"أهلاً بشمهندس أشرف، أريد الاستفسار عن شحن {service} عبر منصة YOU"
    encoded_msg = urllib.parse.quote(msg)
    return f"https://wa.me/{رقم_الواتساب}?text={encoded_msg}"

col1, col2 = st.columns(2)

with col1:
    st.markdown(f'<a href="{send_wa("ChatGPT Plus")}" target="_blank" style="text-decoration:none;"><div class="stButton"><button>ChatGPT Plus ⚡</button></div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{send_wa("Claude.ai Pro")}" target="_blank" style="text-decoration:none;"><div class="stButton"><button>Claude.ai Pro 🧠</button></div></a>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<a href="{send_wa("Midjourney")}" target="_blank" style="text-decoration:none;"><div class="stButton"><button>Midjourney 🎨</button></div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{send_wa("خدمة أخرى")}" target="_blank" style="text-decoration:none;"><div class="stButton"><button>خدمات أخرى 🌐</button></div></a>', unsafe_allow_html=True)

st.info("⚡ تنفيذ سريع | دعم فني متواصل | أسعار تنافسية")

st.markdown("---")
st.markdown(f"<div style='text-align: center; color: #888;'>م. {اسم_المهندس} | 2026 🚀</div>", unsafe_allow_html=True)
