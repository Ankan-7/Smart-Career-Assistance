import pickle


# Load model and vectorizer
with open("app/ml/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("app/ml/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def predict_career(user_skills: str):

    X = vectorizer.transform([user_skills])
    probabilities = model.predict_proba(X)[0]
    classes = model.classes_

    results = []

    for i, prob in enumerate(probabilities):
        results.append({
            "career": classes[i],
            "confidence": round(float(prob), 2)
        })

    # Sort by confidence
    results = sorted(results, key=lambda x: x["confidence"], reverse=True)

    return results[:3]  # top 3