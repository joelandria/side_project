"""
a module to get XKCD comic
"""
from requests_service import get_json_fields
from random import randint


def get_xkcd(url):
    # we only want "interesting" fields
    return get_json_fields(url, ["safe_title", "alt", "img", "num"])


def get_current():
    return get_xkcd("https://xkcd.com/info.0.json")


def get_random():
    last_number = get_current().get("num")
    random_number = randint(1, last_number)

    return get_xkcd(f"https://xkcd.com/{random_number}/info.0.json")


def nice_display(xkcd_json):
    return f"\n{xkcd_json.get('safe_title')}\n{xkcd_json.get('alt')}\n{xkcd_json.get('img')}"


def main(nb_of_items):
    if __name__ == '__main__':
        for i in range(nb_of_items):
            random = get_random()
            print(nice_display(random))


main(5)
