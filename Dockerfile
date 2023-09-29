FROM python:3
RUN pip install django
WORKDIR /opt
COPY . .
CMD [ "python3","manage.py","runserver", "0.0.0.0:1234" ] 
