FROM python:3.14-slim
WORKDIR /app1
COPY . /app1
CMD [ "python", "main.py" ]