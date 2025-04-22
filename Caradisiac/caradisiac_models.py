import json
from driver import *
from progression import *

# Si le code plante, mettre le nom de la dernière marque qui a été référencée dans le fichier de sortie.
STARTING_BRAND_NAME = "Pegaso"

with open('caradisiac_brands_urls.json', 'r+') as file:
    brands: dict = json.load(file)

try:
    STARTING_INDEX = list(brands.keys()).index(STARTING_BRAND_NAME)
except:
    STARTING_INDEX = 0

driver = get_caradisiac_driver(True)

brand_models = {}

brands_amount = len(list(brands.keys())[STARTING_INDEX:])

print_progression(0, brands_amount, 'Début')

try:
    count = 0
    for brand_name in list(brands.keys())[STARTING_INDEX:]:
        count += 1

        url = brands[brand_name]

        if "/modeles" not in url:
            url += "/modeles"

        driver.get(url)

        print_progression(count, brands_amount, brand_name)

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
    with open(f'caradisiac_models{STARTING_INDEX}.json', 'w+') as file:
        json.dump(brand_models, file, indent=2)