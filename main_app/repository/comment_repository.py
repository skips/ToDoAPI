from registry import get_registry
from main_app.models.comment import Comment


class CommentRepository(object):
    def __init__(self):
        self.db = get_registry()["DB"]

    def create_comment(self, text: str, note_id: int) -> Comment:
        comment = Comment(text=text, note_id=note_id)
        self.db.session.add(comment)
        self.db.session.commit()
        return comment

    def get_comment_by_id(self, id: str) -> Comment:
        comment = Comment.query.filter(Comment.id == id).first()
        return comment

    def get_all_comment(self) -> Comment:
        comment = Comment.query.all()
        return comment
