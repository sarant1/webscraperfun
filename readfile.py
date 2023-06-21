import pandas as pd
from cleaners import *


df = pd.read_csv('output.csv', sep=',', header=None, names=['Job ID', 'Job Title', 'Company Location', 'Company Name', 'Job Salary', 'Date Posted'])


value = df.loc[0]['Job Salary']
print(cleanSalary(value))
# print(df.to_string())