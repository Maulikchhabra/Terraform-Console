FROM python:3.9
WORKDIR /MyDjango
COPY . .
RUN pip install django
RUN pip install mysqlclient
CMD ["python", "manage.py", "runserver"]
