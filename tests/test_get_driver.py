from ..code.web.scraper.web_scraper import get_driver


def test_get_driver():
    """
    Tests whether it returns instances of selenium.webdrivers such as
        selenium.webdriver.chrome.webdriver.WebDriver
        selenium.webdriver.firefox.webdriver.WebDriver

    :return: None
    """
    assert get_driver() is not None
