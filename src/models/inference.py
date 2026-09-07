"""
Inference module for predicting an API's category from its name and description.

Uses the final selected pipeline: SentenceTransformer('all-mpnet-base-v2')
embeddings + LinearSVC(C=0.5) classifier.
"""

import joblib
from sentence_transformers import SentenceTransformer

MODEL_PATH = "artifacts/category_classifier_final.pkl"
EMBEDDER_PATH = "artifacts/sentence_embedder"

model = joblib.load(MODEL_PATH)
embedder = SentenceTransformer(EMBEDDER_PATH)


def predict_api_category(name: str, description: str) -> str:
    """
    Combines name and description, computes an mpnet sentence embedding,
    and returns the predicted API category string directly.
    """
    text_input = f"{name} {description}".strip()
    embedding = embedder.encode([text_input])
    prediction = model.predict(embedding)[0]
    return prediction


if __name__ == "__main__":
    result = predict_api_category(
        "Stripe", "Payment processing API for internet businesses"
    )
    print(f"Predicted category: {result}")