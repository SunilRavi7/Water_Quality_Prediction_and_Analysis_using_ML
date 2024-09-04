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
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

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

---

## **⚙️ Installation**

To get started with the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SunilRavi7/Water_Quality_Prediction_and_Analysis_using_ML.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd Water_Quality_Prediction_and_Analysis_using_ML
    ```
3. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## **🚀 Usage**

To run the application, follow these steps:

1. **Ensure you are in the project directory**:
    ```bash
    cd Water_Quality_Prediction_and_Analysis_using_ML
    ```
2. **Start the Flask application**:
    ```bash
    flask run
    ```
3. **Open your web browser** and go to `http://127.0.0.1:5000/` to access the web interface.

4. **Input the chemical properties** of water into the provided fields and hit "Predict" to see if the water is safe for drinking.

---

## **📊 Results**

The model will output whether the water is **safe** or **unsafe** for drinking based on the input parameters. The results are displayed on the web interface along with an explanation of the predicted outcome.

---

## **📂 Project Structure**

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


---

## **🤝 Contributing**

We welcome contributions to this project. If you have any improvements, please submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

## **📝 License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## **📧 Contact**

For any questions or inquiries, feel free to contact me:

- **Email**: [sunilr31r@gmail.com](mailto:sunilr31r@gmail.com)
- **LinkedIn**: [Sunil R](https://www.linkedin.com/in/sunilravi7)
