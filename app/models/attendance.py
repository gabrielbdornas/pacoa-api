from . import (
               db,
               Model,
               ModelSchema,
               )
from .recipient import Recipient
from dotenv import load_dotenv
import datetime
from io import StringIO
import os
import pandas as pd
import requests

now = datetime.datetime.utcnow

class Attendance(db.Model, Model):
    date = db.Column(db.DateTime, default=now, nullable=False)
    observation = db.Column(db.String(255))
    recipient_id = db.Column(db.Integer, db.ForeignKey('recipient.id'), nullable=False)

    def __repr__(self):
        recipient = Recipient.query.get(self.recipient_id)
        return f"Attendance(recipient: '{recipient.name}', date: '{self.date}', observation:'{self.observation}')"

class AttendanceSchema(ModelSchema):

    class Meta():
        ModelSchema.Meta() # Não funcionando
        model = Attendance
        load_instance = True
