from flask import Flask
from werkzeug.utils import find_modules, import_string


def register_blueprints(app):
    for name in find_modules('myapp.blueprints', include_packages=True):
        mod = import_string(name)
        if hasattr(mod, 'blueprint'):
            app.register_blueprint(mod.blueprint)


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(config or {})
    register_blueprints(app)
    # register_other_things(app)
    return app
