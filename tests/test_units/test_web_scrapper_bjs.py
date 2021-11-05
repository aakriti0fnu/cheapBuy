from ...code.web.scraper.scrap.bjs import get_url_bjs, scrap_bjs
from tests import setup_get_driver_details

"""
Tests individual scraping functions of Bjs!
"""


def test_get_url_bjs_1():
    """
    For a given product/item description
        tests whether the url building happens correctly.

    :return: None
    """
    item_name = "Amazfit Band 5 Fitness Tracker with Alexa Built-in"
    assert get_url_bjs(item_name) == f"https://www.bjs.com/search/{item_name}"


def test_get_url_bjs_2():
    """
    For a given product/item description
        tests whether the url building happens correctly.

    :return: None
    """
    item_name = "Brita Longlast Replacement Filters Dispensers"
    assert get_url_bjs(item_name) == f"https://www.bjs.com/search/{item_name}"


def test_scrap_bjs():
    """
    For a given product/item description
        tests whether the returned list has at least 1 item found from the scraped site :Bjs

    :return: None
    """
    item_name = "SAMSUNG Galaxy Tab A7 32GB"
    results = scrap_bjs(setup_get_driver_details(), item_name)
    assert results is not None
