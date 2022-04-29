from flask import Flask
from flask_migrate import Migrate
from .models.commands import init_app
from .models.models import configure as config_db
from .models.serealizer import configure as config_ma


def create_app():  # config_env_var='FLASK_CONFIG'
    app = Flask(__name__)
    # app.config.from_envvar(config_env_var, silent=False)
    app.config.from_pyfile("production.cfg")
    
    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    init_app(app)

    from .views import bp_views
    app.register_blueprint(bp_views)

    from .models import bp_models
    app.register_blueprint(bp_models)

    from app.routes import bp_routes, routes_users, routes_account, routes_access, initial
    app.register_blueprint(bp_routes)

    return app
