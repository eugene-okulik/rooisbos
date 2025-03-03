import requests
import allure
from test_api_iismagilov.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Deleting an object')
    def delete_an_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response