FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /consumer/requirements.txt

WORKDIR /consumer

RUN pip3 install -r requirements.txt

COPY . /consumer

ENTRYPOINT [ "python3" ]

CMD [ "consumer.py" ]