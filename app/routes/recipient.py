from flask import (
                   Blueprint,
                   current_app,
                   jsonify,
                   request,
                  )
from marshmallow import ValidationError
from ..models import recipient


blueprints = Blueprint('recipients', __name__)
model = recipient.Recipient()
schema = recipient.RecipientSchema()
schemas = recipient.RecipientSchema(many=True)

@blueprints.route('/recipients', methods=['GET'])
def get():
    recipients = model.query.all()
    return jsonify(schemas.dump(recipients)), 200

@blueprints.route('/recipients', methods=['POST'])
def create():
    try:
        recipient = schema.load(request.json)
        current_app.db.session.add(recipient)
        current_app.db.session.commit()
        return jsonify(schema.dump(recipient)), 201
    except ValidationError as error:
        print(error.messages)  # => {"email": ['"foo" is not a valid email address.']}
        print(error.valid_data)  # => {"name": "John"}
        return jsonify(error.messages), 401
