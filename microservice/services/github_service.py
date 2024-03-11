import requests
from flask import jsonify, request
import json

class GitHubAPI:
    def __init__(self, access_token=None):
        self.access_token = access_token
        self.headers = {'Authorization': f'Bearer {self.access_token}'} if self.access_token else {}

    def get(self, url):
        response = requests.get(url, headers=self.headers)
        return response

    def post(self, url, data):
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def put(self, url, data):
        response = requests.put(url, headers=self.headers, json=data)
        return response

class GitHubService:
    def __init__(self) :
        pass

    def create_repository(self, name, description, token):
        github_api = GitHubAPI(access_token=token)
        data = {'name': name, 'description': description}
        response = github_api.post(f'https://api.github.com/user/repos', data=data)

        if response.status_code == 201:
            return "Repositorio creado satisfactoriamente"
        else:
            return Exception("Error al crear repositorio")

    def add_folders(self, folders, token, name):
        github_api = GitHubAPI(access_token=token)
        data = {
            "message":"my commit message",
            "committer":
                {
                "name":"Monalisa Octocat",
                "email":"octocat@github.com"
                },
            "content":""
        }
        try:
            for folder in folders:
                github_api.put(f"https://api.github.com/repos/Jared-dev-prog/{name}/contents/{folder}/erase.me", data)
            return "Carpetas creadas"
        except Exception as e:
            return "Hubo un error al crear las carpetas"
        
    def get_all_files(self, github_api, path): 
        files = []
        response = github_api.get(f"https://api.github.com/repos/Jared-dev-prog/Curso-profesional-de-angular/contents/{path}")
        response_json = json.loads(response.content)

        for data in response_json: 
            if data["type"] == 'file':
                files.append({'name': data["name"], "path": data["path"], "url": data["url"]})
            elif data["type"] == 'dir': 
                subdirectory_files = self.get_all_files(github_api, data["path"])
                files.extend(subdirectory_files)
        return files

    def send_file(self, id_crea_type, token):
        github_api = GitHubAPI(access_token=token)
        if id_crea_type == 2:
            files = self.get_all_files(github_api, path="")

            for file in files: 
                response_content = github_api.get(f"{file["url"]}")
                response_content_json = json.loads(response_content.content)

                self.upload_file(token, response_content_json['content'], file["path"])

            return "Archivos subidos correctamente"
        if id_crea_type == 1:
            # response = github_api.get("https://api.github.com/repos/Jared-dev-prog/Repositorio/contents/frontend/transfer.js")
            # responseJson = json.loads(response.content)
            # content = responseJson["content"]

            response = github_api.get("https://api.github.com/repos/Jared-dev-prog/Repositorio/contents/frontend")
            responseJSON = json.loads(response.content)

            archives = []

            for data in responseJSON:
                if data["type"] == 'file':
                    newData = {
                        "name": data["name"],
                        "path": data["path"]
                    }
                    archives.append(newData)
                elif data["type"] == 'dir': 
                    response2 = github_api.get(f"https://api.github.com/repos/Jared-dev-prog/Repositorio/contents/{data["path"]}")
                    responseJSON2 = json.loads(response2.content)
                    print(data["path"])
                    for data in responseJSON2: 
                        if data["type"] == 'file':
                            newData = {
                                "name": data["name"],
                                "path": data["path"]
                            }
                            archives.append(newData)
                    print("Data 2", responseJSON2)
                    
            for archive in archives:
                responseContent = github_api.get(f"https://api.github.com/repos/Jared-dev-prog/Repositorio/contents/{archive["path"]}")
                responseContentJSON = json.loads(responseContent.content)

                print(responseContentJSON['content'])
                self.upload_file(token, responseContentJSON['content'], archive["path"])
            return "Archivo subido correctamente"

    def upload_file(self, token, content, path):
        github_api = GitHubAPI(token)

        data = {
            "message":"my commit message",
            "committer":
                {
                "name":"Monalisa Octocat",
                "email":"octocat@github.com"
                },
            "content": content
        }
        github_api.put(f"https://api.github.com/repos/Jared-dev-prog/Repositorio2/contents/backend/{path}", data)

