# 🚀 AI Resume Screening System

An AI-powered ATS (Applicant Tracking System) Resume Screening application built using Python, NLP, Machine Learning, and Streamlit.

This system analyzes resumes, extracts skills, compares them with job descriptions, calculates ATS match scores, and identifies missing skills.

---

# 📌 Features

✅ Resume PDF Parsing  
✅ NLP-based Text Preprocessing  
✅ Skill Extraction  
✅ TF-IDF Resume Matching  
✅ Cosine Similarity Scoring  
✅ Missing Skills Detection  
✅ Interactive Streamlit UI  
✅ ATS Match Percentage  
✅ Resume Analysis Dashboard  

---

# 🧠 Technologies Used

- Python
- NLTK
- Scikit-learn
- Streamlit
- PyPDF2
- Machine Learning
- Natural Language Processing (NLP)

---

# 📂 Project Structure

```bash
FUTURE_ML_03/
│
├── app.py
├── requirements.txt
├── README.md
├── download_nltk.py
│
├── data/
│   ├── resumes/
│   ├── extracted_text/
│   ├── cleaned_resumes/
│   ├── extracted_skills/
│   └── job_descriptions/
│
├── src/
│   ├── extract_text.py
│   ├── preprocess.py
│   ├── skills.py
│   ├── skill_extractor.py
│   ├── scorer.py
│   └── missing_skills.py
│
└── venv/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Likhita-sri/FUTURE_ML_03.git
```

## Move to Project Folder

```bash
cd FUTURE_ML_03
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📊 How It Works

1. Upload Resume PDF  
2. Enter Job Description  
3. System extracts resume text  
4. NLP preprocessing is applied  
5. Skills are extracted  
6. Resume is compared with job description  
7. ATS score is calculated  
8. Missing skills are identified  

---

# 🖥️ Application Features

- Resume Upload
- Job Description Input
- ATS Match Score
- Resume Skills Detection
- Missing Skills Analysis
- Interactive UI Dashboard

---

# 📈 Future Improvements

- Multi Resume Screening
- Resume Ranking Dashboard
- AI-based Recommendations
- Resume Category Prediction
- OCR Support
- BERT/Sentence Transformer Embeddings

---

# 👩‍💻 Author

**Likhita Sri**

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!