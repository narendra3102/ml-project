#end to end ml project
🎓 Student Performance Prediction (Flask + ML)
📌 Project Overview

This project predicts student performance (math score) based on various input features such as:

Gender

Race/Ethnicity

Parental Level of Education

Lunch Type

Test Preparation Course

Reading Score

Writing Score

It is built using Python, Flask, scikit-learn, and HTML templates for the frontend.

⚙️ Tech Stack

Python 3.9+

Flask (Web Framework)

scikit-learn (ML Model Training & Prediction)

pandas, numpy (Data Processing)

HTML/CSS (Jinja2 templates) for UI

Pickle for saving models

📂 Project Structure
ml project/
│
├── app.py                         # Flask main application
├── train.py                       # Script to train & save model
├── requirements.txt                # Required dependencies
│
├── src/
│   ├── pipeline/
│   │   ├── model_trainer.py        # Model training logic
│   │   ├── predict_pipeline.py     # Prediction pipeline
│   │   ├── utils.py                # Helper functions
│   │   └── exception.py            # Custom exception handling
│
├── artifacts/                      # Saved model & preprocessor
│   ├── model.pkl
│   ├── preprocessor.pkl
│
├── templates/                      # Frontend templates
│   ├── index.html
│   └── home.html
│
├── notebook/                       # Data & experiments
│   └── data/stud.csv
│
└── README.md                       # Project documentation

🚀 How to Run the Project
1. Clone the repo
git clone <your-repo-link>
cd ml project

2. Create a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Linux/Mac

3. Install dependencies
pip install -r requirements.txt

4. Train the model
python train.py


This will generate:

artifacts/model.pkl

artifacts/preprocessor.pkl

5. Run the Flask app
python app.py


Go to:
👉 http://127.0.0.1:5000

🧪 Example Input

Gender: male

Race/Ethnicity: group B

Parental Level of Education: bachelor's degree

Lunch: standard

Test Preparation Course: completed

Reading Score: 72

Writing Score: 74
