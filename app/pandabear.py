import pandas as pd
from cleaners import *


df = pd.read_csv('updated_output.csv', sep=',', header=None, names=['Job ID', 'Job Title', 'Company Location', 'Company Name', 'Job Salary', 'Days Posted Ago'])

def findTotalSeniorPositions(print_df=False):
    senior_df = df.loc[df['Job Title'].str.contains('Senior|Lead')]
    print("\n\nTOTAL SENIOR POSITIONS: ", senior_df.shape[0])
    if print_df:
        print("\n", senior_df.to_string())
    # return senior_df.shape[0]

def findTotalJuniorPositions(print_df=False):
    junior_df = df.loc[df['Job Title'].str.contains("Junior|Entry Level|Intern")]
    print("\n\nTOTAL JUNIOR POSITIONS: ", junior_df.shape[0])
    if print_df:
        print("\n", junior_df.to_string())
    # return junior_df.shape[0]

def findTotalSecurityPositions(print_df=False):
    security_df = df.loc[df['Job Title'].str.contains("Security")]
    print("\n\nTOTAL SECURITY POSITIONS: ", security_df.shape[0])
    if print_df:
        print("\n", security_df.to_string())
    # return security_df

def cleanData():
    df = pd.read_csv('output.csv', sep=',', header=None, names=['Job ID', 'Job Title', 'Company Location', 'Company Name', 'Job Salary', 'Days Posted Ago'])
    df['Job Salary'] = df['Job Salary'].apply(cleanSalary)
    df['Days Posted Ago'] = df['Days Posted Ago'].apply(cleanDatePosted)
    df.to_csv('updated_output.csv', index=False)

# cleanData()

findTotalSeniorPositions()
findTotalJuniorPositions(print_df=True)
findTotalSecurityPositions(print_df=True)


# print(df.to_string())