from registry import get_registry

db = get_registry()['DB']


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    note_id = db.Column(db.Integer, db.ForeignKey("note.id"))
