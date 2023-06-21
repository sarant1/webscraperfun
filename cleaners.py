import re


def cleanSalary(salary):
    match = re.search(r'\$(\d[\d,]*)', salary)
    if match:
        min_salary = match.group(1).replace(',', '')
        min_salary = '${:,.2f}'.format(float(min_salary))
        return min_salary