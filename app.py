from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

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

def writeResultSetToFile(resultSet):
    with open('output.txt', 'a') as f:
        for item in resultSet:
            f.write(item.text + '\n')

def writeDataToFile(data):
    with open('output.txt', 'w') as f:
        f.write(data)

def getJobTitles(soup):
    job_titles = soup.select('span[id^="jobTitle"]')
    return job_titles   

def getJobListItems(soup):
    return soup.find_all("ul", class_="jobsearch-ResultsList")

def getJobListItem(soup):
    return soup.find_all("li")
    
def main():    
    driver = setFireFoxDriver()
    page_soup = getPageData(driver)
    ul_of_job_containers = getJobListItems(page_soup)
    job = getJobListItem(ul_of_job_containers[0])
    print("List length: ", len(job))
    writeDataToFile(job[0].prettify())
    # for item in ul_of_job_containers:
    #     job_title = getJobTitles(item)
    #     print(job_title)
    # driver.close()
    # jobTitles = getJobTitles(page_soup)
    # writeResultSetToFile(jobTitles)
    
main()
    ## Close firefox