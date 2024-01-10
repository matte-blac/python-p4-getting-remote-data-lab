import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # send a GET request to the URL
        response = requests.get(self.url)

        # return the response content
        return response.content
        pass

    def load_json(self):
        # get the response body
        response_body = self.get_response_body()

        # parse the JSON content
        data = json.loads(response_body)

        return data
        pass