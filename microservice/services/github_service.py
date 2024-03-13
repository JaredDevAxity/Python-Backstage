import json
from ..utils.githubapi import GitHubAPI

# class GitHubAPI:
#     def __init__(self, access_token=None):
#         self.access_token = access_token
#         self.headers = {'Authorization': f'Bearer {self.access_token}'} if self.access_token else {}

#     def get(self, url):
#         response = requests.get(url, headers=self.headers)
#         return response

#     def post(self, url, data):
#         response = requests.post(url, headers=self.headers, json=data)
#         return response

#     def put(self, url, data):
#         response = requests.put(url, headers=self.headers, json=data)
#         return response

class GitHubService:
    def __init__(self) :
        self.github_api = GitHubAPI()

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
            "content":"Qm9ycmFtZSBwb3JmYXZvciEgOkQ="
        }
        try:
            for folder in folders:
                github_api.put(f"https://api.github.com/repos/Jared-dev-prog/{name}/contents/{folder}/erase.me", data)
            return "Carpetas creadas"
        except Exception as e:
            return "Hubo un error al crear las carpetas"
        
    def get_all_files(self, github_api, path): 
        files = []
        response = github_api.get(f"https://api.github.com/repos/Jared-dev-prog/angular/contents/{path}")
        response_json = json.loads(response.content)

        for data in response_json: 
            if data["type"] == 'file':
                files.append({'name': data["name"], "path": data["path"], "url": data["url"]})
            elif data["type"] == 'dir': 
                subdirectory_files = self.get_all_files(github_api, data["path"])
                files.extend(subdirectory_files)
        return files

    def send_file(self, id_crea_type, token, user, destination_repo, owner, destination_path):
        github_api = GitHubAPI(access_token=token)
        if id_crea_type == 1:
            files = self.get_all_files(github_api=github_api, path="")

            for file in files: 
                response_content = github_api.get(f"{file["url"]}")
                response_content_json = json.loads(response_content.content)

                self.upload_file(token, response_content_json['content'], file["path"], user, owner, destination_repo, destination_path)

            return "Archivos subidos correctamente"

    def upload_file(self, token, content, path, user, owner, destination_repo, destination_path):
        github_api = GitHubAPI(token)

        data = {
            "message": "subiendo archivo",
            "committer":
                {
                "name": user,
                "email": f"{user}@axity.com"
                },
            "content": content
        }
        github_api.put(f"https://api.github.com/repos/{owner}/{destination_repo}/contents/{destination_path}/{path}", data)

