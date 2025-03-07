import requests
import allure
from test_api_iismagilov.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Sending put request')
    def make_changes_to_object(self, object_id, payload):
        self.response = requests.put(f'{self.url}/{object_id}', json=payload)
        self.response_formatted_to_json = self.response.json()
        return self.response
