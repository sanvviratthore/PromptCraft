import streamlit as st
import os
from openai import AzureOpenAI
from langsmith import traceable  # NEW

# Set LangSmith environment variables
os.environ["LANGCHAIN_API_KEY"] = os.environ["LANGCHAIN_API_KEY"]

# Azure OpenAI setup
client = AzureOpenAI(
    api_key=st.secrets["AZURE_OPENAI_KEY"],
    api_version=st.secrets["AZURE_OPENAI_VERSION"],
    azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"],
)
deployment_name = st.secrets["AZURE_DEPLOYMENT_NAME"]

# ⭐️ Traceable prompt optimization function
@traceable(name="Optimize Prompt")
def optimize_prompt(raw_prompt):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {
                "role": "system",
                "content": "You're a helpful AI that improves and rewrites prompts to make them clearer and more effective.",
            },
            {
                "role": "user",
                "content": f"Please optimize this prompt:\n\n{raw_prompt}",
            },
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()


# Custom Styling
st.markdown("""
    <style>
        html, body {
            background-color: #f9f9fb;
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }

        .block-container {
            padding-top: 2rem !important;
        }

        .glass-box {
            background: rgba(255, 255, 255, 0.65);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border-radius: 18px;
            padding: 2rem;
            max-width: 700px;
            margin: 2rem auto;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        }

        .title {
            font-size: 2.7rem;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(to right, #5f0aff, #b82eff);
            -webkit-background-clip: text;
            color: transparent;
            margin-bottom: 0.3em;
        }

        .subtitle {
            font-size: 1rem;
            color: #555;
            text-align: center;
            margin-bottom: 2em;
        }

        .output-box {
            background: rgba(255, 255, 255, 0.6);
            border-radius: 12px;
            padding: 1.2em;
            margin-top: 2em;
            margin-bottom: 2em;
            font-size: 15px;
            color: #222;
            line-height: 1.6;
            box-shadow: inset 0 0 6px rgba(0,0,0,0.04);
        }

        .footer {
            margin-top: 4em;
            text-align: center;
            font-size: 0.9rem;
            color: #aaa;
        }
    </style>
""", unsafe_allow_html=True)

# Glass UI wrapper
st.markdown("<div class='glass-box'>", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<div class='title'>PromptCraft</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Transform raw thoughts into clean, structured GPT-4 prompts.</div>", unsafe_allow_html=True)

# Prompt input
user_prompt = st.text_area("Your Prompt", height=180, placeholder="e.g. Summarize this article in simple terms...")

# Button + GPT-4 integration
if st.button("Optimize"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Optimizing your prompt..."):
            optimized = optimize_prompt(user_prompt)
            st.markdown(f"""
                <div class='output-box'>
                    <b>Optimized Prompt:</b><br><br>
                    {optimized}
                </div>
            """, unsafe_allow_html=True)

# Close glass container
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>© 2025 PromptCraft · Made with Streamlit</div>", unsafe_allow_html=True)
