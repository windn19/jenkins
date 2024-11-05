FROM python:3.10
LABEL authors="dmitry"

ADD . /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

CMD ["bin/bash", "/app/pipeline.sh"]
