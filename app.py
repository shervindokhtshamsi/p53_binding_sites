import os
import webbrowser
from flask import Flask, render_template, request
import subprocess
import joblib

app = Flask(__name__)

# Get the absolute path to the directory containing the script
current_dir = os.path.dirname(os.path.abspath(__file__))
model_filename = os.path.join(current_dir, 'trained_model.joblib')

# Load the trained model and CountVectorizer
pipeline = joblib.load(model_filename)
vectorizer = pipeline['vectorizer']
model = pipeline['model']

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        sequence = request.form['sequence']
        if sequence:
            vectorized_sequence = vectorizer.transform([sequence])
            prediction = model.predict(vectorized_sequence)[0]
            result = "Binding Site" if prediction == 1 else "Not a Binding Site"
            return render_template('result.html', sequence=sequence, result=result)


@app.route('/run_installer', methods=['GET'])
def run_installer():
    subprocess.run(['install_dependencies.bat'], shell=True)
    return "Dependencies installed. You can now run the application."

if __name__ == '__main__':
    # Open the default web browser automatically when the app starts
    webbrowser.open('http://127.0.0.1:5000/')

    # Start the Flask app
    app.run(debug=False, use_reloader=False)
