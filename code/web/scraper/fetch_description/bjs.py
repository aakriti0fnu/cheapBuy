def description_from_url_bjs(link):
    """

    :param link:
    :return:
    """
    description = ""
    try:
        remove_initial = link.replace("https://www.bjs.com/product/", "")
        print(remove_initial)
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
        print("Can't pull the description from Bjs url.")
        description = ""
    print("-" * 10)
    return description
