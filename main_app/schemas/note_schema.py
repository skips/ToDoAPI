from flask_marshmallow.sqla import SQLAlchemySchema
from marshmallow import fields


class NoteSchema(SQLAlchemySchema):
    id = fields.Integer(data_key='id')
    name = fields.String(data_key='name')
    text = fields.String(data_key='text')
    board_id = fields.Integer(data_key='board_id')
