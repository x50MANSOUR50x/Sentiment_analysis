# 🎬 Sentiment Analysis: IMDb Movie Reviews

This project is a **streamlit-powered web app** that predicts whether a movie review is **positive** or **negative** using a **Logistic Regression model** trained on the IMDb dataset.

---

## 🚀 Features

- Clean and simple Streamlit web interface
- Preprocessing with NLTK (stopword removal + stemming)
- TF-IDF vectorization with unigrams and bigrams
- Predicts sentiment from user input in real-time
- Uses a pre-trained and saved model (`.pkl`)

---

## 📦 Installation

1. **Clone the repo** or download the files:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Download NLTK resources (first time only):

python
Copy
Edit
import nltk
nltk.download('stopwords')
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
📁 Project Structure
Copy
Edit
📦 sentiment-analysis-app/
├── app.py
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
📊 Model Info
Model: Logistic Regression (Scikit-learn)

Vectorizer: TF-IDF with top 5000 features + bigrams

Dataset: IMDb 50K Movie Reviews

🌐 Deploy to Streamlit Cloud
Push this project to a public GitHub repo

Go to streamlit.io/cloud

Connect your GitHub repo

Deploy and share your app link 🎉

🤝 Credits
Developed by Mohamed Ahmed Mansour
Internship Project – Elevvo



ChatGPT can make
