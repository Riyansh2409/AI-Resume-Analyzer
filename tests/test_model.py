# from src.ats.ats_analyzer import analyze_resume_ats

# resume = """
# Python
# SQL
# Machine Learning
# """

# job = """
# Looking for Python Developer with Docker,
# AWS and Machine Learning experience.
# """

# result = analyze_resume_ats(resume, job)

# print(result)


from src.parser.file_parser import extract_text
from src.ats.ats_analyzer import analyze_resume_ats

resume_text = extract_text("tests/RIYANSH_24BTRCL166.pdf")

job_description = """
Looking for an AI/ML Intern with Python,
Machine Learning, Deep Learning,
SQL, NLP and Generative AI knowledge.
"""

result = analyze_resume_ats(
    resume_text,
    job_description
)

print(result)