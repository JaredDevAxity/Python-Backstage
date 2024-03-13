from ..services import GitHubService

class GitHubFacade: 
    def __init__(self):
        self.github_service = GitHubService()

    def create_repository(self, name, description, token): 
        response = self.github_service.create_repository(name, description, token)
        return response
    
    def add_folders(self, folders, token, name): 
        response = self.github_service.add_folders(folders, token, name)
        return response
    
    def send_file(self, id_crea_type, token, user, destination_repo, owner, destination_path):
        response = self.github_service.send_file(id_crea_type, token, user, destination_repo, owner, destination_path)
        return response 
