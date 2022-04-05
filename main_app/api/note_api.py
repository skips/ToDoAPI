from flask import Blueprint, request

from main_app.schemas.comment_schema import CommentSchema
from registry import get_registry
from main_app.schemas.note_schema import NoteSchema

note_api = Blueprint('note', __name__)

note_repo = get_registry()["NOTE_REPO"]


@note_api.route("/create-note", methods=["POST"])
def create_note():
    params = request.json
    name = params.get("name")
    text = params.get("text")
    board_id = params.get("board_id")
    note = note_repo.create_note(name=name, text=text, board_id=board_id)
    note_schema = NoteSchema()
    note_serialized = note_schema.dump(note)
    return note_serialized


@note_api.route("/get-note", methods=["GET"])
def get_note():
    params = request.args
    id = params.get("id")
    note = note_repo.get_note_by_id(id)
    note_schema = NoteSchema()
    note_serialized = note_schema.dump(note)
    comments_schema = CommentSchema(many=True, only=("id", "text"))
    comments_serialized = comments_schema.dump(note.comment.all())
    return {"note": note_serialized, "comments": comments_serialized}

@note_api.route("/get-note-all", methods=["GET"])
def get_note_all():
    note = note_repo.get_all_note()
    note_schema = NoteSchema(many=True)
    note_serialized = note_schema.dump(note)
    return {"notes": note_serialized}
