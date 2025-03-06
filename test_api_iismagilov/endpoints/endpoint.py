import allure
import requests


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    response_formatted_to_json = None

    def deleting_the_object(self, object_id):
        requests.delete(f'{self.url}/{object_id}')

    @allure.step('Checking that system returns right color')
    def checking_color_of_new_object(self, color):
        assert self.response_formatted_to_json['data']['color'] == color

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Checking correctness of the name')
    def check_name_of_new_object(self, name):
        assert self.response_formatted_to_json['name'] == 'sdfasdfasdfasdf'
