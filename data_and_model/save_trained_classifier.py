import numpy as np
import pandas as pd
from Bio import SeqIO
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
from sklearn.pipeline import Pipeline

# Read the FASTA file and extract sequences
def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as fasta_file:
        lines = fasta_file.readlines()

        sequence = ""
        for line in lines:
            line = line.strip()

            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                sequence = ""
            else:
                sequence += line

        if sequence:
            sequences.append(sequence)

    return sequences

# Read the positive and negative sequence files
positive_file = 'C:/Users/user/Desktop/p53_project/data_and_model/binding_sites.fasta'
negative_file = 'C:/Users/user/Desktop/p53_project/data_and_model/non_binding_sites.fasta'

positive_sequences = read_fasta(positive_file)
negative_sequences = read_fasta(negative_file)

# Create a DataFrame for the sequences, with a label of 1 for positive samples and 0 for negative samples
positive_df = pd.DataFrame({'sequence': positive_sequences, 'label': 1})
negative_df = pd.DataFrame({'sequence': negative_sequences, 'label': 0})

# Combine the positive and negative DataFrames
data = pd.concat([positive_df, negative_df], ignore_index=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['sequence'], data['label'], test_size=0.2, random_state=42)

# Convert the DNA sequences into feature vectors using CountVectorizer
vectorizer = CountVectorizer(analyzer='char', ngram_range=(4, 4))  # Use 4-mers as features
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Build and train the Logistic Regression model
model = LogisticRegression(max_iter=500)  # You can increase the max_iter value here
model.fit(X_train_vectorized, y_train)

# Evaluate the model's performance
y_pred = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

print('Classification Report:')
print(classification_report(y_test, y_pred))

print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# Step 8: Save the entire fitted pipeline using joblib
pipeline = Pipeline([('vectorizer', vectorizer), ('model', model)])
model_filename = 'trained_model.joblib'
joblib.dump(pipeline, model_filename)