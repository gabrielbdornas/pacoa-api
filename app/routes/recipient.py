from flask import (
                   Blueprint,
                   jsonify,
                  )
from ..models import recipient


blueprints = Blueprint('recipients', __name__)
model = recipient.Recipient()
schema = recipient.RecipientSchema

@blueprints.route('/recipients', methods=['GET'])
def get_recipients():
    bs = schema(many=True)
    recipients = model.query.all()
    return bs.jsonify(bs.dump(recipients)), 200
