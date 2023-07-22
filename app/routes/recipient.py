from flask import (
                   Blueprint,
                   jsonify,
                  )
from ..models import recipient


blueprints = Blueprint('recipients', __name__)
model = recipient.Recipient()
schema = recipient.RecipientSchema
schemas = recipient.RecipientSchema(many=True)

@blueprints.route('/recipients', methods=['GET'])
def get():
    recipients = model.query.all()
    return jsonify(schemas.dump(recipients)), 200
