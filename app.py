import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# --- Load environment variables from .env ---
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# --- Model choices ---
MODELS = {
    "LLaMA 4 Maverick": "meta-llama/llama-4-maverick-17b-128e-instruct",
    "DeepSeek 70B": "deepseek-r1-distill-llama-70b"
}

# --- Prompt templates ---
PROMPTS = {
    "Standard Rewrite": lambda b: f"Rewrite the following resume bullet to be more impactful, use strong verbs, industry keywords, and include metrics if possible:\nBullet: {b}",
    "Creative Rewrite": lambda b: f"Transform the following resume point into a strong, action-oriented sentence for a top-tier resume:\nBullet: {b}\nKeep it concise and professional.",
    "Recruiter Roleplay": lambda b: f"You are a recruiter at a Fortune 500 company. Improve the resume bullet below to highlight achievements and industry relevance:\nOriginal Bullet: {b}\nUse clear, metric-based language if appropriate."
}

# --- Call Groq ---
def call_groq_sdk(model: str, prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"

# --- UI ---
st.set_page_config(page_title="Resume Rewriter", layout="wide")
st.title("📄 Resume Bullet Point Rewriter")
st.caption("Uses free ultra-fast models from Groq, choose one that suits you.")

bullet_input = st.text_area("✍️ Enter a resume bullet point:", height=100, placeholder="e.g. Scheduled appointments, managed emails...")

if st.button("🔁 Rewrite Bullet"):
    if not bullet_input.strip():
        st.warning("Please enter a bullet point.")
    else:
        with st.spinner("Generating rewritten bullet points..."):
            for model_name, model_id in MODELS.items():
                st.subheader(f"🧠 Model: {model_name}")
                for prompt_name, prompt_func in PROMPTS.items():
                    prompt = prompt_func(bullet_input)
                    result = call_groq_sdk(model_id, prompt)
                    st.markdown(f"**{prompt_name}**")
                    st.success(result)
                    st.markdown("---")
