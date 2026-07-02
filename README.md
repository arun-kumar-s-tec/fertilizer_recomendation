# 🌱 Fertilizer Recommendation System using Decision Tree

## 📌 Project Overview

The **Fertilizer Recommendation System** is a machine learning web application that predicts the most suitable fertilizer based on soil nutrients, environmental conditions, and crop type. The project uses a **Decision Tree Classifier** trained on agricultural data and provides recommendations through an interactive **Streamlit** web interface.

This system aims to assist farmers and agricultural professionals in making data-driven fertilizer decisions, helping improve crop productivity and optimize fertilizer usage.


---

## 🚀 Features

* Predicts the most suitable fertilizer for a given crop and soil condition.
* Interactive and user-friendly Streamlit interface.
* Uses a supervised machine learning approach.
* Performs automatic encoding of crop names and fertilizer labels.
* Supports real-time predictions.
* Model serialization using Pickle/Joblib for deployment.

  Live Working : Click Here(https://fertilizerrecomendationdemo.streamlit.app/)

---

## 📊 Dataset Description

The dataset contains information about:

| Feature     | Description                |
| ----------- | -------------------------- |
| N           | Nitrogen content in soil   |
| P           | Phosphorus content in soil |
| K           | Potassium content in soil  |
| temperature | Temperature in °C          |
| humidity    | Relative humidity (%)      |
| ph          | Soil pH value              |
| rainfall    | Rainfall in mm             |
| label       | Crop name                  |
| fertilizer  | Recommended fertilizer     |

### Target Variable

```text
fertilizer
```

---

## 🛠️ Machine Learning Workflow

The project follows a complete machine learning pipeline:

```text
Problem Definition
        ↓
Data Collection
        ↓
Exploratory Data Analysis
        ↓
Outlier Treatment
        ↓
Feature Selection
        ↓
Data Encoding
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Cross Validation
        ↓
Model Selection
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Model Deployment
```

---

## 🔍 Exploratory Data Analysis

The following preprocessing steps were performed:

* Checked for missing values.
* Checked for duplicate records.
* Performed univariate analysis.
* Detected outliers using the IQR method.
* Applied IQR-based Winsorization to cap extreme values.
* Removed data leakage columns:

  * `N_status`
  * `P_status`
  * `K_status`
  * `recommendation_note`

---

## 🤖 Models Evaluated

Several machine learning algorithms were compared:

| Model                  | Accuracy |
| ---------------------- | -------- |
| Logistic Regression    | 86.14%   |
| Decision Tree          | 100.00%  |
| Random Forest          | 100.00%  |
| K-Nearest Neighbors    | 88.18%   |
| Support Vector Machine | 87.73%   |

### Cross Validation Results

| Model         | Mean CV Accuracy |
| ------------- | ---------------- |
| Decision Tree | 97.32%           |
| Random Forest | 96.23%           |

After cross-validation analysis, the **Decision Tree Classifier** was selected as the final model due to its superior performance.

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

---

## 📁 Project Structure

```text
fertilizer_recommendation/
│
├── app.py
├── decision_tree_model.pkl
├── crop_encoder.pkl
├── fertilizer_encoder.pkl
├── requirements.txt
├── README.md
└── dataset/
    └── crop_fertilizer_recommendation_dataset.csv
```

---

## 💾 Model Serialization

The following files were saved for deployment:

```text
decision_tree_model.pkl
crop_encoder.pkl
fertilizer_encoder.pkl
```

---

## 🖥️ Running the Application Locally

### Clone the repository

```bash
git clone <your-github-repository-url>
cd fertilizer_recommendation
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

The application will start on:

```text
http://localhost:8501
```

---

## 🧪 Example Input

| Feature     | Value |
| ----------- | ----- |
| Crop        | Rice  |
| N           | 90    |
| P           | 42    |
| K           | 43    |
| Temperature | 20.8  |
| Humidity    | 82    |
| pH          | 6.5   |
| Rainfall    | 202   |

### Predicted Output

```text
Recommended Fertilizer: Urea
```

---

## 📈 Future Improvements

* Add fertilizer dosage recommendations.
* Include soil image analysis.
* Integrate weather APIs.
* Add fertilizer cost optimization.
* Deploy using cloud services.
* Build a mobile-friendly interface.

---

## 🎯 Conclusion

This project demonstrates the application of machine learning in precision agriculture by recommending fertilizers based on soil and environmental conditions. The Decision Tree model achieved excellent performance and was successfully integrated into an interactive Streamlit application for real-time predictions.

---

## 👨‍💻 Author

**Arun Kumar**

Machine Learning Project: Fertilizer Recommendation System using Decision Tree and Streamlit.
