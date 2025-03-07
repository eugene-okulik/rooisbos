import pytest

TEST_DATA = [
    {"name": "IIM2asdf", "data": {"color": "orange", "size": "XL"}},
    {"name": "IIM2zxcv", "data": {"color": "black", "size": "L"}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_object(create_object_endpoint, data):
    create_object_endpoint.create_some_object(data)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.checking_color_of_new_object(data['data']['color'])


def test_change_an_object(temp_object, change_object_endpoint):
    body = {
        "name": "IIM_neew",
        "data": {
            "color": "white",
            "size": "M"
        }
    }
    change_object_endpoint.make_changes_to_object(object_id=temp_object['id'], payload=body)
    change_object_endpoint.check_that_status_is_200()
    change_object_endpoint.checking_color_of_new_object(body['data']['color'])


def test_change_an_object_partly(temp_object, change_object_partly_endpoint):
    body = {"name": "sdfasdfasdfasdf"}
    change_object_partly_endpoint.make_partly_changes_to_object(object_id=temp_object['id'], payload=body)
    change_object_partly_endpoint.check_that_status_is_200()
    change_object_partly_endpoint.check_name_of_new_object(body['name'])


def test_delete_an_object(temp_object, delete_object_endpoint):
    delete_object_endpoint.delete_an_object(temp_object['id'])
    delete_object_endpoint.check_that_status_is_200()
