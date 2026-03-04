# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


# Stage 2: Production
FROM python:3.11-slim AS production

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq5 \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* \
    && rm -rf /wheels

# Create non-root user
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

# Copy project and entrypoint
COPY . .
COPY entrypoint.sh /entrypoint.sh

# Set permissions BEFORE switching user
RUN chmod +x /entrypoint.sh && \
    mkdir -p /app/staticfiles /app/media && \
    chown -R appuser:appgroup /app && \
    chown appuser:appgroup /entrypoint.sh

# Switch to non-root user
USER appuser

EXPOSE 8000

CMD ["/entrypoint.sh"]