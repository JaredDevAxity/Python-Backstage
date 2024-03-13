import unittest
from unittest.mock import Mock
from microservice.facade import GitHubFacade

class TestGitHubFacade(unittest.TestCase):
    def test_create_repository(self):
        repository = {
            "name": "NewReposity",
            "description": "Description of the repository",
            "token": "token123"
        }

        mock_github_service = Mock()
    
        mock_github_service.create_repository.return_value = "Repositorio creado satifactoriamente"

        github_facade = GitHubFacade()
        github_facade.github_service = mock_github_service

        result = github_facade.create_repository(repository["name"], repository["description"], repository['token'])

        expected_result = "Repositorio creado satifactoriamente"

        self.assertEqual(result, expected_result)

    def test_add_folders(self):
        repository = {
            "name": "NewReposity",
            "folders": ["frontend", "backend"],
            "token": "token123"
        }

        mock_github_service = Mock()
    
        mock_github_service.add_folders.return_value = "Carpetas creadas"

        github_facade = GitHubFacade()
        github_facade.github_service = mock_github_service

        result = github_facade.add_folders(repository["folders"], repository['token'], repository["name"])

        expected_result = "Carpetas creadas"

        self.assertEqual(result, expected_result)

    def test_send_file(self):
        repository = {
            "id_crea_type": 1,
            "token": "token123",
            "user": "User", 
            "destination_repo": "DestinationRepositorio",
            "owner": "Axity",
            "destination_path": "DestinationPath"
        }

        mock_github_service = Mock()
    
        mock_github_service.send_file.return_value = "Archivos subidos correctamente"

        github_facade = GitHubFacade()
        github_facade.github_service = mock_github_service

        result = github_facade.send_file(repository["id_crea_type"], repository["token"], repository['user'], repository["destination_repo"], repository['owner'], repository["destination_path"])

        expected_result = "Archivos subidos correctamente"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()