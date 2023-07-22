from . import (
               db,
               Model,
               ModelSchema,
               )

class Recipient(db.Model, Model):
    name = db.Column(db.String(255), nullable=False)
    birthdate = db.Column(db.String(255))
    list_kind = db.Column(db.String(255))

    def __repr__(self):
        return f"Recipient(id: '{self.id}', name: '{self.name}', lista:'{self.list_kind}')"


class RecipientSchema(ModelSchema):

    class Meta():
        ModelSchema.Meta() # Não funcionando
        model = Recipient
        load_instance = True
