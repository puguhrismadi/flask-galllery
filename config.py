import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:spasi2025@192.168.7.126/gallery_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
