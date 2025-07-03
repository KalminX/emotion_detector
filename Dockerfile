# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies and curl for uv install
RUN apt-get update && apt-get install -y \
    curl libglib2.0-0 libsm6 libxext6 libxrender-dev \
    ffmpeg build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv globally or make it available in PATH for the build
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# Add uv to PATH for the current and subsequent layers
ENV PATH="/root/.local/bin:$PATH"

# Copy only the requirements file first to leverage Docker cache
# This ensures requirements.txt is present before uv tries to use it
COPY requirements.txt .

# Install dependencies using uv
# This step will now find requirements.txt
RUN uv venv && uv pip install -r requirements.txt

# Copy the rest of your project files
# This step should happen after dependencies are installed if they rely on requirements.txt
COPY . .

# Activate the uv venv for runtime (already set by uv venv, but explicit is good)
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Expose the port
EXPOSE 5000

# Run the app with Gunicorn via uv venv
CMD ["sh", "-c", "/app/.venv/bin/gunicorn --bind 0.0.0.0:$PORT app:app"]
