def description_from_url_walmart(link):
    """

    This is a function to take the user product URL as a link and return the description of the user product
      :param link:
      :return:Search term/description
    """
    description = ""
    try:
        remove_initial = link.replace("https://www.walmart.com/ip/", "")
        for i in remove_initial:
            if i != "/":
                description += i
            else:
                break
        description = description.replace("-", " ")
        print(
            f"Extracted item/search_term/description to be searched:\n >>{description}<<"
        )
    except:
        print("Can't pull the description from walmart url.")
        description = ""
    print("-" * 10)
    return description
