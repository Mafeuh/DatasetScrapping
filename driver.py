from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

def get_driver(url: str, headless: bool = False):
    """
    Returns a new driver instance linked to the URL.
    """
    options = Options()
    options.headless = headless

    driver = Firefox(options=options)
    driver.get(url)

    return driver


def get_caradisiac_driver(headless: bool = False):
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
        print("Un problème est survenu en voulant accepter les cookies.")
        print("Erreur complète:", e)
        driver.quit()

    return driver