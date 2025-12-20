# BUILD STAGE - Installs dependencies only (cached, not in prod image)
# Use hardened light weight secure image that has up to 95% less vulnerabilities 
FROM dhi.io/docker/dockerfile:1.5 AS builder

#Sets working directory for build artifacts
WORKDIR /app

# Copies only requirements (enables layer caching on deps change)
COPY requirements.txt .

# Installs Python packages as non-root user, no cache to reduce size
RUN pip install --no-cache-dir -r requirements.txt

# Production stage - OFFICIAL Docker Hub Python Alpine (hardened)
FROM dhi.io/python:3.11-alpine AS prod
# Pre-scanned by Docker Scout, minimal Alpine base (~50MB), non-root ready

# Copies ONLY app code (excludes .git, tests, docs - reduces attack surface)
COPY app.py /app/

#Sets working directory for build artifacts
WORKDIR /app

# SECURITY HARDENING - Production best practices
# Runs as non-root (no privilege escalation if compromised)
USER 65532:65532

# Documents container port (doesn't actually open it)
EXPOSE 5000

# Flask app entrypoint config
ENV FLASK_APP=app.py

# Runs Flask via Python module (more reliable than CMD ["flask", "run"])
CMD ["/usr/local/bin/python", "-m", "flask", "run", "--host=0.0.0.0"]
