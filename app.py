import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from registry import get_registry


def _register_blueprints(app):
    from main_app.api.board_api import board_api
    app.register_blueprint(board_api,  url_prefix='/api/v1/board')
    from main_app.api.note_api import note_api
    app.register_blueprint(note_api,  url_prefix='/api/v1/note')
    from main_app.api.comment_api import comment_api
    app.register_blueprint(comment_api,  url_prefix='/api/v1/comment')


def create_app() -> Flask:
    app = Flask(__name__)
    reg = get_registry()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DB_URL')
    db = SQLAlchemy(
        app,
        session_options={
            "autoflush": False,
            # "autocommit": True
        }
    )
    db.init_app(app)
    Migrate(app, db)
    reg["DB"] = db
    reg["MA"] = Marshmallow(app)

    from main_app.repository.board_repository import BoardRepository
    reg["BOARD_REPO"] = BoardRepository()
    from main_app.repository.note_repository import NoteRepository
    reg["NOTE_REPO"] = NoteRepository()
    from main_app.repository.comment_repository import CommentRepository
    reg["COMMENT_REPO"] = CommentRepository()

    _register_blueprints(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
