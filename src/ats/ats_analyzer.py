from src.llm.gemini_client import generate_response


def analyze_resume_ats(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the resume against the job description.

Give:

1. ATS Score out of 100
2. Strengths
3. Weaknesses
4. Missing Skills
5. Resume Improvement Suggestions
6. Improved Professional Summary

Resume:
{resume_text}

Job Description:
{job_description}
"""

    return generate_response(prompt)