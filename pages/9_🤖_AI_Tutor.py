import streamlit as st
import time
import google.generativeai as genai

# --- 1. SAFE IMPORT FOR OFFLINE AI ---
# We wrap this in a try-block so the app DOES NOT CRASH if you haven't installed gpt4all
try:
    import ai_manager 
    HAS_OFFLINE = True
except ImportError:
    HAS_OFFLINE = False

# --- CONFIGURATION ---
st.set_page_config(page_title="Hybrid AI Tutor", page_icon="🤖")

# --- SIDEBAR: THE BRAIN SWITCH ---
st.sidebar.header("🧠 AI Brain Settings")
mode = st.sidebar.radio(
    "Choose Intelligence Source:",
    ["☁️ Online (Gemini)", "🏠 Offline (GPT4All)"],
    help="Online is smarter. Offline works without internet."
)

# --- SIDEBAR: CLEAR BUTTON ---
with st.sidebar:
    st.write("### ⚙️ Controls")
    if st.button("🗑️ Clear Chat History", type="primary"):
        st.session_state.messages = [] 
        st.rerun() 

st.title("🤖 Math Tutor")
if "Online" in mode:
    st.caption("🟢 Status: Connected to Google Gemini (High Intelligence)")
else:
    st.caption("🟠 Status: Running Locally on Device (Privacy Mode)")

# --- 2. DEFINE THE TWO BRAINS ---

def get_online_response(user_input):
    """
    Connects to Google Gemini API.
    """
    # 🛠️ FIX 1: ACCESS THE KEY CORRECTLY
    # We use .get() to avoid crashing if the key is missing entirely
    api_key_group = st.secrets.get("gemini")
    
    if not api_key_group:
        return "⚠️ Error: Missing [gemini] section in secrets.toml"
        
    API_KEY = api_key_group.get("api_key")
    
    if not API_KEY:
        return "⚠️ Error: Missing 'api_key' inside secrets.toml"

    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"❌ Connection Error: {str(e)}"

def get_offline_response(user_input):
    """
    Connects to your local GPT4All file safely.
    """
    # 🛠️ FIX 2: PREVENT CRASH IF LIBRARY MISSING
    if not HAS_OFFLINE:
        return "❌ Offline Error: Module 'gpt4all' is not installed. Please use Online mode or run `pip install gpt4all`."
    
    try:
        return ai_manager.get_ai_response(user_input)
    except Exception as e:
        return f"⚠️ Offline Error: {str(e)}"

# --- 3. SESSION STATE (Chat History) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 4. DISPLAY HISTORY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. HANDLE INPUT ---
if prompt := st.chat_input("Ask a math question..."):
    # A. Show User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # B. Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        if "Online" in mode:
            with st.spinner("☁️ Connecting to Google Cloud..."):
                response_text = get_online_response(prompt)
        else:
            response_text = get_offline_response(prompt)
        
        message_placeholder.markdown(response_text)
        
    # C. Save to History
    st.session_state.messages.append({"role": "assistant", "content": response_text})