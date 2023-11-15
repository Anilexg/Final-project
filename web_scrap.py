from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Apsirašome draiverių inicializavimą
service = Service(ChromeDriverManager().install())

#Atidarome naują Chrome naršyklės langą, kuris valdomas Selenium biblioteka
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

# Funkcija išgauname duomenis iš internetinio puslapio
def scrape_table():
    # Nurodme interneto puslapio URL, iš kurio imsime duomenis
    url="https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo"

    # Atidaro nurodytą URL Chrome naršyklėje
    driver.get(url)

    # Ieškome <table> elemento
    tbody = driver.find_element(By.XPATH, '//html/body/div[2]/table')

    # Sukuriame tuščią sąrašą, kuriame bus saugomi gaunami duomenys
    data = []


    # Ciklas kiekvienai lentelės eilutei (tr) ieško duomenų. Išskyrus antraštinę eilutę [1:]
    # Ciklas suranda visas lentelės (tbody) eilutes naudodamas XPath.
    for tr in tbody.find_elements(By.XPATH, '//tr')[1:]:

        # Kiekvienai eilutei (tr) suranda visus langelių elementus (td) ir išgauna teksto reikšmes
        row = [item.text for item in tr.find_elements(By.XPATH, './/td')]

        # Rastos teksto duomenų eilutė pridedamos prie sąrašo
        data.append(row)


    # Grąžina gautus duomenis
    return data

# Kreipimasis į funkciją
scrape_table()







