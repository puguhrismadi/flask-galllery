from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    image_url = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description, "image_url": self.image_url}
