from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

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

def extractJobLocation(job):
    results = job.find_all(class_='companyLocation')
    if len(results) == 0:
        return "unknown"
    else:
        return results[0].text

def extractJobTitle(job):
    results = job.select('span[id^="jobTitle"]')
    if len(results) == 0:
        return None
    else:
        return results[0].text

def writeResultSetToFile(resultSet):
    with open('output.txt', 'w') as f:
        for item in resultSet:
            item.prettify()
            print(item)
            # f.write(item + '\n' + '-------------------' + '\n')

def writeStringDataToFile(data):
    with open('output.txt', 'w') as f:
        f.write(data)

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

    for job in jobs:
        job_title = extractJobTitle(job)
        job_location = extractJobLocation(job)
        if job_title:
            print(f'{job_title},{job_location}')
    
    driver.close()
    
main()
    ## Close firefox