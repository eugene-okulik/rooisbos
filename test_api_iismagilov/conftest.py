import pytest

from test_api_iismagilov.endpoints.create_an_object import CreateObject
from test_api_iismagilov.endpoints.change_an_object import UpdateObject
from test_api_iismagilov.endpoints.change_an_object_partly import PartlyUpdateObject
from test_api_iismagilov.endpoints.delete_an_object import DeleteObject


@pytest.fixture()
def temp_object():
    body = {
        "name": "IIM_260225",
        "data": {
            "color": "gray",
            "size": "S"
        }
    }
    temp_object = CreateObject()
    temp_object.create_some_object(body)
    return temp_object.response_formatted_to_json


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def change_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def change_object_partly_endpoint():
    return PartlyUpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
