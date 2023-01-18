from requests_service import get_json


def find_a_joke():
    json = get_json('https://geek-jokes.sameerkumar.website/api?format=json')
    joke = json.get("joke")

    return joke


def main(nb_of_jokes):
    if __name__ == '__main__':
        for i in range(nb_of_jokes):
            print(find_a_joke())


main(5)
