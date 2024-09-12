LABEL org.opencontainers.image.source=https://github.com/beecave-homelab/ollama-transcriptor

##################################################
################## PYTHON BASE ###################
##################################################
# Stage 1: Base image with Python and dependencies
FROM ubuntu:22.04 AS base

# Install system dependencies as root
USER root
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    sudo git build-essential \
    python3 python3-dev python3-pip python3-venv python-dev-is-python3 \
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

#################################################
################## PYTHON APP ###################
#################################################
FROM base AS final

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
# RUN git clone https://github.com/explosion/spaCy
RUN pip install -U pip setuptools wheel
    # && pip install spacy
# RUN cd spaCy && pip install -r requirements.txt && \
#     pip install --no-build-isolation . && cd ..
RUN PIP_CONSTRAINT=https://raw.githubusercontent.com/explosion/spacy/master/build-constraints.txt \
    pip install spacy --no-cache-dir

COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_lg

# Copy the application code with correct ownership
COPY --chown=appuser:appuser . .

# Expose the Gradio interface port
EXPOSE 7860

# Set up Gradio host
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Run the application
ENTRYPOINT ["python"]