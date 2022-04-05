from flask import Blueprint, request

from registry import get_registry
from main_app.schemas.comment_schema import CommentSchema


comment_api = Blueprint('comment', __name__)

comment_repo = get_registry()["COMMENT_REPO"]


@comment_api.route("/create-comment", methods=["POST"])
def create_comment():
    params = request.json
    text = params.get("text")
    note_id = params.get("note_id")
    comment = comment_repo.create_comment(text=text, note_id=note_id)
    comment_schema = CommentSchema()
    comment_serialized = comment_schema.dump(comment)
    return comment_serialized


@comment_api.route("/get-comment", methods=["GET"])
def get_note():
    params = request.args
    id = params.get("id")
    comment = comment_repo.get_comment_by_id(id)
    comment_schema = CommentSchema()
    comment_serialized = comment_schema.dump(comment)
    return comment_serialized


@comment_api.route("/get-comment-all", methods=["GET"])
def get_comment_all():
    comments = comment_repo.get_all_comment()
    comment_schema = CommentSchema(many=True)
    comment_serialized = comment_schema.dump(comments)
    return {"boards": comment_serialized}
