from registry import get_registry

db = get_registry()['DB']


class Board(db.Model):
    __tablename__ = 'board'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    notes = db.relationship("Note", backref="board_owner")
