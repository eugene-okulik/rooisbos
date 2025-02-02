import requests

def create_object():
    body = {
        "name": "IIM2asdf",
        "data": {
            "color": "orange",
            "size": "XXXXXLL"
        }
    }
    response = requests.post('http://167.172.172.115:52353/object', json=body)
    assert response.status_code == 200, 'Object is not created'


def new_object():
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
    return response.json()['id']

def clear(post_id):
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')

def change_object():
    post_id = new_object()
    body = {
        "name": "IIM_22",
        "data": {
            "color": "black",
            "size": "XXXXXLCCCL"
        }
    }
    response = requests.put(f'http://167.172.172.115:52353/object/{post_id}', json=body).json()
    assert response['name'] == 'IIM_22'
    assert response['data']['color'] == 'black'
    assert response['data']['size'] == 'XXXXXLCCCL'
    clear(post_id)


def change_object_partly():
    post_id = new_object()
    body = {
        "name": "sdfasdfasdfasdf"
    }
    response = requests.patch(f'http://167.172.172.115:52353/object/{post_id}', json=body).json()
    assert response['name'] == 'sdfasdfasdfasdf', 'Name has not been changed'
    clear(post_id)


def delete_object():
    post_id = new_object()
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')
    assert response.status_code == 200, 'Object is not deleted'


create_object()
change_object()
change_object_partly()
delete_object()
