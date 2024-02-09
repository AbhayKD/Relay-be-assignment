# Use an official Python runtime as the parent image
FROM python:3.11

# Set environment variable to ensure Python includes the directory in its search path
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

# Set the working directory in the container
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Set the default command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]