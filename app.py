import streamlit as st
import PyPDF2
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.skills import SKILLS


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🚀",
    layout="wide"
)


# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

/* Remove default padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.4);
    margin-bottom: 30px;
}

.hero h1 {
    color: white;
    font-size: 52px;
    margin-bottom: 10px;
}

.hero p {
    color: #e5e7eb;
    font-size: 20px;
}

/* Glass Cards */
.glass {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Score Card */
.score-card {
    background: linear-gradient(135deg, #10b981, #059669);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    color: white;
    box-shadow: 0px 10px 25px rgba(16,185,129,0.4);
    animation: float 3s ease-in-out infinite;
}

.score-card h1 {
    font-size: 55px;
}

/* Animation */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}

/* Skill Tags */
.skill-box {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    padding: 12px 18px;
    border-radius: 50px;
    display: inline-block;
    margin: 6px;
    font-weight: bold;
    font-size: 15px;
    box-shadow: 0px 4px 10px rgba(37,99,235,0.4);
}

/* Missing Skills */
.missing-skill {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: white;
    padding: 12px 18px;
    border-radius: 50px;
    display: inline-block;
    margin: 6px;
    font-weight: bold;
    font-size: 15px;
    box-shadow: 0px 4px 10px rgba(239,68,68,0.4);
}

/* Upload Section */
.upload-box {
    border: 2px dashed #60a5fa;
    border-radius: 20px;
    padding: 20px;
    background: rgba(255,255,255,0.03);
}

/* Sidebar */
.css-1d391kg {
    background-color: #111827;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 15px;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    font-size: 20px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0px 8px 20px rgba(124,58,237,0.5);
}

/* Text Area */
textarea {
    border-radius: 15px !important;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# PDF EXTRACTION
# -------------------------------------------------
def extract_text_from_pdf(uploaded_file):

    text = ""

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text


# -------------------------------------------------
# CLEAN TEXT
# -------------------------------------------------
def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    return text


# -------------------------------------------------
# SKILL EXTRACTION
# -------------------------------------------------
def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🚀 AI Resume Screening System</h1>
    <p>Smart ATS Resume Analyzer using NLP & Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("📌 Features")

st.sidebar.markdown("""
### This ATS System Can:

✅ Extract Resume Text  
✅ Detect Candidate Skills  
✅ Compare Resume with JD  
✅ Calculate ATS Score  
✅ Detect Missing Skills  
✅ Analyze PDF Resumes  
""")

st.sidebar.markdown("---")

st.sidebar.info("Built using Python, NLP, Scikit-learn and Streamlit")


# -------------------------------------------------
# INPUT SECTION
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("📄 Upload Resume")

    uploaded_resume = st.file_uploader(
        "Choose Resume PDF",
        type=["pdf"]
    )

    st.markdown('</div>', unsafe_allow_html=True)


with col2:

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("📝 Job Description")

    job_description = st.text_area(
        "Paste Job Description Here",
        height=250
    )

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------------------
# ANALYZE BUTTON
# -------------------------------------------------
if st.button("🔍 Analyze Resume"):

    if uploaded_resume and job_description:

        # Extract Text
        resume_text = extract_text_from_pdf(uploaded_resume)

        # Clean Text
        cleaned_resume = clean_text(resume_text)
        cleaned_jd = clean_text(job_description)

        # Skills
        resume_skills = extract_skills(cleaned_resume)
        jd_skills = extract_skills(cleaned_jd)

        # TF-IDF Similarity
        documents = [cleaned_resume, cleaned_jd]

        vectorizer = TfidfVectorizer()

        tfidf_matrix = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )

        score = round(similarity[0][0] * 100, 2)

        # Missing Skills
        missing_skills = list(
            set(jd_skills) - set(resume_skills)
        )


        # -------------------------------------------------
        # SCORE SECTION
        # -------------------------------------------------
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="score-card">
            <h2>ATS MATCH SCORE</h2>
            <h1>{score}%</h1>
        </div>
        """, unsafe_allow_html=True)

        st.progress(min(int(score), 100))

        st.markdown("---")


        # -------------------------------------------------
        # RESULT COLUMNS
        # -------------------------------------------------
        col3, col4 = st.columns(2)


        # Resume Skills
        with col3:

            st.markdown('<div class="glass">', unsafe_allow_html=True)

            st.subheader("✅ Resume Skills")

            if resume_skills:

                for skill in resume_skills:

                    st.markdown(
                        f'<span class="skill-box">{skill}</span>',
                        unsafe_allow_html=True
                    )

            else:

                st.warning("No skills detected")

            st.markdown('</div>', unsafe_allow_html=True)


        # Missing Skills
        with col4:

            st.markdown('<div class="glass">', unsafe_allow_html=True)

            st.subheader("❌ Missing Skills")

            if missing_skills:

                for skill in missing_skills:

                    st.markdown(
                        f'<span class="missing-skill">{skill}</span>',
                        unsafe_allow_html=True
                    )

            else:

                st.success("Perfect Match! No Missing Skills")

            st.markdown('</div>', unsafe_allow_html=True)


        # -------------------------------------------------
        # EXTRA INFO SECTION
        # -------------------------------------------------
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("📊 Analysis Summary")

        st.write(f"✅ Resume Skills Found: {len(resume_skills)}")
        st.write(f"📌 Required Skills: {len(jd_skills)}")
        st.write(f"❌ Missing Skills: {len(missing_skills)}")

        if score >= 70:
            st.success("Excellent Resume Match")

        elif score >= 40:
            st.warning("Moderate Resume Match")

        else:
            st.error("Low Resume Match")

        st.markdown('</div>', unsafe_allow_html=True)


    else:

        st.warning("⚠️ Please upload a resume and enter a job description.")
