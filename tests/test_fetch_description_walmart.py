from ..code.web.scraper.fetch_description.walmart import description_from_url_walmart

"""
User is on Walmart!
"""


def test_fetch_description_walmart1():
    """
    tests whether the description string extraction from a user product URL is working okay.

    :return: None
    """
    link = "https://www.walmart.com/ip/Oreo-Chocolate-Hazelnut-Flavored-Creme-Chocolate-Sandwich-Cookies-Family-Size-17-Oz/720352647"
    assert (
        description_from_url_walmart(link)
        == "Oreo Chocolate Hazelnut Flavored Creme Chocolate Sandwich Cookies Family Size 17 Oz"
    )


def test_fetch_description_walmart2():
    """
    tests whether the description string extraction from a user product URL is working okay.

    :return: None
    """
    link = "https://www.walmart.com/ip/Time-and-Tru-Shaker-Cardigan/530065539"
    description = description_from_url_walmart(link)
    assert description == "Time and Tru Shaker Cardigan"
