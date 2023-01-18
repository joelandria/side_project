from requests_service import get_json
from random import randint


def get_xkcd(url):
    json = get_json(url)
    title = json.get("safe_title")
    alt = json.get("alt")
    image_link = json.get("img")
    number = json.get("num")
    return {
        "number": number,
        "title": title,
        "alt": alt,
        "image_link": image_link
    }


def get_current():
    return get_xkcd("https://xkcd.com/info.0.json")


def get_random():
    # get last comic number
    last_number = get_current().get("number")
    random_number = randint(1, last_number)

    return get_xkcd(f"https://xkcd.com/{random_number}/info.0.json")


def main(nb_of_jokes):
    if __name__ == '__main__':
        for i in range(nb_of_jokes):
            print(get_random())


main(5)
