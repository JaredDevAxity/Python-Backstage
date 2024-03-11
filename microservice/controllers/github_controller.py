from flask import jsonify, request
from . import github_controller_blueprint
from ..facade import GitHubFacade

github_facade = GitHubFacade()

@github_controller_blueprint.route("/api/github/crear", methods=['POST'])
def create_github():
    if request.method == 'POST': 
        try: 
            data = request.get_json()
            name = data["name"]
            description = data['description']
            token = data["token"]
            folders = data['folders']
        except KeyError as e:
            return jsonify({'error': f"Missing required field: {e.args[0]}"}), 400
        
        try: 
            github_facade.create_repository(name, description, token)
        except Exception as e: 
            return jsonify({'error': f"Error al crear repositorio: {e}"}), 400
        
        try: 
             github_facade.add_folders(folders, token, name)
        except Exception as e: 
            return jsonify({'error': f"Error al crear repositorio: {e}"}), 400
        
        return "Repositorio creado correctamente"
        
    else: 
        return jsonify({'error': 'Método no permitido'}), 500
    
@github_controller_blueprint.route("/api/github/content", methods=['POST'])
def send_file():
    try: 
        data = request.get_json()
        id_crea_type = data['id_crea_type']
        token = data["token"]
    except KeyError as e: 
        return jsonify({'error': f"Missing required field: {e.args[0]}"}), 400
    
    try: 
        response = github_facade.send_file(id_crea_type, token)
        return jsonify({
            "code": 200,
            "status": True, 
            "message": response
        })
    except Exception as e: 
            return jsonify({'error': f"Ocurrio un error {e}"}), 400

    
    
