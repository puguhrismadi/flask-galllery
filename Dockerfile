# Gunakan base image Python yang lebih ringan
FROM python:3.11-slim

# Set direktori kerja dalam container
WORKDIR /app

# Salin file yang diperlukan
COPY . .

# Install dependencies dalam virtual environment && remove all file extension py after build
RUN python -m venv venv && \
    ./venv/bin/pip install --no-cache-dir -r requirements.txt && \
    mkdir -p /app/pycache && \
    find /app -type f -name "*.py" -exec rm -f {} \;

# Set environment variables untuk Flask dan Database
ENV FLASK_APP=routes
ENV FLASK_ENV=production
ENV DATABASE_URL=postgresql://postgres:spasi2025@172.17.0.4/gallery_db

# Expose port 5000 untuk Flask
EXPOSE 5000

# Gunakan Gunicorn untuk menjalankan Flask dalam mode Production
CMD ["/app/venv/bin/gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "routes:app"]