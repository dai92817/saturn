FROM ubuntu

MAINTAINER Dalei <guoyunlei#live.com>

RUN apt-get update -y && apt-get install git python python-pip -y
RUN cd /tmp \
        && git clone https://github.com/daleione/saturn.git \
        && cd saturn \
        && pip install -r requirements.txt

EXPOSE 8888

CMD ["python", "/tmp/saturn/hello.py"]
