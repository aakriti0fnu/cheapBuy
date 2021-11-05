def description_from_url_amazon(link):
    """
    This is a function to take the user product URL as a link and return the description of the user product
        :param link:
        :return:Search term/description
    """
    description = ""
    try:
        link = link.replace("https://www.amazon.com/", "")
        for ch in link:
            if ch != "/":
                description += ch
            else:
                break
        # description = " ".join( description.split("-")[:-1] )
        description = description.replace("-", " ")
        print(
            f"Extracted item/search_term/description to be searched: \n >>{description}<<"
        )
    except:
        print("Can't pull the description from amazon url.")
        description = ""
    print("-" * 10)
    return description
