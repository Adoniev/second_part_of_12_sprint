import data
import send_request
import pytest


def get_track():
    order_response = send_request.post_create_order(data.order_body)
    return order_response.json()["track"]

def test_response_code_200():
    track = get_track()
    find_order_respose = send_request.get_find_order(track)
    assert find_order_respose.status_code == 200
