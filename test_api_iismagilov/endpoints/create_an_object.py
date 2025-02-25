import requests
import allure
from test_api_iismagilov.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step('Creating an object')
    def create_some_object(self, payload):
        self.response = requests.post(self.url, json=payload)
        self.response_formatted_to_json = self.response.json()
        return self.response
