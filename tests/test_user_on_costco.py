from ...code.web.scraper.web_scraper import scraper

"""
User is on Costco!
"""


def test_scrapper_costco_result1():
    """
    For a given user product url
        tests whether the returned dict has 4 entries respective to each scraped sites :ebay,amazon,walmart,bjs

    :return: None
    """
    result = scraper(
        "https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html"
    )
    assert result is not None


def test_scrapper_costco_result2():
    """
    For a given user product url
        tests whether the returned dict has 4 entries respective to each scraped sites :ebay,amazon,walmart,bjs

    :return: None
    """
    result = scraper(
        "https://www.costco.com/apple-airpods-wireless-headphones-with-charging-case-(2nd-generation).product.100487204.html"
    )
    assert result is not None


def test_scrapper_costco_result_len1():
    """
    For a given user product url
        tests whether the returned dict has 4 entries respective to each scraped sites :ebay,amazon,walmart,bjs

    :return: None
    """
    result = scraper(
        "https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html"
    )
    assert len(result) == 4


def test_scrapper_costco_result_len2():
    """
    For a given user product url
        tests whether the returned dict has 4 entries respective to each scraped sites :ebay,amazon,walmart,bjs

    :return: None
    """
    result = scraper(
        "https://www.costco.com/apple-airpods-wireless-headphones-with-charging-case-(2nd-generation).product.100487204.html"
    )
    assert len(result) == 4
