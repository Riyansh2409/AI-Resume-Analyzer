# 🧠 AI Resume Analyzer

An intelligent AI-powered system that analyzes resumes against job descriptions using NLP and transformer-based models.

---

## 🚀 Features

- 📄 Upload Resume (PDF / DOCX)
- 🧠 Semantic similarity using Sentence-BERT
- 🛠️ Skill extraction and matching
- ❌ Missing skills detection
- 📊 Resume scoring system
- 💡 Suggestions for improvement
- 🌐 Interactive web UI using Streamlit

---

## 🛠️ Tech Stack

- Python
- Sentence Transformers (BERT)
- spaCy (NLP)
- PyMuPDF (PDF parsing)
- python-docx (DOCX parsing)
- Streamlit (UI)

---

## ⚙️ How It Works

1. Upload your resume (PDF/DOCX)
2. Enter job description
3. System:
   - Extracts text from resume
   - Computes semantic similarity using transformer embeddings
   - Extracts skills from both inputs
   - Matches skills and identifies gaps
4. Generates:
   - Similarity score
   - Skill match score
   - Final score
   - Suggestions for improvement

---

## ▶️ Run Locally

```bash
# Clone repo
git clone https://github.com/Riyansh2409/AI-Resume-Analyzer.git

# Go to project folder
cd AI-Resume-Analyzer

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy model (IMPORTANT)
python -m spacy download en_core_web_sm

# Run app
streamlit run ui.py