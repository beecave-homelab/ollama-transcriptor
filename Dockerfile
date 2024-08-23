# Stage 1: Base image with Python and dependencies
FROM python:3.11-slim-bullseye AS base

# Install system dependencies as root
USER root
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    sudo git build-essential python-dev-is-python3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
git 
# (Optional) Setup a password-less sudo file for the new user
# COPY sudo-nopasswd /etc/sudoers.d/sudo-nopasswd

# Create a non-root user and set up a home directory
RUN useradd --create-home --shell /bin/bash appuser && usermod -aG sudo appuser

# Switch to the non-root user
USER appuser

# Set the working directory for the application
WORKDIR /home/appuser

# Stage 2: Final stage with application code and building spaCy from source
FROM python-base AS final

# Switch to the non-root user
USER appuser

# Set the working directory
WORKDIR /app

# Copy the requirements file and install general dependencies
RUN python -m venv venv && \
    . venv/bin/activate

# Set the PATH environment variable
ENV PATH="$PATH:/home/appuser/.local/bin"

# Clone and build spaCy from source within the same environment
RUN git clone https://github.com/explosion/spaCy /home/appuser/spaCy
WORKDIR /home/appuser/spaCy
RUN cd spaCy && pip install -r requirements.txt && \
    pip install --no-build-isolation . && cd ..

COPY --chown=appuser:appuser requirements.txt .
RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Clone and build spaCy from source within the same environment
RUN git clone https://github.com/explosion/spaCy /home/appuser/spaCy
WORKDIR /home/appuser/spaCy
RUN cd spaCy && pip install -r requirements.txt && \
    pip install --no-build-isolation . && cd ..

# Copy the application code with correct ownership
WORKDIR /app
COPY --chown=appuser:appuser . .

# Expose the Gradio interface port
EXPOSE 7860

# Set up Gradio host
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Run the application
CMD ["python", "app.py"]