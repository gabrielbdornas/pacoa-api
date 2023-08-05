from flask import (
                   Blueprint,
                   current_app,
                   jsonify,
                   request,
                  )
from marshmallow import ValidationError
from .models import Recipient, Attendance
from .schemas import AttendanceSchema

attendance_blueprint = Blueprint('attendances', __name__)
model = Attendance()
schema = AttendanceSchema()
schemas = AttendanceSchema(many=True)

@attendance_blueprint.route('/recipients/<int:recipient_id>/attendances', methods=['GET'])
def get(recipient_id):
    try:
        recipient = Recipient.query.get(recipient_id)
        attendances = recipient.attendances
        return jsonify(schemas.dump(attendances)), 200
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

@attendance_blueprint.route('/recipients/attendances', methods=['POST'])
def create():
    try:
        attendance = schema.load(request.json)
        current_app.db.session.add(attendance)
        current_app.db.session.commit()
        return jsonify(schema.dump(attendance)), 201
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

# @attendance_blueprint.route('/recipients/<int:id>', methods=['PUT'])
# def update(id):
#     try:
#         # import ipdb; ipdb.set_trace(context=10)
#         update_recipient = model.query.filter(recipient.Recipient.id == id)
#         update_recipient.update(request.json)
#         current_app.db.session.commit()
#         return jsonify(schema.dump(update_recipient.first())), 201
#     except ValidationError as error:
#         print(error.messages)
#         print(error.valid_data)
#         return jsonify(error.messages), 401

# @attendance_blueprint.route('/recipients/<int:id>', methods=['DELETE'])
# def delete(id):
#     try:
#         recipient = model.query.get(id)
#         current_app.db.session.delete(recipient)
#         current_app.db.session.commit()
#         return jsonify(schema.dump(recipient)), 200
#     except ValidationError as error:
#         print(error.messages)
#         print(error.valid_data)
#         return jsonify(error.messages), 401
