# Stage 1: Base image with Python and dependencies
FROM python:3.12-slim AS base

# Install system dependencies as root
USER root
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    sudo git build-essential python-dev-is-python3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# (Optional) Setup a password-less sudo file for the new user
# COPY sudo-nopasswd /etc/sudoers.d/sudo-nopasswd

# Create a non-root user and set up a home directory
RUN useradd --create-home --shell /bin/bash appuser && usermod -aG sudo appuser

# Switch to the non-root user
USER appuser

# Set the working directory for the application
WORKDIR /home/appuser

# Stage 2: Install Python dependencies
FROM base AS python-dependencies

# Copy the requirements file and install dependencies
COPY --chown=appuser:appuser requirements.txt .
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -U pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Stage 3: Final stage with application code
FROM python-dependencies AS final

# Switch to the non-root user
USER appuser

# Set the working directory
WORKDIR /app

# Copy the application code with correct ownership
COPY --chown=appuser:appuser . .

# Expose the Gradio interface port
EXPOSE 7860

# Set up Gradio host
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Run the application
CMD ["python", "app.py"]