from requests_service import get_json, get_json_fields


# idées en vrac
# base url : https://kaamelott.chaudie.re/api

def get_random():
    output = get_json("https://kaamelott.chaudie.re/api/random")

    citation = output.get("citation")

    infos = citation.get("infos")
    text = citation.get("citation")
    personnage = infos.get("personnage")
    saison = infos.get("saison")
    episode = infos.get("episode")
    return f"{text} - {personnage}\n{saison} - {episode}"


def main(nb_of_items):
    if __name__ == '__main__':
        for i in range(nb_of_items):
            print(get_random())


main()

# todo: trouver un moyen de stocker la liste des personnages https://github.com/sin0light/api-kaamelott/#liste-des-personnages
# et de le lire depuis ce programme