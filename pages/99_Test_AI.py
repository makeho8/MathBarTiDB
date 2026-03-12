import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Doctor", page_icon="🩺")
st.title("🩺 ‍AI Connection Doctor")

# 1. CHECK THE KEY
st.subheader("1. Checking API Key")
try:
    # Try to grab the key safely
    api_key = st.secrets["gemini"]["api_key"]
    st.success(f"✅ Key Found: `{api_key[:6]}...`")
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("❌ Could not find Key in secrets.toml")
    st.code("""
    [gemini]
    api_key = "AIza..."
    """)
    st.stop()

# 2. CHECK THE MODELS
st.subheader("2. Asking Google for Available Models")
try:
    # Ask Google: "What models can I use?"
    models = list(genai.list_models())
    
    chat_models = []
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            chat_models.append(m.name)
            
    if chat_models:
        st.success(f"✅ Connection Works! Found {len(chat_models)} models.")
        st.write("### 📋 Copy one of these EXACT names:")
        for name in chat_models:
            st.code(f"model = genai.GenerativeModel('{name}')")
            # Note: Sometimes it requires 'models/gemini-pro' instead of just 'gemini-pro'
    else:
        st.warning("⚠️ Connected, but no Chat models found. Check your API Key permissions.")

except Exception as e:
    st.error(f"❌ Crash Report: {e}")
    st.info("💡 Try running: pip install --upgrade google-generativeai")