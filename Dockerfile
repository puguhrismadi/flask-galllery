# Gunakan base image Python
FROM python:3.11

# Set direktori kerja dalam container
WORKDIR /app

# Salin semua file ke dalam container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=routes.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DATABASE_URL=postgresql://postgres:spasi2025@192.168.7.126/gallery_db

# Expose port Flask
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "routes.py"]
