from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import time
import requests

# Configuration du mode headless et blocage des pop-ups/publicités
options = Options()
options.headless = True  # Active le mode headless
options.set_preference("dom.disable_open_during_load", True)  # Bloque les pop-ups
options.set_preference("privacy.popups.showBrowserMessage", False)  # Empêche les alertes pop-up

print("Mode headless activé :", options.headless)

driver = Firefox(options=options)

def get_images(driver, brand, model, amount=30):
    images = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "wIjY0d jFk0f")]//img[contains(@class, "YQ4gaf")]'))
    )[:amount * 2]

    for i in range(0, len(images), 2):
        try:
            image = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'(//div[contains(@class, "wIjY0d jFk0f")]//img[contains(@class, "YQ4gaf")])[{i + 1}]'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", image)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", image)

            img = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "p7sI2 PUxBg")]//img'))
            )
            src = img.get_attribute('src')
            resp = requests.get(src)

            path = f'data/{brand}/{model}'
            os.makedirs(path, exist_ok=True)

            with open(f'{path}/{i}.png', 'wb') as file:
                file.write(resp.content)

        except Exception as e:
            print(f"Erreur lors du traitement de l'image {i} : {e}")

# Chargement des données JSON
with open('Caradisiac/voiturepresenfrance.json') as file:
    models = json.load(file)

query_url = "https://www.google.com/search?udm=2&q="
driver.get(query_url)

# Gestion des cookies
cookies_xpath = '//*[@id="L2AGLb"]'
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cookies_xpath))).click()
except Exception as e:
    print("Pas de popup de cookies trouvé.")

# Parcours des marques et modèles
brands = list(models.keys())

for key in brands:
    for model in models[key]:
        driver.get(query_url + str('voiture ' + model).replace(' ', '+'))
        time.sleep(1)
        get_images(driver, key, model)

driver.quit()  # Ferme le navigateur proprement