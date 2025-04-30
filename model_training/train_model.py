import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import joblib

# Load and clean data
df = pd.read_csv("../data/fake_job_postings.csv")
df = df[df["fraudulent"].isin([0, 1])]
df.fillna("", inplace=True)

# Combine fields
df["text"] = df["title"].str.lower() + " " + df["description"].str.lower()
X = df["text"]
y = df["fraudulent"]

# TF-IDF
vectorizer = TfidfVectorizer(max_features=1000, stop_words="english")
X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, stratify=y, test_size=0.2, random_state=42)

# Apply SMOTE
smote = SMOTE(sampling_strategy=0.5, random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Train model
clf = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42)
clf.fit(X_train_res, y_train_res)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model & vectorizer
joblib.dump(clf, "../backend/model/fraud_model.pkl")
joblib.dump(vectorizer, "../backend/model/tfidf_vectorizer.pkl")
