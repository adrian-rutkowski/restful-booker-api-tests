FROM python:3-alpine

RUN apk update

WORKDIR /container

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . /container