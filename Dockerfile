FROM python:3.13.1-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

ENV DJANGO_SETTINGS_MODULE=Backend_api.settings

ENV PYTHONUNBUFFERED=1

CMD ["python" , "manage.py" , "runserver" , "0.0.0.0:8000"]