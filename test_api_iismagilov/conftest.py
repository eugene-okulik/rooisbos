import pytest

from endpoints.create_an_object import CreateObject
from endpoints.change_an_object import UpdateObject
from endpoints.change_an_object_partly import PartlyUpdateObject


@pytest.fixture()
def precondition_create_an_object():
    return CreateObject()

@pytest.fixture()
def precondition_change_an_object():
    return UpdateObject()

@pytest.fixture()
def precondition_change_an_object_partly():
    return PartlyUpdateObject()


