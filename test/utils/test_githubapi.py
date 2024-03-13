import unittest
from microservice.utils import GitHubAPI
from unittest.mock import patch

class GitHubApiTestCase(unittest.TestCase):

    @patch('requests.get')
    def test_get_valid_response(self, mock_get): 
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'message': "success"}

        api = GitHubAPI("valid_token")

        response = api.get("https://api.github.com/users/bard")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': "success"})

    @patch('requests.get')
    def test_get_not_found(self, mock_get): 
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {'message': "Not Found"}

        api = GitHubAPI()

        with self.assertRaises(Exception): 
            response = api.get("https://api.github.com/user/bar")
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json(), {'message': "Not Found"})

    @patch('requests.get')
    def test_get_unauthorized(self, mock_get): 
        mock_get.return_value.status_code = 401
        mock_get.return_value.json.return_value = {'message': "Unauthorized"}

        api = GitHubAPI()

        with self.assertRaises(Exception): 
            response = api.get("https://api.github.com/user/bar")
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json(), {'message': "success"})
            
if __name__ == '__main__':
    unittest.main()
        