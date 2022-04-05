from flask_marshmallow.sqla import SQLAlchemySchema
from marshmallow import fields


class CommentSchema(SQLAlchemySchema):
    id = fields.Integer(data_key="id")
    text = fields.String(data_key="text")
    note_id = fields.Integer(data_key="note_id")