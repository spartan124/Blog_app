from flask_restx import Api
from flask import Blueprint
from app.main.controllers.auth_controller import api as auth_ns
from app.main.controllers.user_controller import api as user_ns
blueprint = Blueprint("api", __name__)
api = Api(blueprint,
        title = "Your Personal Blog",
        version = "1.0",
        description = "Passionate about writing? \n Ignite your passion, it's a blog app!!!"
        )

# api.add_namespace(auth_ns)
# api.add_namespace(user_ns, path="/api/user")