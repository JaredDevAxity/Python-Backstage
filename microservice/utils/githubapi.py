import requests

class GitHubAPI:
    def __init__(self, access_token=None):
        self.access_token = access_token
        self.headers = {'Authorization': f'Bearer {self.access_token}'} if self.access_token else {}

    def get(self, url):
        response = requests.get(url, headers=self.headers)

        if response.status_code == 401:
            response = "Unauthorized"
        
        if response.status_code == 404:
            response = "Not Found"

        return response

    def post(self, url, data):
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def put(self, url, data):
        response = requests.put(url, headers=self.headers, json=data)
        return response