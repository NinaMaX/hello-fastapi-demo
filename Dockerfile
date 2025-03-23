# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working dir.
WORKDIR /app

# Copy uv dependencies.
COPY pyproject.toml .python-version uv.lock ./

# Install the application dependencies.
RUN uv sync --frozen --no-cache

# Copy the application into the container.
COPY ./app .

# Indicate the port for correct usage.
EXPOSE 80

# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "app.py", "--port", "80", "--host", "0.0.0.0"]