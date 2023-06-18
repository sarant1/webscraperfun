from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time
import csv

start_time = time.time()

# find_all returns a resultSet (list of tags)
# find returns a single tag


# Is this bad ting to do ?
url = "https://www.indeed.com/jobs?q=aws+engineer&l=Florida&from=searchOnHP&vjk=52d6942ea02fcc27"

def setFireFoxDriver():
    driver = webdriver.Firefox()
    driver.get(url)
    return driver

def getPageData(driver):
    page_data = driver.page_source
    soup = BeautifulSoup(page_data, 'html.parser')
    # soup = soup.prettify() # This turns soup into string
    return soup

def removeCommas(string):
    return string.replace(',', ' ')

def extractJobId(job):
    div_element = job.find('div', class_='css-1m4cuuf e37uo190')
    if div_element is not None:
        data_jk = div_element.find('a')['data-jk']
        return data_jk
    else:
        return None


def extractDataPosted(job):
    results = job.find_all(class_='date')
    if len(results) == 0:
        return "unknown"
    else:
        return removeCommas(results[0].text)

def extractCompanyName(job):
    results = job.find_all(class_='companyName')
    if len(results) == 0:
        return "unknown"
    else:
        return results[0].text

def extractJobSalary(job):
    results = job.find_all(class_='salary-snippet-container')
    if len(results) == 0:
        return "unknown"
    else:
        return results[0].text

def extractJobLocation(job):
    results = job.find_all(class_='companyLocation')
    if len(results) == 0:
        return "unknown"
    else:
        return removeCommas(results[0].text)

def extractJobTitle(job):
    results = job.select('span[id^="jobTitle"]')
    if len(results) == 0:
        return None
    else:
        return results[0].text

def writeResultSetToFile(resultSet):
    with open('output.csv', 'w') as f:
        for item in resultSet:
            item.prettify()
            print(item)
            # f.write(item + '\n' + '-------------------' + '\n')

def writeStringDataToFile(data):
    with open('output.txt', 'a') as f:
        f.write(data)

def writeCsvDataToFile(data):
    with open('output.csv', 'w', newline='') as f:
        print(data)
        writer = csv.writer(f)
        writer.writerows(data)
        print("Data written to file")

def getJobTitles(soup):
    job_titles = soup.select('span[id^="jobTitle"]')
    return job_titles   

def getJobListItems(soup):
    return soup.find_all("ul", class_="jobsearch-ResultsList")

# soup must include a unordered list of job conatiners
def getJobListItem(soup):
    return soup.find_all("li")
    
def main():    
    driver = setFireFoxDriver()
    page_soup = getPageData(driver)

    # ul encapsures all job li items
    ul_of_job_containers = getJobListItems(page_soup)

    # this will grab all li items and put them into a result set (list)
    jobs = getJobListItem(ul_of_job_containers[0])

    data = []
    
    for job in jobs:
        job_data = []
        job_data.append(extractJobId(job))
        job_data.append(extractJobTitle(job))
        job_data.append(extractJobLocation(job))
        job_data.append(extractCompanyName(job))
        job_data.append(extractJobSalary(job))
        job_data.append(extractDataPosted(job))
        if job_data[0]:
            data.append(job_data)
    
    writeCsvDataToFile(data)
    # Close firefox
    driver.close()
main()

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")