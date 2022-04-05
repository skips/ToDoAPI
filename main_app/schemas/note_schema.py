from flask_marshmallow.sqla import SQLAlchemySchema
from marshmallow import fields
from main_app.schemas.comment_schema import CommentSchema


class NoteSchema(SQLAlchemySchema):
    id = fields.Integer(data_key='id')
    name = fields.String(data_key='name')
    text = fields.String(data_key='text')
    board_id = fields.Integer(data_key='board_id')
    comments = fields.Nested(CommentSchema, many=True, only=("id", "text"))
