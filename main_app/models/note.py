from registry import get_registry

db = get_registry()['DB']


class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.String)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
