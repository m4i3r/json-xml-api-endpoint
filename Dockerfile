FROM python:alpine3.16
COPY src /app
WORKDIR /app
RUN apk add build-base
RUN python3 -m pip install fastapi
RUN python3 -m pip install "uvicorn[standard]"
CMD ["uvicorn", "main:app", "--reload", "--port", "80", "--host", "0.0.0.0"]