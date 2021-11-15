from ..code.web.scraper.scrap.amazon import get_url_amazon, scrap_amazon
from tests import setup_get_driver_details

"""
Tests individual scraping functions of Amazon!
"""


def test_get_url_amazon_1():
    """
    For a given product/item description
        tests whether the url building happens correctly.

    :return: None
    """
    item_name = "2021 Apple 10 2 inch iPad Wi Fi"
    search_term = item_name.replace(" ", "+")
    assert (
        get_url_amazon(item_name)
        == f"https://www.amazon.com/s?k={search_term}&ref=nb_sb_ss_ts-doa-p_3_5"
    )


def test_get_url_amazon_2():
    """
    For a given product/item description
        tests whether the url building happens correctly.

    :return: None
    """
    item_name = "Brita Longlast Replacement Filters Dispensers"

    search_term = item_name.replace(" ", "+")
    assert (
        get_url_amazon(item_name)
        == f"https://www.amazon.com/s?k={search_term}&ref=nb_sb_ss_ts-doa-p_3_5"
    )


def test_scrap_amazon():
    """
    For a given product/item description
        tests whether the returned list has at least 1 item found from the scraped site :Amazon

    :return: None
    """
    item_name = "W. Trends Sunset Twin-Size Metal Bunk Bed - Black"
    results = scrap_amazon(setup_get_driver_details(), item_name)
    assert results is not None
