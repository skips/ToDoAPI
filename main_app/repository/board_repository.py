from registry import get_registry
from main_app.models.board import Board


class BoardRepository(object):

    def __init__(self):
        self.db = get_registry()["DB"]

    def create_board(self, name: str) -> Board:
        board = Board(name=name)
        self.db.session.add(board)
        self.db.session.commit()
        return board

    def get_board_by_id(self, id: str) -> Board:
        board = Board.query.filter(Board.id == id).first()
        return board

    def get_all_board(self) -> Board:
        board = Board.query.all()
        return board
