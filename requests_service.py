"""
a library / service to facilitate the use of requests
"""
import requests


def get_json(url):
    """
    make a GET call to URL and return the JSON response
    :param url: the URL to request
    :return: the JSON response
    """
    response = requests.get(url)

    json = response.json()

    response.close()
    return json


def get_json_fields(url, fields):
    """
    make a GET call to URL and return a JSON response with the requested fields
    :param url: the URL to request
    :param fields: the fields to include in the response
    :return: the filtered JSON response
    :raise: if fields is not a list
    """
    if isinstance(fields, list):
        json = get_json(url)
        output = {}

        for field in fields:
            output[field] = json.get(field)

        return output
    else:
        raise TypeError("parameter fields MUST be a list")
