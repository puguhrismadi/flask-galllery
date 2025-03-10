from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Gallery

app = Flask(__name__)
app.config.from_object("config.Config")
db.init_app(app)
migrate = Migrate(app, db)  # Tambahkan ini

CORS(app)

@app.route('/gallery', methods=['GET'])
def get_images():
    images = Gallery.query.all()
    return jsonify([img.to_dict() for img in images])

@app.route('/gallery/<int:id>', methods=['GET'])
def get_image(id):
    image = Gallery.query.get_or_404(id)
    return jsonify(image.to_dict())

@app.route('/gallery', methods=['POST'])
def add_image():
    data = request.json
    new_image = Gallery(title=data['title'], description=data['description'], image_url=data['image_url'])
    db.session.add(new_image)
    db.session.commit()
    return jsonify(new_image.to_dict()), 201

@app.route('/gallery/<int:id>', methods=['PUT'])
def update_image(id):
    image = Gallery.query.get_or_404(id)
    data = request.json
    image.title = data.get('title', image.title)
    image.description = data.get('description', image.description)
    image.image_url = data.get('image_url', image.image_url)
    db.session.commit()
    return jsonify(image.to_dict())

@app.route('/gallery/<int:id>', methods=['DELETE'])
def delete_image(id):
    image = Gallery.query.get_or_404(id)
    db.session.delete(image)
    db.session.commit()
    return jsonify({"message": "Image deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
