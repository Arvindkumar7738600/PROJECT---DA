import pandas as pd


df = pd.read_csv('customer_shopping_behavior.csv')  # Load data from a CSV file into a DataFrame

df.head() # Display the first few rows of the DataFrame

df.info() # Get a summary of the DataFrame including data types and non-null counts

df.describe(include='all') # Generate descriptive statistics for numerical columns

df.isnull().sum() # Check for missing values in each column

