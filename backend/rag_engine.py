import pandas as pd

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_vector_db():
    # 1️⃣ Load SHL catalog
    df = pd.read_csv("data/SHL_catalog.csv")

    # 2️⃣ Combine useful columns into text
    df["combined_text"] = (
        "Assessment Name: " + df["Assessment Name"].astype(str) + ". "
        "Description: " + df["Description"].astype(str) + ". "
        "Skills: " + df["Skills"].astype(str) + ". "
        "Test Type: " + df["Test Type"].astype(str) + ". "
        "Duration: " + df["Duration"].astype(str) + ". "
        "Remote Testing Support: " + df["Remote Testing Support"].astype(str)
    )

    # 3️⃣ Convert rows to Documents
    documents = []
    for i, row in df.iterrows():
        print(f"Preparing document {i+1}/{len(df)}")
        documents.append(
            Document(
                page_content=row["combined_text"],
                metadata={
                    "assessment_name": row["Assessment Name"],
                    "url": row["URL"],
                    "duration": row["Duration"],
                    "test_type": row["Test Type"],
                    "remote_support": row["Remote Testing Support"]
                }
            )
        )

    # 4️⃣ FREE embeddings (NO API, NO QUOTA)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 5️⃣ Create FAISS vector DB
    vector_db = FAISS.from_documents(documents, embeddings)

    return vector_db


# 🔹 Test retrieval
if __name__ == "__main__":
    db = create_vector_db()
    results = db.similarity_search(
        "Hiring a data analyst with numerical reasoning skills",
        k=3
    )

    for r in results:
        print("-----")
        print("Assessment:", r.metadata["assessment_name"])
