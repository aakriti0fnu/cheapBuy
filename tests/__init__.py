from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def setup_get_driver_details():
    """
    This function provides the instance of a chrome and firefox driver to get the request

    :return:  instance of Chrome and firefoxWebDriver.
    """
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(
        options=options, executable_path=ChromeDriverManager().install()
    )
    return driver
