# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY fetch_hf_data.py .

# Install any needed packages specified in requirements.txt
RUN pip install requests

# Run fetch_hf_data.py when the container launches
CMD ["python", "./fetch_hf_data.py"]
