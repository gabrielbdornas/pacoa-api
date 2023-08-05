from flask import Flask
from flask_migrate import Migrate
from .models import configure_db, configure_ma


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure_db(app)
    configure_ma(app)

    Migrate(app, app.db)

    from .recipient import recipient_blueprint
    app.register_blueprint(recipient_blueprint)

    return app
