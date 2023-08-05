from .models import (
                     ma,
                     Recipient,
                     Attendance,
)

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
