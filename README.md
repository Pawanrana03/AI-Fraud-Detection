🔐 AI Financial Fraud Detection System

An AI-powered Financial Fraud Detection System built with Python and Machine Learning to identify potentially fraudulent transactions. The project analyzes transaction data, learns patterns from historical data, and predicts whether a transaction is fraudulent or legitimate.

The project also includes a simple Streamlit web application where users can enter transaction details and get a prediction along with the estimated fraud probability.

✨ Features
Financial transaction fraud detection
Machine Learning-based prediction
Fraud probability estimation
Data preprocessing and analysis
Model training and evaluation
Interactive Streamlit web application
Simple and easy-to-use interface

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Streamlit
Jupyter Notebook

📂 Project Structure
AI-Fraud-Detection/
│
├── fapp.py                         # Streamlit application
├── fraud_detection_pipeline.pkl    # Trained ML pipeline
├── AIML dataset.csv                # Dataset
├── fraud_detection.ipynb           # Model development and analysis
├── requirements.txt                # Required libraries
└── README.md                       # Project documentation

⚙️ How It Works

The system follows a simple Machine Learning workflow:

Transaction Data → Preprocessing → ML Pipeline → Prediction → Fraud Probability

Transaction data is collected through the Streamlit interface.
The trained pipeline processes the input data.
The Machine Learning model analyzes the transaction.
The system predicts whether the transaction is fraudulent or legitimate.
The application displays the prediction and estimated fraud probability.
