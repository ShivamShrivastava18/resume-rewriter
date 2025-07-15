#  Setup Instructions for Resume Bullet Point Rewriter

This guide walks you through setting up the project locally using the Groq API and Streamlit.

---

##  Prerequisites

* Python 3.8 or higher
* [Groq API key](https://console.groq.com/)
* Internet connection

---

##  1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-rewriter-groq.git
cd resume-rewriter-groq
```

> If you don’t have Git, you can just download the ZIP and extract it.

---

##  2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

##  3. Install Dependencies

```bash
pip install -r requirements.txt
```

> The required packages are:
>
> * `streamlit`
> * `groq`
> * `python-dotenv`

---

##  4. Create a `.env` File

In the project root, create a file named `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

##  5. Run the Streamlit App

```bash
streamlit run app.py
```

> The app will open in your browser at `http://localhost:8501/`

---

##  Troubleshooting

* **Invalid API key?**
  Make sure `.env` is in the root directory and correctly formatted.

* **Groq not responding?**
  Check your internet connection and verify the model name is available at [console.groq.com](https://console.groq.com).

---

##  You're All Set!

You can now paste any resume bullet point and get 6 rewritten versions using 2 LLMs and 3 prompt strategies, all for free 🎉
