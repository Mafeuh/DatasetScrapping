import json
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

import urllib

with open('Caradisiac/caradisiac_models.json') as file:
    models: dict = json.load(file)

driver = Firefox()

query_url = "https://www.google.com/search?udm=2&q="

driver.get(query_url)

cookies_xpath = '//*[@id="L2AGLb"]'
driver.find_element(By.XPATH, cookies_xpath).click()

brands = list(models.keys())

for i in range(20):
    key = brands[i]

    for model in models[key]:
        driver.get(query_url + str('voiture ' + model).replace(' ', '+'))
        input()


def get_images(driver: WebDriver, amount: int = 10):
    images = driver.find_elements(By.TAG_NAME, 'img')

    for image in images:
        src = image.get_attribute('src')
        urllib.urlretrieve(src, 'out.jpg')