from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

def scrape_table():
    url="https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo"
    driver.get(url)

    tbody = driver.find_element(By.XPATH, '//html/body/div[2]/table')

    data = []
    for tr in tbody.find_elements(By.XPATH, '//tr')[1:]:
        row = [item.text for item in tr.find_elements(By.XPATH, './/td')]
        data.append(row)

    return data
    driver.quit()



scrape_table()
