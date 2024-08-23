##################################################
################## PYTHON BASE ###################
##################################################
# Stage 1: Base image with Python and dependencies
FROM python:3.12-slim AS base

# Install system dependencies as root
USER root
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    sudo git build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# (Optional) Setup a password-less sudo file for the new user
# COPY sudo-nopasswd /etc/sudoers.d/sudo-nopasswd

# Create a non-root user and set up a home directory
RUN useradd --create-home --shell /bin/bash appuser && usermod -aG sudo appuser

#################################################
################## PYTHON DEP ###################
#################################################
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
RUN git clone https://github.com/explosion/spaCy
RUN cd spaCy && pip install -r requirements.txt && \
    pip install --no-build-isolation . && cd ..

COPY --chown=appuser:appuser requirements.txt .
RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Clone and build spaCy from source within the same environment
RUN git clone https://github.com/explosion/spaCy
RUN cd spaCy && pip install -r requirements.txt && \
    # pip install --no-build-isolation . && cd ..
    pip install . && cd ..

# Copy the application code with correct ownership
COPY --chown=appuser:appuser . .

# Expose the Gradio interface port
EXPOSE 7860

# Set up Gradio host
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Run the application
CMD ["python", "app.py"]


---

##################################################
################## PYTHON BASE ###################
##################################################
# Stage 1: Base image with Python and dependencies
FROM python:3.12-slim AS base

# Install system dependencies as root
USER root
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    sudo git build-essential \
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
################## PYTHON DEP ###################
#################################################
FROM base AS python-dependencies

# Copy the requirements file and install dependencies
COPY --chown=appuser:appuser requirements.txt .
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