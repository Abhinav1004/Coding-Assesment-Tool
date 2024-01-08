FROM public.ecr.aws/docker/library/python:3.10-slim

COPY src/. src/.
COPY config/. config/.
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ARG BRANCH
ENV app_env=$BRANCH

CMD uvicorn src.main:app --host 0.0.0.0 --port 5000
