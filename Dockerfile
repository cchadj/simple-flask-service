FROM python:3.9-slim-bookworm

WORKDIR /usr/src/app

COPY . .

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
