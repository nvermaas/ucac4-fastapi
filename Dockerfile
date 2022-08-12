#FROM python:3.6.7-slim
#FROM python:3.10-slim
FROM python:3.9.7-slim

RUN apt-get update && apt-get install --no-install-recommends -y bash nano mc

ENV PYTHONUNBUFFERED 1
# RUN apk update && apk add bash && apk add nano && apk add mc

RUN mkdir /src
WORKDIR /src
COPY . /src/
RUN pip install -r requirements/prod.txt
CMD exec uvicorn main:app --reload

# build the image like this:
# docker build -t ucac4-fastapi:latest .

# log into the container
# docker exec -it ucac4-fastapi sh