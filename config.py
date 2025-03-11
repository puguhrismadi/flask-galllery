import os
import logging
from sqlalchemy import create_engine

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:spasi2025@172.17.0.4/gallery_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def test_db_connection():
        """Menguji koneksi ke database PostgreSQL."""
        try:
            engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
            with engine.connect() as connection:
                logger.info("✅ Koneksi ke database PostgreSQL BERHASIL!")
        except Exception as e:
            logger.error("❌ Gagal terhubung ke database PostgreSQL!")
            logger.error(f"Detail Error: {e}")

# Jalankan pengecekan koneksi saat konfigurasi dimuat
if __name__ == "__main__":
    Config.test_db_connection()
