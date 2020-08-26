# Importing essential libraries
import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

# Loading the dataset
diabetes = pd.read_csv('diabetes_data_upload.csv')

# Change column names: replace spaces with underscores
diabetes.rename(columns={'sudden weight loss': 'sudden_weight_loss', 'Genital thrush': 'Genital_thrush', 
                         'visual blurring': 'visual_blurring', 'delayed healing': 'delayed_healing', 
                         'partial paresis': 'partial_paresis', 'muscle stiffness': 'muscle_stiffness'}, inplace=True)

# making capitalizing the fisrt letter of each head column 
diabetes.columns = map(lambda x: str(x).capitalize(), diabetes.columns)

#changing data values to integer
change = {'Age':'Age', 'Gender':{'Male':1, 'Female':0}, 'Polyuria':{'Yes':1, 'No':0},       
        'Polydipsia':{'Yes':1, 'No':0}, 'Sudden_weight_loss':{'Yes':1, 'No':0},
          'Weakness':{'Yes':1, 'No':0}, 'Polyphagia':{'Yes':1, 'No':0},
         'Genital_thrush':{'Yes':1, 'No':0}, 'Visual_blurring':{'Yes':1, 'No':0},
          'Itching':{'Yes':1, 'No':0}, 'Irritability':{'Yes':1, 'No':0}, 
          'Delayed_healing':{'Yes':1, 'No':0},'Partial_paresis':{'Yes':1, 'No':0}, 
          'Muscle_stiffness':{'Yes':1, 'No':0}, 'Alopecia':{'Yes':1, 'No':0}, 
          'Obesity':{'Yes':1, 'No':0}, 'Class':{'Positive':1, 'Negative':0}}


for k, v in change.items():
    diabetes[k] = diabetes[k].replace(v)

# Model Building
from sklearn.model_selection import train_test_split
X = diabetes.drop(columns='Class')
y = diabetes['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

  
# Creating Random Forest Model
model = RandomForestClassifier(random_state=50, n_jobs=-1)
pipeline.fit(X_train, y_train)

# Creating a pickle file for the classifier
filename = 'diabetes-prediction-rfc-model.pkl'
pickle.dump(model, open(filename, 'wb'))
