
FROM python:3.8-slim-buster
VOLUME ["/app"]
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY server.py /app/server.py
COPY language_detector.py /app/language_detector.py
RUN apt-get update
RUN apt-get install -y wget 
RUN wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
COPY lid.176.bin /app/
RUN apt-get install -y python3-dev build-essential
RUN pip3 install -r requirements.txt

EXPOSE 8000


CMD ["uvicorn", "server:app", "--host", "0.0.0.0"]
