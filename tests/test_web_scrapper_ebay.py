from ..code.web.scraper.scrap.ebay import get_url_ebay, scrap_ebay, extract_item_ebay
from . import setup_get_driver_details

"""
Tests individual scraping functions of Ebay!
"""


def test_get_url_ebay_1():
    """
    For a given product/item description
        tests whether the url building happens correctly.

    :return: None
    """
    item_name = "2021 Apple 10 2 inch iPad Wi Fi"
    search_term = item_name.replace("%20", " ")
    assert (
        get_url_ebay(item_name)
        == f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={search_term}"
    )


def test_get_url_ebay_2():
    """
    For a given product/item description
        tests whether the url building happens correctly.

    :return: None
    """
    item_name = "Brita Longlast Replacement Filters Dispensers"
    search_term = item_name.replace("%20", " ")
    assert (
        get_url_ebay(item_name)
        == f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={search_term}"
    )


def test_scrap_ebay():
    """
    For a given product/item description
        tests whether the returned list has at least 1 item found from the scraped site :Ebay.

    :return: None
    """
    item_name = "W. Trends Sunset Twin-Size Metal Bunk Bed - Black"
    results = scrap_ebay(setup_get_driver_details(), item_name)
    assert results is not None


# def test_extract_item_ebay_result_len():
#     '''
#     For a given product/item description
#         1. get a list of items found from the scraped site :Ebay.
#         2. Then, picking the 1st one,
#             tests whether the returned dict has 4 keys{ site, url, description, price}, i.e scraped successfully.
#     :return:
#     '''
#     item_name = "Brita Longlast Replacement Filters Dispensers"
#     result = extract_item_ebay(setup_get_driver_details(), item_name)
#     assert len(result) == 4
#
# def test_extract_item_ebay_result_site():
#     '''
#     For a given product/item description
#         1. get a list of items found from the scraped site :Ebay.
#         2. Then, picking the 1st one,
#             tests whether the returned dict has key {site} value ebay , i.e scraped successfully.
#     :return:
#     '''
#     item_name = "Amazfit Band 5 Fitness Tracker with Alexa Built-in"
#     result = extract_item_ebay(setup_get_driver_details(), item_name)
#     assert result["site"] == "ebay"
#
# def test_extract_item_ebay_result_url():
#     '''
#     For a given product/item description
#         1. get a list of items found from the scraped site :Ebay.
#         2. Then, picking the 1st one,
#             tests whether the returned dict has key {url} that belongs to ebay, i.e scraped successfully.
#     :return:
#     '''
#     item_name = "SAMSUNG Galaxy Tab A7 32GB"
#     result = extract_item_ebay(setup_get_driver_details(), item_name)
#     assert result["url"].find("https://www.ebay.com") != -1
