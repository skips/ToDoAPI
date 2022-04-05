from flask_marshmallow.sqla import SQLAlchemySchema
from marshmallow import fields

from main_app.schemas.note_schema import NoteSchema


class BoardSchema(SQLAlchemySchema):
    id = fields.Integer(data_key="id")
    name = fields.String(data_key="name")
    notes = fields.Nested(NoteSchema, many=True, only=("id", "name", "text"))
