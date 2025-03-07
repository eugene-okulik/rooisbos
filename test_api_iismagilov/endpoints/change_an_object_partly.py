import requests
import allure
from test_api_iismagilov.endpoints.endpoint import Endpoint


class PartlyUpdateObject(Endpoint):

    @allure.step('Sending patch request')
    def make_partly_changes_to_object(self, object_id, payload):
        self.response = requests.patch(f'{self.url}/{object_id}', json=payload)
        self.response_formatted_to_json = self.response.json()
        return self.response
