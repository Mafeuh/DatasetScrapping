import json
from driver import *
from progression import *

with open('caradisiac_brands_urls.json', 'r+') as file:
    brands: dict = json.load(file)

driver = get_caradisiac_driver(True)

brand_models = {}

brands_amount = len(list(brands.keys()))

print_progression(0, brands_amount, 'Début')

try:
    count = 0
    for brand_name in list(brands.keys()):
        count += 1
        driver.get(brands[brand_name])

        print_progression(count, brands_amount, brand_name)

        modeles_button_xpath = "//a[contains(text(), 'Modèles')]"

        modeles_url = driver.find_element(By.XPATH, modeles_button_xpath).get_attribute('href')

        driver.get(modeles_url)

        models_divs_xpath = "//li[contains(@class, 'displayGalerie')]//a/img/.."

        models = driver.find_elements(By.XPATH, models_divs_xpath)

        if len(models) > 0:
            brand_models[brand_name] = []
            for model in models:
                brand_models[brand_name].append(model.get_attribute('title'))
except Exception as error:
    print(f"Erreur: Le code a planté sur la marque {brand_name}")
    print("Erreur complète:", error)
finally:
    driver.close()
    with open('caradisiac_models.json', 'w+') as file:
        json.dump(brand_models, file, indent=2)