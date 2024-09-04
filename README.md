# **🚰 Water Quality Prediction and Analysis using ML**

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## **📄 Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

---

## **🌟 Project Overview**

This project focuses on predicting water potability using **machine learning** techniques. It classifies water samples as **safe** or **unsafe** for drinking based on various chemical properties. Key features used in this model include:

- **pH Level**: Indicates the acidity or alkalinity of water.
- **Hardness**: Measures the concentration of calcium and magnesium ions.
- **Solids**: Represents the total dissolved solids in water.
- **Chloramines**: Amount of disinfectant used to treat drinking water.
- **Sulfate**: A chemical compound found naturally in some drinking water supplies.
- **Conductivity**: Indicates the water's capability to pass electrical flow.
- **Organic Carbon**: Amount of carbon found in organic compounds in water.
- **Trihalomethanes**: A by-product of chlorine disinfection of water.
- **Turbidity**: Measure of the cloudiness or haziness in water.

The model integrates various classifiers to enhance prediction accuracy, ensuring reliable water safety analysis.

---

## **✨ Features**

- **Machine Learning Models**: Combines multiple classifiers for accurate prediction.
- **Real-time Prediction**: Allows users to input data for instant prediction.
- **Web Interface**: Developed using **Flask** for an easy-to-use web application.
- **Data Visualization**: Graphical representations of predictions and feature importances.
- **Scalable**: The application can be easily extended for larger datasets and additional features.

---

## **🛠️ Requirements**

Make sure you have the following dependencies installed:

```bash
- Python 3.10
- Flask 2.3.2
- scikit-learn 1.3.0
- Pandas 2.0.3
- Numpy 1.25.0
- Matplotlib 3.7.2

Water_Quality_Prediction_and_Analysis_using_ML/
│
├── static/
│   ├── css/
│   │   └── styles.css  # CSS for styling
│   └── js/
│       └── script.js   # Optional JavaScript
│
├── templates/
│   └── index.html      # HTML template for Flask
│
├── water_potability.csv  # Dataset
├── model.pkl            # Trained model
├── app.py               # Flask app
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation


🚀 Usage
To run the application, follow these steps:

Ensure you are in the project directory:

bash
Copy code
cd Water_Quality_Prediction_and_Analysis_using_ML
Start the Flask application:

bash
Copy code
flask run
Open your web browser and go to http://127.0.0.1:5000/ to access the web interface.

Input the chemical properties of water into the provided fields and hit "Predict" to see if the water is safe for drinking.
