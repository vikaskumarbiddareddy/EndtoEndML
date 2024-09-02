FROM python:3.8-slim-buster
WORKDIR /service
COPY requirements.txt .
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python3", "app.py" ]