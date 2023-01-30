FROM python:3.10

COPY . /app
RUN pip install -r /app/requirements.txt

EXPOSE 8000

WORKDIR /app

CMD ["bash", "docker-entrypoint.sh"]