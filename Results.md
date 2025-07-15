##  Models and Tools Used

- **LLMs via Groq API**:
  - `meta-llama/llama-4-maverick-17b-128e-instruct`
  - `deepseek-r1-distill-llama-70b`

- **Frameworks & Tools**:
  - [`groq` Python SDK](https://pypi.org/project/groq/)
  - `streamlit` for UI
  - `python-dotenv` for loading API keys from `.env`

---

##  Best Performing Setup

- **Model**: `deepseek-r1-distill-llama-70b`
- **Prompt**: *Recruiter Roleplay*
- **Why?**  
  - Delivered more polished, industry-relevant bullet points
  - Incorporated metrics and keywords naturally
  - Minimal hallucinations compared to other prompts/models
  - Detailed explanation behind each decision

---

##  Prompting Strategies Used

1. **Standard Rewrite**  
   > “Rewrite the following resume bullet to be more impactful, use strong verbs, industry keywords, and include metrics if possible.”

2. **Creative Rewrite**  
   > “Transform the following resume point into a strong, action-oriented sentence for a top-tier resume. Keep it concise and professional.”

3. **Recruiter Roleplay**  
   > “You are a recruiter at a Fortune 500 company. Improve the resume bullet below to highlight achievements and industry relevance. Use clear, metric-based language if appropriate.”

---

##  Challenges Faced

- **Prompt Engineering to Prevent Hallucinations**:
  - Initial prompts led to vague or fabricated metrics
  - Mitigated by:
    - Role-specific prompting
    - Clear constraints in prompt wording
    - Avoiding overly generic verbs or filler language
