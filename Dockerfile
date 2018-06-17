FROM python:3

RUN apt-get update -y
RUN apt-get -y install vim
RUN mkdir -p /opt/ask

COPY . /opt/ask
WORKDIR /opt/ask

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT      ["python", "ask.py"]
