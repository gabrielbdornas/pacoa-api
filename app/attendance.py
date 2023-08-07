from flask import (
                   Blueprint,
                   current_app,
                   jsonify,
                   request,
                  )
import datetime
from sqlalchemy import func
from marshmallow import ValidationError
from .models import Recipient, Attendance
from .schemas import AttendanceSchema

attendance_blueprint = Blueprint('attendances', __name__)
model = Attendance()
schema = AttendanceSchema()
schemas = AttendanceSchema(many=True)

@attendance_blueprint.route('/attendances', methods=['GET'])
def get():
    try:
        attendance = model.query.all()
        return jsonify(schemas.dump(attendance)), 200
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

@attendance_blueprint.route('/attendances/<int:id>', methods=['GET'])
def get_by_id(id):
    try:
        attendance = model.query.get(id)
        return jsonify(schema.dump(attendance)), 200
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

@attendance_blueprint.route('/recipients/<int:recipient_id>/attendances', methods=['GET'])
def get_by_recipient(recipient_id):
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
        date = datetime.datetime.utcnow().date()
        attendances = current_app.db.session.query(Attendance). \
                      filter(Attendance.recipient_id == request.json['recipient_id']). \
                      filter(func.date(Attendance.date) == date). \
                      all()
        if len(attendances) > 0:
            raise ValidationError('Presence alread checked for this recipient in this date.')
        else:
            attendance = schema.load(request.json)
            current_app.db.session.add(attendance)
            current_app.db.session.commit()
            return jsonify(schema.dump(attendance)), 201
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

@attendance_blueprint.route('/attendances/<int:id>', methods=['PUT'])
def update(id):
    try:
        attendance = model.query.get(id)
        if attendance == None:
            raise ValidationError('Attendance id not exist.')
        else:
            update_attendance = model.query.filter(Attendance.id == id)
            update_attendance.update(request.json)
            current_app.db.session.commit()
            return jsonify(schema.dump(update_attendance.first())), 201
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401

@attendance_blueprint.route('/attendances/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        attendance = model.query.get(id)
        if attendance == None:
            raise ValidationError('Attendance id not exist.')
        else:
            current_app.db.session.delete(attendance)
            current_app.db.session.commit()
            return jsonify({'deleted': f'id: {id}.'}), 200
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)
        return jsonify(error.messages), 401
