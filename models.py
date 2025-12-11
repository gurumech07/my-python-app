from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f"<Task {self.id} {self.title!r}>"
