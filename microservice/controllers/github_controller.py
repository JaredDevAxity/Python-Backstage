from flask import jsonify, request
from . import github_controller_blueprint
from ..facade import GitHubFacade

github_facade = GitHubFacade()

@github_controller_blueprint.route("/api/github/crear", methods=['POST'])
def create_github():
        try: 
            data = request.get_json()
            name = data["name"]
            description = data['description']
            token = data["token"]
            folders = data['folders']
            user = data['user']
            destination_repo = data['destination_repo']
            destination_path = data['destination_path']
            owner = data['owner']
            id_crea_type = data['id_crea_type']
        except KeyError as e:
            return jsonify({'error': f"Missing required field: {e.args[0]}"}), 400
        
        try: 
            github_facade.create_repository(name, description, token)
            github_facade.add_folders(folders, token, name)
            github_facade.send_file(id_crea_type, token, user, destination_repo, owner, destination_path)

            return jsonify({
                "code": 201,
                "status": True, 
                "message": "Repositorio creado correctamente"
            }), 201
        
        except Exception as e: 
            return jsonify({'error': f"Error al crear repositorio: {e}"}), 400
    
@github_controller_blueprint.route("/api/github/content", methods=['POST'])
def send_file():
    try: 
        data = request.get_json()
        user = data['user']
        destination_repo = data['destination_repo']
        destination_path = data['destination_path']
        owner = data['owner']
        id_crea_type = data['id_crea_type']
        token = data["token"]
    except KeyError as e: 
        return jsonify({'error': f"Missing required field: {e.args[0]}"}), 400
    
    try: 
        github_facade.send_file(id_crea_type, token, user, destination_repo, owner, destination_path)
        return jsonify({
            "code": 200,
            "status": True, 
            "message": "Archivos subidos correctamente"
        })
    except Exception as e: 
            return jsonify({'error': f"Ocurrio un error {e}"}), 400

    
    
