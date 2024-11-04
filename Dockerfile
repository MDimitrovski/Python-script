FROM python:3.9-slim

# setting the working directory in the container
WORKDIR /app

# Coping the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run fetch_data.py when the container launches
CMD ["python", "fetch_data.py"]
