from registry import get_registry
from main_app.models.note import Note


class NoteRepository(object):
    def __init__(self):
        self.db = get_registry()["DB"]

    def create_note(self, name: str, text: str, board_id: int) -> Note:
        note = Note(name=name, text=text, board_id=board_id)
        self.db.session.add(note)
        self.db.session.commit()
        return note

    def get_note_by_id(self, id: str) -> Note:
        note = Note.query.filter(Note.id == id).first()
        return note

    def get_all_note(self) -> Note:
        note = Note.query.all()
        return note
