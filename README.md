# 🚗 Vehicle CO2 Emissions Predictor

An interactive web application built with **Streamlit** that uses a **Multiple Linear Regression** machine learning model to estimate a vehicle's carbon dioxide ($CO_2$) emissions. 

Users can tune various engine specifications and fuel consumption metrics in real-time and compute the estimated emissions with a single click.

Live Demo: *[https://co2-emissions-predictor-app-2-engr-nauman.streamlit.app/]*

---

## 🌟 Features

* **Interactive User Interface:** Simple sliders and numeric inputs via the Streamlit sidebar.
* **On-Demand Computation:** A primary calculation button prevents unnecessary real-time calculations while the user is actively adjusting inputs.
* **Smart Threshold Indicators:** Highlights whether the calculated emissions are low, moderate, or heavy based on standard carbon emission benchmarks.
* **Robust Backend:** Powered by a pre-trained Scikit-Learn Multiple Linear Regression pipeline.

---

## 🛠️ Project Structure

```text
├── app.py                  # The main Streamlit web application script
├── co2_emission_model.pkl  # Pre-trained Scikit-Learn Linear Regression model
├── requirements.txt        # Python library dependencies for deployment
└── README.md               # Project documentation
```

---

## 📦 Features & Input Variables

The machine learning model accepts six critical vehicle specifications to predict emissions ($g/km$):

| Feature Name | Component Type | Value Range |
| :--- | :--- | :--- |
| **Engine Size (L)** | Sidebar Slider | 0.9L - 8.4L |
| **Cylinders** | Sidebar Slider | 3 - 16 |
| **Fuel Consumption City** | Numeric Input | 4.0 - 31.0 L/100 km |
| **Fuel Consumption Hwy** | Numeric Input | 4.0 - 21.0 L/100 km |
| **Fuel Consumption Comb** | Numeric Input | 4.0 - 27.0 L/100 km |
| **Fuel Consumption Comb (mpg)**| Sidebar Slider | 11 - 69 mpg |

---

## 🚀 Local Installation & Setup

To run this application locally on your computer, follow these quick steps:

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```
> Your local browser should automatically open to `http://localhost:8501`.

---

## ☁️ Deployment

This project is configured for seamless deployment on **Streamlit Community Cloud**:

1. Push your updated code, model pickle file, and `requirements.txt` to GitHub.
2. Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **New App**, select your repository and the `main` branch, and point the main file path to `app.py`.
4. Click **Deploy**!

---

## 🧠 Model Details

The core machine learning engine is a **Multiple Linear Regression** model. The model calculates the target output using the standard linear equation:

$$y = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n$$

Where:
* $y$ is the predicted $CO_2$ emission ($g/km$).
* $\beta_0$ is the intercept value.
* $\beta_n$ represents the feature coefficients optimized during training in Google Colab.
* $x_n$ represents the inputs provided by the user via the app sidebar.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
