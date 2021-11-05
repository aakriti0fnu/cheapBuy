from bs4 import BeautifulSoup


def get_url_bjs(search_term):
    """
    Take the user's product description
        return the constructed Bjs product url.

    :param search_term: product description
    :return url: bjs product URL

    """
    # template = "https://www.bjs.com" + "/search/{search_term}"
    domain = "https://www.bjs.com"
    url = f"{domain}/search/{search_term}"
    print(f"Constructed BJ's URL: \n {url}")
    return url


def scrap_bjs(driver, search_term):
    """
    Take the web driver and search_term(user product description)
        scrap the Amazon product page and return the list of item found.

    :param driver: instance of webdriver
    :param search_term: product description
    :return results: list of items found

    """
    url = get_url_bjs(search_term)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    results = soup.find_all("div", {"class": "each-section"})
    return results


def extract_item_bjs(driver, search_term):
    """
    Take the web driver and search_term(user product description),
        return child dictionary of 1st item found the scraped product list.

    :param driver:instance of chrome webdriver
    :param search_term:product description
    :return result:product details dictionary

    """

    result = {}
    try:

        results = scrap_bjs(driver, search_term)
        if len(results) == 0:
            print(
                f"For search_term: {search_term}, \n No item found scrapping BJ's.")
            return result
        print(f"Found {len(results)} items on the BJ's, picking the 2nd one.")
        item = results[1]
        atag = item.find(
            "a", {"class": "product-link mt-xl-3 mt-xs-3 mt-md-0 mt-3"})
        result["url"] = "https://www.bjs.com" + atag.get("href")
        result["description"] = item.find(
            "h2", {"class": "product-title no-select d-none"}
        )
        if result["description"] is None:
            result["description"] = (
                item.find(
                    "h2", {"class": "product-title no-select d-none d-sm-block"})
                .get_text()
                .strip()
            )
        else:
            result["description"] = result["description"].get("title")
        result["description"] = result["description"].replace(
            " | safeHtml", "")
        result["price"] = (
            item.find("div", {"class": "price-block no-select"})
            .get_text()
            .strip()
            .strip("$")
        )

        price = ""

        for i in result["price"]:
            if i != " ":
                price += i
            else:
                break
        result["price"] = price
        result["site"] = "bjs"

    except:
        print("Scraping failed for BJ's")
        result = {}

    return result
