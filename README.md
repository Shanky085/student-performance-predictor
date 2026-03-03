# 📊 Student Performance Predictor

A Machine Learning regression project that predicts student final scores based on study hours, attendance percentage, and previous performance.

This project demonstrates:
- Linear Regression modeling
- Model evaluation using R² score
- Flask web deployment
- Bootstrap UI integration
- Prediction logging
- Docker containerization

---

## 🚀 Features

- 📈 Linear Regression model using scikit-learn  
- 📊 Live Model R² Score display  
- 🧮 Interactive prediction form  
- 🗂 Prediction history logging (CSV)  
- 🐳 Fully Dockerized application  

---

## 🧠 Tech Stack

- Python 3.11
- scikit-learn
- pandas
- Flask
- Bootstrap
- Docker

---

## 📂 Project Structure
student-performance-predictor/
│
├── app.py
├── student_predictor.py
├── student_model.pkl
├── student_data.csv
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md



## ▶️ Run Locally (Without Docker)

1. Create virtual environment:
py -3.11 -m venv venv
venv\Scripts\activate

2. Install dependencies:
pip install -r requirements.txt

3. Run:
python app.py

4. Open browser:
http://127.0.0.1:5000

---

## 🐳 Run Using Docker

Build image:
docker build -t student-predictor .


Run container:
docker run -p 5000:5000 student-predictor

Open:
http://localhost:5000

---

## 📊 Model Performance

- Algorithm: Linear Regression
- Evaluation Metric: R² Score
- Displays model performance directly on the web interface

---

## 🎯 Learning Outcomes

This project demonstrates:
- Supervised Machine Learning workflow
- Model training and evaluation
- Saving and loading trained models
- Web deployment using Flask
- Containerization using Docker

---

## 👨‍💻 Author

Shanky  
B.Tech CSE Student  
