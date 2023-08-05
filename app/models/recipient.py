from . import (
               db,
               Model,
               ModelSchema,
               )
from dotenv import load_dotenv
from io import StringIO
import os
import pandas as pd
import requests

class Recipient(db.Model, Model):
    name = db.Column(db.String(255), nullable=False)
    birthdate = db.Column(db.String(255))
    list_kind = db.Column(db.String(255))
    attendances = db.relationship('Attendance', backref='date', lazy=True)
    seed_files = [
        {
        'org_repo': 'gabrielbdornas/pacoa-dataset',
        'file_base_path': 'data/pacoa_junho_lista1.csv',
        'ref': '85a365ebce34e53be60ed4cd51e443d594225814',
        },
        {
        'org_repo': 'gabrielbdornas/pacoa-dataset',
        'file_base_path': 'data/pacoa_junho_lista2.csv',
        'ref': '85a365ebce34e53be60ed4cd51e443d594225814',
        },
    ]

    def __repr__(self):
        return f"Recipient(id: '{self.id}', name: '{self.name}', lista:'{self.list_kind}')"

    @classmethod
    def seed(cls):
        load_dotenv()
        recipients = []
        for file in cls.seed_files:
            file_name = file["file_base_path"].split('/')[-1]
            file_path = f'https://api.github.com/repos/{file["org_repo"]}/contents/{file["file_base_path"]}?ref={file["ref"]}'
            data = requests.get(
                file_path,
                headers={
                    'Accept': 'application/vnd.github.v3.raw',
                    'Authorization': f'token {os.getenv("GH_TOKEN")}',
                    }
            )
            string_io_obj = StringIO(data.text)
            df = pd.read_csv(string_io_obj, sep=",", index_col=0)
            df = df.reset_index()
            for index, row in df.iterrows():
                recipients.append({
                    'name': row['nome_completo'],
                    'list_kind': row['tipo'],
                })
        return recipients

class RecipientSchema(ModelSchema):

    class Meta():
        ModelSchema.Meta() # Não funcionando
        model = Recipient
        load_instance = True
