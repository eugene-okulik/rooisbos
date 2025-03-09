from locust import HttpUser, task


class TestApi(HttpUser):
    object_id = None

    def on_start(self) -> None:
        response = self.client.post(
            '/object',
            json={"data": {
                "color": "BLACK",
                "size": "BIG"
            },
                "name": "II_object"}
        )
        self.object_id = response.json()['id']

    @task(2)
    def get_objects(self):
        self.client.get('/object')

    @task(5)
    def get_object(self):
        self.client.get(f'/object/{self.object_id}')

    @task(1)
    def post_object(self):
        self.client.post('/object',
                         json={"data": {
                             "color": "some_color",
                             "size": "XXXXXL"
                         },
                             "name": "II_object_2"})

    @task(3)
    def change_object(self):
        self.client.put(f'/object/{self.object_id}',
                        json={"data": {
                            "color": "some_color_2",
                            "size": "CCXX"
                        },
                            "name": "II_object_3"}
                        )

    @task(3)
    def change_object_partly(self):
        self.client.patch(f'/object/{self.object_id}',
                          json={"name": "II_object_4"})

    def on_stop(self):
        self.client.delete(f'/object/{self.object_id}')
