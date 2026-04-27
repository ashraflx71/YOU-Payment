import streamlit as st

st.set_page_config(page_title="YOU - Coming Soon", page_icon="🌟")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; text-align: center; direction: rtl; }
    .loader {
        border: 4px solid #111;
        border-top: 4px solid #007bff;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 2s linear infinite;
        margin: auto;
    }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
    <div style="margin-top: 15%;">
        <h1 style="color: #007bff; font-size: 50px;">YOU</h1>
        <p style="font-size: 20px; color: #888;">نعمل على بناء تجربة دفع رقمية تليق بكم..</p>
        <div class="loader"></div>
        <p style="margin-top: 20px; color: #25d366;">قريباً جداً | بإشراف م. أشرف حسن</p>
    </div>
    """, unsafe_allow_html=True)
