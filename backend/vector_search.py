
from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd

model = SentenceTransformer("all-MiniLM-L6-v2")
df = pd.read_csv("data/faq_data.csv", quotechar='"')

questions = df["question"].tolist()
embeddings = model.encode(questions)
index = faiss.IndexFlatL2(384)
index.add(embeddings)

def get_similar_question(user_input):
    user_embedding = model.encode([user_input])
    D, I = index.search(user_embedding, k=1)
    if D[0][0] < 1.0:
        return df.iloc[I[0][0]]["answer"]
    else:
        return None
