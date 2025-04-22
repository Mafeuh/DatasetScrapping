import json
import os
import time

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from progression import print_progression

import requests


def get_images(driver: WebDriver, brand: str, model: str, amount: int = 10):
    images = driver.find_elements(By.XPATH, '//div[contains(@class, "wIjY0d jFk0f")]//img[contains(@class, "YQ4gaf")]')[:amount * 2]

    for i, image in enumerate(images):
        if i % 2 == 0:
            image.click()

            img = driver.find_element(By.XPATH, '//div[contains(@class, "p7sI2 PUxBg")]//img')
            src = img.get_attribute('src')
            resp = requests.get(src)

            path = f'data/{brand}/{model}'
            os.makedirs(path, exist_ok=True)

            with open(f'data/{brand}/{model}/{i}.png', 'wb') as file:
                file.write(resp.content)


    """
    for i, image in enumerate(images[:amount]):
        image.click()
        src = driver.find_element(By.XPATH, '//img[contains(@class, "sFlh5c")]').get_attribute('src')
        resp = requests.get(src)
        with open(f'data/{brand}/{model}/{i}.png', 'w+') as file:
            file.write(resp.content)
    """


with open('Caradisiac/caradisiac_models.json') as file:
    models: dict = json.load(file)

driver = Firefox()

query_url = "https://www.google.com/search?udm=2&q="

driver.get(query_url)

cookies_xpath = '//*[@id="L2AGLb"]'
driver.find_element(By.XPATH, cookies_xpath).click()

brands = list(models.keys())

for i in range(len(brands)):
    key = brands[i]

    for model in models[key]:
        driver.get(query_url + str('voiture ' + model).replace(' ', '+'))
        time.sleep(1)
        get_images(driver, key, model)