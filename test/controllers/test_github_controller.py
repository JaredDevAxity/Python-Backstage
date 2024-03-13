import unittest
from flask import Flask, jsonify
from microservice.controllers import github_controller_blueprint  # Importa el módulo correcto
from unittest.mock import MagicMock, patch

patch_controller = 'microservice.controllers.github_controller.github_facade'
GITHUB_ROUTE = '/api/github/crear'


class TestGitHubController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(github_controller_blueprint)

    def test_create_repository(self):
        response = {
            "code": 201,
            "message": "Repositorio creado correctamente",
            "status": True
        }

        body = {
            "name": "Backstage",
            "description": "Este es un repositorio de prueba", 
            "token": "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",
            "folders": ["frontend/polux"],
            "id_crea_type": 1,
            "user": "Jared",
            "destination_repo": "Backstage",
            "owner": "Jared-dev-prog",
            "destination_path": "frontend/polux"
        }

        github_facade = MagicMock()
        github_facade.create_repository.return_value = response

        with patch(patch_controller, github_facade):
            with self.app.test_client() as client:
                response = client.post(GITHUB_ROUTE, json=body)
                data = response.get_json()

                self.assertEqual(response.status_code, 201)
                self.assertEqual(data["status"], True)
                self.assertEqual(data["message"], "Repositorio creado correctamente")

    def test_add_folders(self):
        response = {
            "code": 201,
            "message": "Repositorio creado correctamente",
            "status": True
        }

        body = {
            "name": "Backstage",
            "description": "Este es un repositorio de prueba", 
            "token": "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",
            "folders": ["frontend/polux"],
            "id_crea_type": 1,
            "user": "Jared",
            "destination_repo": "Backstage",
            "owner": "Jared-dev-prog",
            "destination_path": "frontend/polux"
        }

        github_facade = MagicMock()
        github_facade.add_folders.return_value = response

        with patch(patch_controller, github_facade):
            with self.app.test_client() as client:
                response = client.post(GITHUB_ROUTE, json=body)
                data = response.get_json()

                self.assertEqual(response.status_code, 201)
                self.assertEqual(data["status"], True)
                self.assertEqual(data["message"], "Repositorio creado correctamente")

    def test_upload_files(self):
        response = {
            "code": 201,
            "message": "Repositorio creado correctamente",
            "status": True
        }

        body = {
            "name": "Backstage",
            "description": "Este es un repositorio de prueba", 
            "token": "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",
            "folders": ["frontend/polux"],
            "id_crea_type": 1,
            "user": "Jared",
            "destination_repo": "Backstage",
            "owner": "Jared-dev-prog",
            "destination_path": "frontend/polux"
        }

        github_facade = MagicMock()
        github_facade.send_file.return_value = response

        with patch(patch_controller, github_facade):
            with self.app.test_client() as client:
                response = client.post(GITHUB_ROUTE, json=body)
                data = response.get_json()

                self.assertEqual(response.status_code, 201)
                self.assertEqual(data["status"], True)
                self.assertEqual(data["message"], "Repositorio creado correctamente")


if __name__ == '__main__':
    unittest.main()