import streamlit as st
from file_parser import extract_text
from utils import get_similarity
from skills import extract_skills

st.title("🧠 AI Resume Analyzer")

# File upload
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

# Job description input
job_text = st.text_area("Enter Job Description")

if st.button("Analyze Resume"):

    if uploaded_file is not None and job_text:

        # Save file temporarily
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        resume = extract_text(uploaded_file.name)

        # Similarity
        similarity_score = get_similarity(resume, job_text)

        # Skills
        resume_skills = extract_skills(resume)
        job_skills = extract_skills(job_text)

        matched = list(set(resume_skills) & set(job_skills))
        missing = list(set(job_skills) - set(resume_skills))

        # Skill score
        skill_score = (len(matched) / len(job_skills)) * 100 if job_skills else 0

        # Final score
        final_score = (similarity_score * 0.6) + (skill_score * 0.4)

        # OUTPUT
        st.subheader("📊 Results")

        st.write(f"Similarity Score: {round(similarity_score,2)}%")
        st.write(f"Skill Match Score: {round(skill_score,2)}%")
        st.write(f"Final Score: {round(final_score,2)}%")

        st.success(f"Matched Skills: {matched}")
        st.error(f"Missing Skills: {missing}")

        st.subheader("💡 Suggestions")
        for skill in missing:
            st.write(f"Learn {skill}")

    else:
        st.warning("Please upload resume and enter job description")