import requests


def find_a_joke():
    response = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')

    json = response.json()
    joke = json.get("joke")
    print(joke)

    response.close()
    return joke


def main(nb_of_jokes):
    if __name__ == '__main__':
        for i in range(nb_of_jokes):
            find_a_joke()


main(5)
