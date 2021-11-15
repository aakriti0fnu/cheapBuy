from ..code.web.scraper.fetch_description.costco import description_from_url_costco

"""
User is on Costco!
"""


def test_fetch_description_costco1():
    """
    tests whether the description string extraction from a user product URL is working okay.

    :return: None
    """
    link = "https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html"
    assert description_from_url_costco(
        link) == "brita replacement filters%2c 10 pack"


def test_fetch_description_costco2():
    """
    tests whether the description string extraction from a user product URL is working okay.

    :return: None
    """
    link = "https://www.costco.com/apple-airpods-wireless-headphones-with-charging-case-(2nd-generation).product.100487204.html"
    assert (
        description_from_url_costco(link)
        == "apple airpods wireless headphones with charging case (2nd generation)"
    )


def test_fetch_description_costco3():
    """
    tests whether the description string extraction from a user product URL is working okay.

    :return: None
    """
    link = "https://www.costco.com/novaform-12%22-advanced-back-support-memory-foam-mattress.product.100478915.html"
    assert (
        description_from_url_costco(link)
        == "novaform 12%22 advanced back support memory foam mattress"
    )
