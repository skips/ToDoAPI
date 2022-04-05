from flask import Blueprint, request
from registry import get_registry
from main_app.schemas.board_schema import BoardSchema


board_api = Blueprint('board', __name__)

board_repo = get_registry()["BOARD_REPO"]


@board_api.route("/create-board", methods=["POST"])
def create_board():
    params = request.json
    name = params.get("name")
    board = board_repo.create_board(name=name)
    board_schema = BoardSchema()
    board_serialized = board_schema.dump(board)
    return board_serialized


@board_api.route("/get-board", methods=["GET"])
def get_board():
    params = request.args
    id = params.get("id")
    board = board_repo.get_board_by_id(id)
    board_schema = BoardSchema()
    board_serialized = board_schema.dump(board)
    return board_serialized


@board_api.route("/get-board-all", methods=["GET"])
def get_note_all():
    boards = board_repo.get_all_board()
    board_schema = BoardSchema(many=True)
    board_serialized = board_schema.dump(boards)
    return {"boards": board_serialized}
