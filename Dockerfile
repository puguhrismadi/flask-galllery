# Gunakan base image Python
FROM python:3.11

# Set direktori kerja dalam container
WORKDIR /app

# Salin semua file dan meng-compile menjadi bytecode
COPY . .
RUN python -m compileall .

# Buat folder baru untuk menyimpan file hasil kompilasi
RUN mkdir -p /app/pycache && cp -r __pycache__/* /app/pycache/

# Hanya salin file dalam __pycache__
WORKDIR /app/pycache

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0
ENV DATABASE_URL=postgresql://postgres:spasi2025@192.168.7.26/gallery_db

# Expose port Flask
EXPOSE 5000

# Jalankan aplikasi dari file Python yang sudah dikompilasi
CMD ["python", "routes.cpython-311.pyc"]
