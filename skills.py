import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

# Skills list (expand kar sakte hain)
SKILLS = [
    "python", "java", "sql", "machine learning",
    "deep learning", "nlp", "aws", "docker", "git"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))