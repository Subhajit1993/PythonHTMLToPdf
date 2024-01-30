# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Update the system and install Python
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0


# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py"]