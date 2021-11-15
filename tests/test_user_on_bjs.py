from ...code.web.scraper.web_scraper import scraper

"""
User is on Bjs!
"""


def test_scrapper_bjs_result1():
    """
    For a given user product url
        tests whether the returned dict has at least 1 entry from the 4 scraped sites :ebay,costco,walmart,amazon

    :return:
    """
    result = scraper(
        "https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578"
    )
    assert result is not None


def test_scrapper_bjs_result2():
    """
    For a given user product url
        tests whether the returned dict has at least 1 entry from the 4 scraped sites :ebay,costco,walmart,amazon

    :return: None
    """

    result = scraper(
        "https://www.bjs.com/product/apple-airpods-with-charging-case---2nd-generation/3000000000001690751"
    )
    assert result is not None


def test_scrapper_bjs_result_len1():
    """
    For a given user product url
        tests whether the returned dict has 4 entries respective to each scraped sites :ebay,costco,walmart,amazon

    :return: None
    """
    result = scraper(
        "https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578"
    )
    assert len(result) == 4


def test_scrapper_bjs_result_len2():
    """
    For a given user product url
        tests whether the returned dict has 4 entries respective to each scraped sites :ebay,costco,walmart,amazon
    :return: None
    """
    result = scraper(
        "https://www.bjs.com/product/apple-airpods-with-charging-case---2nd-generation/3000000000001690751"
    )
    assert len(result) == 4


def test_scrapper_bjs_result_description_count():
    """
    For a given user product url
        tests whether the returned dict-key{description} at least 1 entry from the 4 scraped sites :ebay,costco,walmart,amazon

    :return: None
    """
    result = scraper(
        "https://www.bjs.com/product/hersheys-zero-sugar-chocolate-candy-assortment-182-oz/3000000000003027755"
    )
    assert len(result["description"]) >= 1
