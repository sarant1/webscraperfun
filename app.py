from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup


driver = webdriver.Firefox()
driver.get("https://samuelarant.com")

page_data = driver.page_source
soup = BeautifulSoup(page_data, 'html.parser')
data = soup.find_all("p", class_='indent-8')
print(data)


# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()