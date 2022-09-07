FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD python manage.py migrate && python manage.py load_data && python manage.py runserver 0.0.0.0:8000