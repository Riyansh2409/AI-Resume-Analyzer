from sentence_transformers import SentenceTransformer, util

print("Loading model...")

model = SentenceTransformer('all-MiniLM-L6-v2')

resume = "I know Python, Machine Learning, SQL"
job = "Looking for Python developer with ML skills"

score = util.cos_sim(model.encode(resume), model.encode(job))

print("Similarity Score:", score.item())