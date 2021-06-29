# Base image
FROM python:3.8-alpine

#Copy all files from dir with Dockerfile and requirements.txt to /app folder in image
COPY . /app

# Cd into /app folder with (in this case only) the requirements.txt
WORKDIR /app

# Install python modules
RUN pip install -r requirements.txt

# Change into / as starting point of container
WORKDIR /

# When container runs it should start in a bash terminal
CMD ["ash"]

