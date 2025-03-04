# **Thyroid Cancer Risk Predictor** <br> 
Early Detection of Thyroid Cancer Using Machine Learning

## **Overview** <br>
Thyroid cancer is a critical public health concern, and early detection significantly improves prognosis, enabling timely intervention and better treatment outcomes. Existing clinical models rely on binary risk classifications, which may oversimplify complex medical relationships, leading to misdiagnoses.
This project leverages machine learning algorithms to predict thyroid cancer risk based on structured patient data, aiming to assist primary care physicians (PCPs), endocrinologists, and even self-assessing individuals in identifying high-risk patients for further evaluation.

## **Objective** <br>
The goal of this project is to develop a cost-effective, data-driven AI screening tool that can be integrated into primary care settings and endocrinology practices to enhance early detection and improve diagnostic accuracy. Unlike traditional risk assessment models, this approach allows machine learning to automatically discern complex, non-linear patterns in patient data, reducing false negatives and improving overall screening efficiency.

## **Data & Methodology** <br>
The model is trained on structured patient data sourced from Kaggle repositories. It considers a range of demographic, clinical, and laboratory markers to determine cancer risk:

### **Features Used**

| Feature Category        | Included Data Points                                                                                                         |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------| 
 Demographics & History   | Age, Country of Origin, Ethnicity, Family History, Radiation Exposure, Iodine Deficiency, Smoking History, Obesity, Diabetes 
 Clinical & Lab Markers   | TSH, T3, T4 Levels, Nodule Sizes                                                                                             |
 Outcome Variable         |Thyroid Cancer Diagnosis (Yes/No)

### **Machine Learning Models Used** <br>
To optimize predictive performance, multiple classification algorithms were evaluated:
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree Classifier 
- Random Forest Classifier 
- AdaBoost Classifier 
- Gradient Boosting Classifier 
- Extra Trees Classifier 
- XGBoost Classifier 
- Gaussian Naïve Bayes (GaussianNB)

### **Model Evaluation Metrics** <br>
To ensure high diagnostic reliability, the models are assessed using:
- Accuracy – Overall correctness of predictions
- Sensitivity (Recall) – Ability to correctly identify thyroid cancer cases
- Specificity – Ability to correctly classify non-cancer cases
- Precision – Percentage of predicted positive cases that are actually cancerous
- F1-Score – Balances false positives and false negatives
- AUC-ROC (Area Under Curve - Receiver Operating Characteristic) – Evaluates classifier performance across thresholds

### **Current Best Model Performance:**
- Accuracy: [value]
- Precision: [value]
- Recall: [value]
- F1-Score: [value]

### **Key Benefits & Impact**
- Early Detection: Enables earlier interventions, improving prognosis 
- AI-Driven Accuracy: Identifies complex risk factors beyond traditional binary classification 
- Clinical Integration: Designed for PCPs, endocrinologists, and patient self-screening 
- Scalable & Adaptable: Can be deployed in hospitals, telemedicine platforms, and self-assessment apps

### **Tech Stack & Dependencies** <br>
The project is built using a Python-based ML pipeline with the following frameworks & tools:
- Machine Learning: TensorFlow, Scikit-learn, XGBoost, LightGBM
- Deep Learning for Tabular Data: Tab-Transformer-PyTorch, tsai, PyTorch-Tabular, Torch, Skorch
- Data Processing & Visualization: Pandas, Matplotlib, Seaborn, PyArrow, Category-Encoders
- Deployment (Planned): Flask API, Docker, Kubernetes

## How to Install & Run the Project
#### Clone the Repository

`git clone https://github.com/rajeshkbutta/thyroid_risk_prediction`<br>
`cd thyroid_risk_prediction`

#### Install Dependencies
`pip install -r requirements.txt`

#### Run the Model
`python train_model.py`

#### Evaluate the Model
`python evaluate.py`

## Future Improvements
- Tabular Transformers Integration – Improve performance using deep learning techniques
- Flask API Development – Deploy the model as a web service for easy integration 
- Docker & Kubernetes Integration – Enable scalable deployment in cloud environments 
- Hyperparameter Optimization – Further tuning of ML models for enhanced accuracy

## Contributing
- Contributions are welcome! If you’d like to improve the model or add new features, feel free to submit a pull request. 
- Contact Me: rajeshkbuttaj@gmail.com
- If you find this project helpful, please give it a star!

