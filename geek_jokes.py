from requests_service import get_json


def find_a_joke():
    json = get_json('https://geek-jokes.sameerkumar.website/api?format=json')
    return json.get("joke")


def main(nb_of_items):
    if __name__ == '__main__':
        for i in range(nb_of_items):
            print(f"{find_a_joke()}\n")


main(5)
