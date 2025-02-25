import pytest

TEST_DATA = [
    {"name": "IIM2asdf", "data": {"color": "orange", "size": "XL"}},
    {"name": "IIM2zxcv", "data": {"color": "black", "size": "L"}}
]

@pytest.mark.parametrize('data', TEST_DATA)
def test_create_object(precondition_create_an_object, data):
    precondition_create_an_object.create_some_object(data)
    precondition_create_an_object.check_that_status_is_200()
    precondition_create_an_object.checking_color_of_new_object(data['data']['color'])

def test_change_an_object(precondition_change_an_object):
    body = {
        "name": "IIM_neew",
        "data": {
            "color": "white",
            "size": "M"
        }
    }
    precondition_change_an_object.make_changes_to_object(object_id=10, payload=body)
    precondition_change_an_object.check_that_status_is_200()
    precondition_change_an_object.checking_color_of_new_object(body['data']['color'])

def test_change_an_object_partly(precondition_change_an_object_partly):
    body = {"name": "sdfasdfasdfasdf"}
    precondition_change_an_object_partly.make_partly_changes_to_object(object_id=11, payload=body)
    precondition_change_an_object_partly.check_that_status_is_200()
    precondition_change_an_object_partly.check_name_of_new_object(body['name'])

@pytest.mark.parametrize('data', TEST_DATA)
def test_delete_an_object(precondition_create_an_object, data):
    precondition_create_an_object.create_some_object(data)
    precondition_create_an_object.
