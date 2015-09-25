FROM ubuntu

MAINTAINER Dalei <guoyunlei#live.com>

RUN apt-get update -y && apt-get install git python python-pip -y
RUN mkdir /saturn
COPY . /saturn
WORKDIR /saturn
RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["python", "hello.py"]
