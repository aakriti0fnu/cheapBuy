from ..code.web.scraper.fetch_description.amazon import description_from_url_amazon

"""
User is on Amazon!
"""


def test_fetch_description_amazon1():
    """
    tests whether the description string extraction from a user product URL is working okay.

    :return: None
    """
    link = "https://www.amazon.com/2021-Apple-10-2-inch-iPad-Wi-Fi/dp/B09G9FPHY6/ref=sr_1_3?dchild=1&keywords=ipad&qid=1632940310&sr=8-3"
    assert description_from_url_amazon(
        link) == "2021 Apple 10 2 inch iPad Wi Fi"


def test_fetch_description_amazon2():
    """
    tests whether the description string extraction from a user product URL is working okay.

    :return: None
    """
    link = "https://www.amazon.com/Brita-Longlast-Replacement-Filters-Dispensers/dp/B01MU7973W/ref=sr_1_5?dchild=1&keywords=brita+filter&qid=1632940370&sr=8-5"
    description = description_from_url_amazon(link)
    assert description == "Brita Longlast Replacement Filters Dispensers"
