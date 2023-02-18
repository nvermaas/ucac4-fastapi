FROM python:3.9.7-slim

RUN apt-get update && apt-get install --no-install-recommends -y bash nano mc

ENV PYTHONUNBUFFERED 1
# RUN apk update && apk add bash && apk add nano && apk add mc

RUN mkdir /src
WORKDIR /src
COPY . /src/
RUN pip install -r requirements.txt
CMD ["uvicorn", "main_psycopg2:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]

# build the image like this:
# docker build -t ucac4-fastapi-psycopg2:latest .

# log into the container
# docker exec -it ucac4-fastapi-psycopg2 sh
