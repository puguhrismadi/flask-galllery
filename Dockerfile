# Gunakan base image Python yang lebih ringan
# Menggunakan base image Python yang ringan
FROM python:3.11-slim

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin dan menginstal dependensi terlebih dahulu agar build lebih efisien
COPY requirements.txt .
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

# Menyalin seluruh kode sumber ke dalam container
COPY . .

# Menetapkan variabel lingkungan untuk menggunakan virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Expose port 5000 untuk Flask
EXPOSE 5000

# Gunakan Gunicorn untuk menjalankan Flask dalam mode Production
CMD ["/app/venv/bin/gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "routes:app"]