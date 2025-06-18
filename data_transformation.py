# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Load the Dataset
df = pd.read_csv("Medicaldataset.csv")  # Replace with your actual dataset file name
print("Original Data:\n", df.head())  # Display first few rows

# 2. Handle Missing Values
df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)  # Fill missing numerical values with mean

# Fill categorical missing values with the most common value (mode)
for column in df.select_dtypes(include=['object']).columns:  
    df[column].fillna(df[column].mode()[0], inplace=True)

# 3. Encode Categorical Data (Convert Gender and Result)
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Result'] = df['Result'].map({'Normal': 0, 'High Risk': 1})

# 4. Normalize/Scale Numerical Features
scaler = StandardScaler()
df[['Heart rate', 'Systolic blood pressure', 'Diastolic blood pressure', 'Blood sugar', 'CK-MB', 'Troponin']] = \
    scaler.fit_transform(df[['Heart rate', 'Systolic blood pressure', 'Diastolic blood pressure', 'Blood sugar', 'CK-MB', 'Troponin']])

# 5. Create Age Groups for Analysis
df['Age Group'] = pd.cut(df['Age'], bins=[0, 40, 55, 70, 100], labels=['Young', 'Middle-Aged', 'Older', 'Elderly'])

# 6. Group Data for Analysis
grouped_data = df.groupby('Age Group').agg({'Heart rate': 'mean', 'Systolic blood pressure': 'mean', 'Blood sugar': 'mean'})
print("\nGrouped Data:\n", grouped_data)

# 7. Save the Transformed Dataset
df.to_csv("transformed_dataset.csv", index=False)

print("Transformed dataset saved as 'transformed_dataset.csv'.")