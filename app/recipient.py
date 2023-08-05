from flask import (
                   Blueprint,
                   current_app,
                   jsonify,
                   request,
                  )
from marshmallow import ValidationError
from .attendance import attendance_blueprint
from .models import Recipient
from .schemas import RecipientSchema

recipient_blueprint = Blueprint('recipients', __name__)
recipient_blueprint.register_blueprint(attendance_blueprint)

model = Recipient()
schema = RecipientSchema()
schemas = RecipientSchema(many=True)

@recipient_blueprint.route('/recipients', methods=['GET'])
def get():
    try:
        recipients = model.query.all()
        return jsonify(schemas.dump(recipients)), 200
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

@recipient_blueprint.route('/recipients/<int:id>', methods=['GET'])
def get_by_id(id):
    try:
        recipient = model.query.get(id)
        return jsonify(schema.dump(recipient)), 200
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

@recipient_blueprint.route('/recipients/substring/<string:substring>', methods=['GET'])
def get_by_substring(substring):
    try:
        recipients = model.query.filter(
            recipient.Recipient.name.startswith(substring)
        ).all()
        return jsonify(schemas.dump(recipients)), 200
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

@recipient_blueprint.route('/recipients', methods=['POST'])
def create():
    try:
        recipient = schema.load(request.json)
        current_app.db.session.add(recipient)
        current_app.db.session.commit()
        return jsonify(schema.dump(recipient)), 201
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

@recipient_blueprint.route('/recipients/<int:id>', methods=['PUT'])
def update(id):
    try:
        # import ipdb; ipdb.set_trace(context=10)
        update_recipient = model.query.filter(recipient.Recipient.id == id)
        update_recipient.update(request.json)
        current_app.db.session.commit()
        return jsonify(schema.dump(update_recipient.first())), 201
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

@recipient_blueprint.route('/recipients/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        recipient = model.query.get(id)
        current_app.db.session.delete(recipient)
        current_app.db.session.commit()
        return jsonify(schema.dump(recipient)), 200
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401
