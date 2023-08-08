from .models import (
                     ma,
                     User,
                     Recipient,
                     Attendance,
)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class RecipientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipient
        load_instance = True

class AttendanceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Attendance
        load_instance = True
        include_fk = True
        include_relationships = True
