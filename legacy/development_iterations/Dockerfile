# Use Python 3.11 slim image for optimal size and performance
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app
RUN chown -R app:app /app
USER app

# Create directories for logs and data
RUN mkdir -p /app/logs /app/data /app/sanctuary_data /app/sanctuary_logs

# Health check - Cloud Run will set PORT environment variable  
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:${PORT:-8080}/health || exit 1

# Expose port (Cloud Run will set PORT env var dynamically)
EXPOSE 8080

# Set default environment
ENV ENVIRONMENT=production \
    LOG_LEVEL=INFO \
    API_HOST=0.0.0.0 \
    API_PORT=8080

# Set PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Default command - Use refactored production server
CMD ["python", "scripts/servers/refactored_production_server.py"]
