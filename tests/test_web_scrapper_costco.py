from ..code.web.scraper.scrap.costco import get_url_costco, scrap_costco
from tests import setup_get_driver_details

"""
Tests individual scraping functions of Costco!
"""


def test_get_url_costco_1():
    """
    For a given product/item description
        tests whether the url building happens correctly.

    :return: None
    """
    search_term = (
        "White Diamonds by Elizabeth Taylor 3.3 3.4 oz EDT Perfume for Women New Tester"
    )
    item_name = search_term.replace(" ", "%20")
    assert (
        get_url_costco(item_name)
        == f"https://www.costco.com//CatalogSearch?dept=All&keyword={item_name}"
    )


def test_get_url_costco_2():
    """
    For a given product/item description
        tests whether the url building happens correctly.

    :return: None
    """
    search_term = "Olay Regenerist Micro Sculpting Moisturizer Fragrance Free"
    item_name = search_term.replace(" ", "%20")
    assert (
        get_url_costco(item_name)
        == f"https://www.costco.com//CatalogSearch?dept=All&keyword={item_name}"
    )


def test_scrap_costco():
    """
    For a given product/item description
        tests whether the returned list has at least 1 item found from the scraped site :Costco
    :return: None

    """
    search_term = "Olay Regenerist Micro Sculpting Moisturizer Fragrance Free"
    item_name = search_term.replace(" ", "%20")
    results = scrap_costco(setup_get_driver_details(), item_name)
    assert results is not None
