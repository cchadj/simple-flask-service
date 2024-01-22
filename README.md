# Simple Flask Service

This is a simple Flask web service created to demonstrate how to create a web service and deploy it using Docker.

## Manual Installation & Running

Dependencies:
* python 3.9

1.  Install requirements
    ```bash
    pip install -r requirements.txt
    ```
3. Configure environment variables. \
   Copy `.env.manual` file to `.env`
    ```bash
    cp .env.manual .env
    ```
2. Launch service
    ```bash
    python app.py
    ```

## Installation & Running with Docker

1. Configure environment variables. \
   Copy `.env.docker` file to `.env`
    ```bash
    cp .env.docker .env
    ```
2. Build docker image
    ```bash
        docker build -t simple-flask-service .
    ```
3. Run docker service
    ```bash
        docker run -p 8888:8888 simple-flask-service
    ```