# p53_binding_sites
Project Name: p53 Binding Site Predictor - Educational Project 

Overview
This project focuses on predicting DNA sequence binding sites using a Logistic Regression model, with a specific emphasis on the TP53 gene (p53). The model achieves an impressive accuracy of 93% in distinguishing binding sites from non-binding sites.
Features
* DNA sequences are extracted from FASTA files and labeled as positive or negative samples.
* The sequences are transformed into feature vectors using the CountVectorizer, using 4-mers as features.
* A Logistic Regression model is built and trained on the feature vectors.
* Flask is used to create a web application for predicting binding sites based on user input sequences.

Disclaimer:
It is essential to emphasize that this project is purely for educational purposes and should not be utilized or deployed in real-world scenarios.

Data Sources:

Binding Sites Data: Binding site data for p53 was obtained from the JASPAR database at http://jaspar.genereg.net/.
Non-Binding Sites Data: Non-binding site data for p53 was obtained from the National Center for Biotechnology Information (NCBI) at https://www.ncbi.nlm.nih.gov/.

Installation:

Clone the repository: git clone https://github.com/shervindokhtshamsi/p53_binding_sites.git
Navigate to the project directory: cd p53-binding-predictor
Install dependencies: pip install -r requirements.txt
Run the application: python app.py

Usage:

Access the web interface by opening your browser and visiting http://127.0.0.1:5000/.
Input a DNA sequence into the provided textarea.
Click the "Predict" button to view the prediction result.

Contributing:

While practical contributions are not sought due to the educational nature of this project, engaging in discussions and sharing insights is welcomed.

