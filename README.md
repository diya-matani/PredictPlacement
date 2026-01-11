# 🎓 Placement Predictor

<p align = center><img src = "https://user-images.githubusercontent.com/74038190/226190894-18e959ba-d458-4a94-ac44-790190f2a947.gif" />


>*“From Jupyter experiments to a live Streamlit app — what a ride!”*


---

## 🤖Introduction
So, this is my first project using StreamLit service in python used for deploying my machine learning model which is also my first built model.

---

## 📖 About the Project

This repo contains a **Placement Predictor** web app built with **Streamlit**.  
Given a student’s academic profile, it predicts whether they will get placed in campus recruitment.

Under the hood:
- 📦 Preprocessing + Model are wrapped in a single `sklearn` **Pipeline**
- 📊 Logistic Regression with `class_weight='balanced'` powers the prediction
- ✨ Custom dark-themed UI with purple-orange gradient

---

## 🔍 Model Journey & Challenges

1. **Initial Prototype in Jupyter Notebook**
   - Tried an **SVM (linear kernel)** — it actually outperformed Logistic Regression in terms of accuracy.
   - However:
     - SVM with `probability=True` is **slow**
     - It returned **extreme probability scores (0% or 100%)**
     - Couldn’t interpret middle confidence scores reliably

2. **Switch to Logistic Regression**
   - Provided smoother and **more calibrated probabilities**
   - Supported `class_weight='balanced'` to handle imbalance in “Placed” vs “Not Placed”
   - More compatible with web deployment due to lighter model size and better performance on new inputs

3. **Streamlit Integration**
   - Built a three-column form layout
   - Used `@st.cache_resource` instead of deprecated `@st.cache`
   - Removed aggressive outlier filtering to keep students with high scores (90%+)

4. **Deployment Woes & Wins**
   - Resolved local Python path issues using: `python -m streamlit run streamlit_app.py`
   - Fixed CSS for dark mode gradient
   - Resized header banner to avoid pushing the UI down
   - Successfully deployed to Streamlit Cloud 🎉

---

## ✨ Features

- 📈 End-to-end ML pipeline using `scikit-learn`
- 🧠 Predicts placement based on academic background
- 🎨 Dark-themed UI with modern styling
- 🔁 Cached model for fast prediction
- 🚀 Deployed app ready for real-world use

---

## 🛠️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/placement-predictor.git
   cd placement-predictor
   ```

2. **(Optional) Setup a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate     # macOS/Linux
   venv\Scripts\activate        # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚦 Usage

1. **Train or retrain the model**
   ```bash
   python train_and_save_model.py
   ```
   This generates `placement_pipeline.pkl`.

2. **Launch the Streamlit app**
   ```bash
   python -m streamlit run streamlit_app.py
   ```

3. **Visit** `http://localhost:8501` in your browser.

---

## 🌐 Deployment

This project is deployed on **Streamlit Cloud**  
👉 [**Live Demo**](https://placement-prediction-using-machine-learning-algorithms-cmy2s3s.streamlit.app/)

To deploy it yourself:

1. Push this repo to GitHub  
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) → **New app**  
3. Choose your repo → Main file: `streamlit_app.py` → Deploy  
4. Done. 🎉

![Success Kid](https://media.giphy.com/media/111ebonMs90YLu/giphy.gif)

---

>***“In the end, it’s not just about predictions… it’s about the journey of building, breaking, fixing, and learning.”*** 🚀


