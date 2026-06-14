from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_similarity(resume, job):
    resume_emb = model.encode(resume)
    job_emb = model.encode(job)
    score = util.cos_sim(resume_emb, job_emb)
    return score.item() * 100