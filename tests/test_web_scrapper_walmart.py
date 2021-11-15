from ..code.web.scraper.scrap.walmart import get_url_walmart, scrap_walmart
from tests import setup_get_driver_details

"""
Tests individual scraping functions of Walmart!
"""


def test_get_url_walmart_1():
    """
    For a given product/item description
        tests whether the url building happens correctly.

    :return: None
    """
    item_name = "SAMSUNG Galaxy Tab A7 32GB"
    assert (
        get_url_walmart(item_name)
        == "https://www.walmart.com/search?q=SAMSUNG+Galaxy+Tab+A7+32GB"
    )


def test_get_url_walmart_2():
    """
    For a given product/item description
        tests whether the url building happens correctly.

    :return:
    """
    assert (
        get_url_walmart("Brita Longlast Replacement Filters Dispensers")
        == "https://www.walmart.com/search?q=Brita+Longlast+Replacement+Filters+Dispensers"
    )


# def test_scrap_walmart():
#     '''
#     For a given product/item description
#         tests whether the returned list has at least 1 item found from the scraped site :Walmart.
#
#     :return: None
#     '''
#     item_name = "Fresh Strawberries, 1 lb"
#     results = scrap_walmart(setup_get_driver_details(), item_name)
#     assert results is not None
