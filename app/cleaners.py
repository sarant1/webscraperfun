import re


# ~1750 hours per year worked

def cleanSalary(salary):

    # Looking for hourly or yearly in the string
    hourly_rate = re.search(r'hour', salary)
    yearly_rate = re.search(r'year', salary)

    # Looking for the salary amounts hourly/yearly
    match_hourly = re.search(r"(?<=\$)\d.", salary)
    match_yearly = re.search(r'\$(\d[\d,]*)', salary)

    if yearly_rate:
        salary = match_yearly.group(1).replace(',', '')
        salary = '${:,.2f}'.format(float(salary))
    elif hourly_rate:
        salary = match_hourly.group(0)
        salary = '${:,.2f}'.format(float(salary) * 1750)
    return salary 



