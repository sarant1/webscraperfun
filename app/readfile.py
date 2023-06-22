import pandas as pd
from cleaners import *


df = pd.read_csv('output.csv', sep=',', header=None, names=['Job ID', 'Job Title', 'Company Location', 'Company Name', 'Job Salary', 'Date Posted'])


df.loc[9]['Job Salary'] = cleanSalary(df.loc[9]['Job Salary'])

df['Job Salary'] = df['Job Salary'].apply(cleanSalary)

df.to_csv('updated_output.csv', index=False)

# print(df.to_string())