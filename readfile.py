import pandas as pd

df = pd.read_csv('output.csv', sep=',', header=None, names=['Job ID', 'Job Title', 'Company Location', 'Company Name', 'Job Salary', 'Date Posted'])

print(df.to_string())