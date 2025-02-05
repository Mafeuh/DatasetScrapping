from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver(url: str):
    """
    Returns a new driver instance linked to the URL.
    """
    driver = Firefox()
    driver.get(url)

    return driver


def get_caradisiac_driver():
    """
    Returns a new driver instance linked to Caradisiac website, with cookies accepted.
    """
    URL = "https://www.caradisiac.com/"

    driver = get_driver(URL)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button/span[contains(text(), \'Accepter & Fermer\')]'))
        )
        element.click()
    except Exception as e:
        print("Connexion internet pourrie en vrai")
        driver.quit()