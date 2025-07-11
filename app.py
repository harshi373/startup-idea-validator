import streamlit as st
import requests

def pich_idea(idea):
    API_URL = "https://router.huggingface.co/featherless-ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer HF_TOKEN",
    }

    prompt = f"""
Act as a startup business analyst.

Analyze the following startup idea:
"{idea}"

Provide the following:
1. Market Potential  
2. Competitive Analysis  
3. SWOT Analysis  
4. Monetization Strategies  
5. Suggested MVP Features
"""

    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "mistralai/Mistral-7B-Instruct-v0.2"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit UI setup
st.set_page_config(page_title="Startup Idea Validator", layout="centered")
st.title("🚀 Startup Idea Validator using LLM")

st.markdown("""
Enter your startup idea. This AI tool will generate:
- 📊 Market Potential  
- 🏁 Competitive Analysis  
- 🔍 SWOT Analysis  
- 💰 Monetization Strategies  
- 🧪 MVP Feature Suggestions
""")

# Input box
startup_idea = st.text_area("💡 Startup Idea", height=200)

# Button click handler
if st.button("🔍 Generate Validation Report"):
    if not startup_idea.strip():
        st.warning("⚠️ Please enter a startup idea first.")
    else:
        with st.spinner("🤖 Analyzing idea with LLM..."):
            result = pich_idea(startup_idea)
        
        st.subheader("📋 Validation Report")
        
        # Split result into sections using line-based headers
        sections = {
            "📈 Market Potential": "",
            "🏁 Competitive Analysis": "",
            "🔍 SWOT Analysis": "",
            "💰 Monetization Strategies": "",
            "🧪 Suggested MVP Features": ""
        }
        
        current_key = None
        for line in result.splitlines():
            line = line.strip()
            for key in sections:
                if key.split(" ", 1)[1].lower() in line.lower():
                    current_key = key
                    break
            else:
                if current_key:
                    sections[current_key] += line + "\n"

        for title, content in sections.items():
            with st.expander(title, expanded=True):
                st.markdown(content.strip())
        
        st.balloons()
