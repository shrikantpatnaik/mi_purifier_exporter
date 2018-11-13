FROM python:3

WORKDIR /app

ADD exporter.py /app
ADD requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

CMD [ "python", "exporter.py", "/config/purifiers.json" ]

