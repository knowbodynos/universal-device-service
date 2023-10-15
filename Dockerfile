FROM --platform=linux/amd64 python:3.9

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app

COPY src/ /app/
COPY tests/fixtures/ /app/static/

ENV DEFAULT_IMAGE "/app/static/example.jpg"

EXPOSE 80

CMD ["python", "/app/main.py"]
