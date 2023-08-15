# p53_binding_sites
*Project Name:* p53 Binding Site Predictor - Educational Project

*Overview:*
This project focuses on predicting DNA sequence binding sites using a Logistic Regression model, with a specific emphasis on the TP53 gene (p53). The model achieves an impressive accuracy of 93% in distinguishing binding sites from non-binding sites.

To download the executable file, refer to the following link:
https://drive.google.com/drive/folders/1DN1Ylc8SumAKif1OQOwM97fvYqr1ev1V?usp=sharing

*Features:*
- DNA sequences are extracted from FASTA files and labeled as positive or negative samples.
- The sequences are transformed into feature vectors using the CountVectorizer, using 4-mers as features.
- A Logistic Regression model is built and trained on the feature vectors.
- Flask is used to create a web application for predicting binding sites based on user input sequences.

*Disclaimer:*
It is essential to emphasize that this project is purely for educational purposes and should not be utilized or deployed in real-world scenarios.

*Data Sources:*
- Binding Sites Data: Binding site data for p53 was obtained from the JASPAR database at http://jaspar.genereg.net/.
- Non-Binding Sites Data: Non-binding site data for p53 was obtained from the National Center for Biotechnology Information (NCBI) at https://www.ncbi.nlm.nih.gov/.

*Installation:*
1. Clone the repository: `git clone https://github.com/shervindokhtshamsi/p53_binding_sites.git`
2. Navigate to the project directory: `cd p53-binding-predictor`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python app.py`

*Usage:*
1. Access the web interface by opening your browser and visiting http://127.0.0.1:5000/.
2. Input a DNA sequence into the provided textarea.
3. Click the "Predict" button to view the prediction result.

*Running with PyInstaller:*
After downloading the codes and installing the requirements, you can generate an executable using PyInstaller. Detailed instructions are available in the `pyinstaller_command.txt` file.
