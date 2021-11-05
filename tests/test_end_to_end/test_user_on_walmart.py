from ...code.web.scraper.web_scraper import scraper

"""
User is on Walmart!
"""


def test_scrapper_walmart_result():
    """
    For a given user product url
        tests whether the returned dict has at least 1 entry from the 4 scraped sites :ebay,costco,walmart,bjs

    :return: None

    """
    result = scraper(
        "https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038"
    )
    assert result is not None


def test_scrapper_walmart_result_len():
    """
    For a given user product url
        tests whether the returned dict has 4 entries respective to each scraped sites :ebay,costco,walmart,amazon

    :return: None
    """
    result = scraper(
        "https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038"
    )
    assert len(result) == 4
