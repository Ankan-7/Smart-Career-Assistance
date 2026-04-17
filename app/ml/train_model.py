import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Load dataset
df = pd.read_csv("data/career_dataset.csv")

# Features and labels
X = df["skills"]
y = df["career"]

# Vectorization
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X_vectorized = vectorizer.fit_transform(X)

# Model training
model = LogisticRegression()
model.fit(X_vectorized, y)

# Save model
with open("app/ml/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("app/ml/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model trained and saved ")