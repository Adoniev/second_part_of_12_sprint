import config
import requests
import data


def post_create_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH, json=body, headers=data.headers)

def get_find_order(track):
    return requests.get(config.URL_SERVICE + config.FIND_ORDER_PATH + "?t=" + str(track), headers=data.headers)