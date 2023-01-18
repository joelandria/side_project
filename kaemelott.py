from requests_service import get_json, get_json_fields


# idées en vrac
# base url : https://kaamelott.chaudie.re/api

def get_random():
    output = get_json("https://kaamelott.chaudie.re/api/random")

    # todo: extract get_kaamelott
    citation = output.get("citation")

    infos = citation.get("infos")
    text = citation.get("citation")
    personnage = infos.get("personnage")
    saison = infos.get("saison")
    episode = infos.get("episode")
    return f"{text} - {personnage}\n{saison} - {episode}"


def get_characters_list():
    with open("personnages.txt", "r", encoding="utf-8") as file:
        return file.read().split("\n")


def main(nb_of_items):
    if __name__ == '__main__':
        for i in range(nb_of_items):
            print(f"{get_random()}\n")


print(get_characters_list())
