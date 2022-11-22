FROM python:3.7

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python", "./run_server.py"]

CMD ["run_server.py" ]

EXPOSE 5000