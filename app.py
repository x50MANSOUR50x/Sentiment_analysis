import streamlit as st
import joblib
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load model and vectorizer
model = joblib.load(r'Models trained\sentiment_model.pkl')
vectorizer = joblib.load(r'Models trained\tfidf_vectorizer.pkl')

# Text cleaning function
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    text = re.sub(r'<.*?>', '', text.lower())
    text = re.sub(r'[^a-z\s]', '', text)
    words = [stemmer.stem(word) for word in text.split() if word not in stop_words]
    return re.sub(r'\s+', ' ', " ".join(words)).strip()

# Streamlit UI
st.title("🎬 Sentiment Analysis: IMDb Movie Reviews")
st.write("Enter a movie review and I'll tell you if it's positive or negative.")

user_input = st.text_area("📝 Your Review:", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        pred = model.predict(vec)[0]
        sentiment = "✅ Positive" if pred == 1 else "❌ Negative"
        st.subheader("Prediction:")
        st.success(sentiment)
