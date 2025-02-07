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

for brand in brands.keys():
    driver.get(brands[brand])

    # Find the 'Modeles' button and click it
    modeles_button_xpath = "//div[contains(@class, 'navProd')]//a[contains(text(), 'Modèles')]"
    modeles_button = driver.find_elements(By.XPATH, modeles_button_xpath)[1]
    modeles_button.click()


driver.quit()