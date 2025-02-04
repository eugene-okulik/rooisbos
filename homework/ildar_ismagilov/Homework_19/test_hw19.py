import requests
import pytest


@pytest.fixture()
def creating_and_clearing_the_object():
    body = {
        "name": "IIM2asdf",
        "data": {
            "color": "orange",
            "size": "XXXXXLL"
        }
    }
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


def test_create_object():
    body = {
        "name": "IIM2asdf",
        "data": {
            "color": "orange",
            "size": "XXXXXLL"
        }
    }
    response = requests.post('http://167.172.172.115:52353/object', json=body)
    assert response.status_code == 200, 'Object is not created'


def test_change_object(creating_and_clearing_the_object):
    body = {
        "name": "IIM_22",
        "data": {
            "color": "black",
            "size": "XXXXXLCCCL"
        }
    }
    response = requests.put(f'http://167.172.172.115:52353/object/{creating_and_clearing_the_object}', json=body).json()
    assert response['name'] == 'IIM_22'
    assert response['data']['color'] == 'black'
    assert response['data']['size'] == 'XXXXXLCCCL'


def test_change_object_partly(creating_and_clearing_the_object):
    body = {
        "name": "sdfasdfasdfasdf"
    }
    response = requests.patch(f'http://167.172.172.115:52353/object/{creating_and_clearing_the_object}', json=body).json()
    assert response['name'] == 'sdfasdfasdfasdf', 'Name has not been changed'


def test_delete_object(creating_and_clearing_the_object):
    response = requests.delete(f'http://167.172.172.115:52353/object/{creating_and_clearing_the_object}')
    assert response.status_code == 200, 'Object is not deleted'
