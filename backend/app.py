from flask import Flask, request, jsonify
from flask_cors import CORS

from rag_engine import create_vector_db

app = Flask(__name__)
CORS(app)

# Load vector database once
vector_db = create_vector_db()


@app.route("/")
def home():
    return "SHL Assessment Recommendation API is running"


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"error": "Query is required"}), 400

    # Retrieve relevant assessments
    docs = vector_db.similarity_search(query, k=3)

    recommendations = []
    explanation_lines = []

    for doc in docs:
        recommendations.append({
            "assessment_name": doc.metadata["assessment_name"],
            "duration": doc.metadata["duration"],
            "test_type": doc.metadata["test_type"],
            "url": doc.metadata["url"]
        })

        explanation_lines.append(
            f"- {doc.metadata['assessment_name']} is relevant based on required skills and assessment type."
        )

    explanation = (
        "Based on the given job requirement, the following SHL assessments are recommended:\n\n"
        + "\n".join(explanation_lines)
    )

    return jsonify({
        "answer": explanation,
        "recommendations": recommendations
    })


if __name__ == "__main__":
    app.run(debug=True)
