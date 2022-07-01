FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /producer/requirements.txt

WORKDIR /producer

RUN pip3 install -r requirements.txt

COPY . /producer

ENTRYPOINT [ "python3" ]

CMD [ "producer.py" ]