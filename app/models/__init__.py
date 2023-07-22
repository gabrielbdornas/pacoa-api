from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
ma = Marshmallow()

def configure_db(app):
    db.init_app(app)
    app.db = db # Não entendi bem, mas segundo ele é p ficar mais fácil e ter algo p chamar na rota

def configure_ma(app):
    ma.init_app(app)

class Model():
    id = db.Column(db.Integer, primary_key=True)

class ModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True # Não funcionando
