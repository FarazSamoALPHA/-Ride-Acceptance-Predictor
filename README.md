# 🚖 Ride Acceptance Predictor

A Machine Learning web application built with **Python**, **Streamlit**, and **Scikit-learn** that predicts whether a driver will accept or reject a customer's offered ride fare based on ride details.

---

# 📌 Project Overview

The Ride Acceptance Predictor is an intelligent pricing assistant that estimates whether a driver is likely to accept a customer's offered fare. The prediction is made using a trained Machine Learning classification model.

The user enters ride information such as travel distance, offered price, and time of day. The application analyzes these inputs and predicts the driver's response along with the probability of acceptance.

This project demonstrates how Machine Learning can be used in ride-hailing and transportation systems to improve pricing decisions.

---

# 🎯 Objective

The goal of this project is to help passengers understand whether their offered fare is likely to be accepted before requesting a ride.

---

# ✨ Features

* 🚖 Predict driver acceptance or rejection
* 💰 Custom fare price input
* 📍 Distance-based prediction
* 🕒 Time of day consideration
* 📊 Probability score for prediction
* ⚡ Real-time prediction using Machine Learning
* 🖥 Interactive Streamlit interface

---

# 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Joblib

---

# 🤖 Machine Learning Model

The project uses a trained classification model stored in **ride_acceptance_clf.pkl**.

Feature names are loaded from **clf_features.pkl** to ensure the prediction input matches the model's training format.

---

# 📂 Project Structure

```text
Ride-Acceptance-Predictor/
│── app.py
│── ride_acceptance_clf.pkl
│── clf_features.pkl
│── requirements.txt
└── README.md
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Ride-Acceptance-Predictor.git
```

Move into the project folder:

```bash
cd Ride-Acceptance-Predictor
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# ▶ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your default web browser.

---

# 📖 How It Works

1. Enter the ride distance.
2. Select the hour of the day.
3. Enter your offered ride price.
4. The trained Machine Learning model analyzes the inputs.
5. The application predicts whether the driver is likely to **Accept** or **Reject** the offer.
6. A probability score is also displayed for better understanding.

---

# 📊 Input Features

The model uses the following information:

* Distance (km)
* Offered Price
* Hour of the Day

---

# 📈 Output

The application displays:

* ✅ Driver Accept
* ❌ Driver Reject
* 📊 Acceptance Probability

---

# 📦 Required Files

* app.py
* ride_acceptance_clf.pkl
* clf_features.pkl
* requirements.txt
* README.md

---

# 🚀 Future Improvements

* Dynamic pricing recommendation
* Google Maps API integration
* Traffic condition analysis
* Weather-based prediction
* Interactive charts and analytics
* Mobile-friendly interface
* Cloud deployment

---

# 👨‍💻 Author

Developed using **Python**, **Streamlit**, and **Machine Learning** for educational purposes and intelligent ride fare prediction.

---

# 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and improve it for educational and research purposes.
