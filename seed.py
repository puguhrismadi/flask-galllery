from faker import Faker
from models import db, Gallery
from routes import app

fake = Faker()

def seed_database(n=10):
    """Mengisi database dengan n data dummy."""
    with app.app_context():
        for _ in range(n):
            new_image = Gallery(
                title=fake.sentence(nb_words=3),
                description=fake.text(max_nb_chars=200),
                image_url=fake.image_url()
            )
            db.session.add(new_image)
        
        db.session.commit()
        print(f"{n} data dummy berhasil dimasukkan ke database!")

if __name__ == "__main__":
    seed_database(20)  # Masukkan 20 data dummy
