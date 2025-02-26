import json

from driver import *
from selenium.webdriver import Firefox

driver: Firefox = get_caradisiac_driver()

URL = "https://www.caradisiac.com/constructeurs--automobiles/"

driver.get(URL)

brands_href = driver.find_elements(By.XPATH, "//p/a/span[contains(@class, 'font16')]/..")

brands = {}

for brand_href in brands_href:
    brand_url = brand_href.get_attribute('href')
    brand_name = brand_href.text

    brands[brand_name] = brand_url

driver.close()


with open('caradisiac_brands_urls.json', 'w+') as file:
    json.dump(brands, file, indent=4)