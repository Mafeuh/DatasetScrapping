from selenium.webdriver import Firefox

def get_driver(url: str):
    """
    Returns a new driver instance linked to the URL
    :param url:
    :return:
    """
    driver = Firefox()
    driver.get(url)

    return driver