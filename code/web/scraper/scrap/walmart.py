from bs4 import BeautifulSoup


def get_url_walmart(search_term):
    """
    Take the user's product description
        return the constructed Amazon product url.

    :param search_term:product description
    :return url:specific product URL

    """

    template = "https://www.walmart.com/search?q={}"
    search_term = search_term.replace(" ", "+")
    url = template.format(search_term)
    print(f"Constructed Walmart URL: \n >>{url}<<")
    return url


def scrap_walmart(driver, search_term):
    """
    Take the web driver and search_term(user product description)
        scrap the Amazon product page and return the list of item found.


    :param driver: instance of webdriver
    :param search_term: product description
    :return results: list of items found

    """
    url = get_url_walmart(search_term)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    with open(
        "/Users/anubhavchaudhary/Downloads/github/repos/cheapBuy/data/walmart.html", "w"
    ) as fileptr:
        fileptr.write(str(soup))

    results = soup.find_all(
        "div",
        {
            "class": "flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3"
        },
    )
    print("results:{}".format(results))
    return results


def extract_item_walmart(driver, search_term):
    """
    Take the web driver and search_term(user product description)
        scrap the Amazon product page and return the list of item found.

    :param driver:instance of webdriver
    :param search_term:product description
    :return result:product details dictionary

    """
    result = {}
    try:
        results = scrap_walmart(driver, search_term)
        if len(results) == 0:
            print(
                f"***** For search_term: {search_term}, \n No item found scrapping Walmart."
            )
            return result
        print(
            f"Found {len(results)} items on the Walmart, picking the 1st one.")
        item = results[0]
        atag = item.find("a", {"class": "absolute w-100 h-100 z-1"})
        result["description"] = atag.find("span", {"class": "w_Cs"}).text
        result["url"] = atag.get("href")
        parent_price = item.find(
            "div",
            {"class": "flex flex-wrap justify-start items-center lh-title mb2 mb1-m"},
        )
        result["price"] = parent_price.find(
            "div", {"class": "b black f5 mr1 mr2-xl lh-copy f4-l"}
        ).text.strip("$")
        result["site"] = "walmart"
    except:
        print("Scraping failed for Ebay")
        result = {}
    return result
