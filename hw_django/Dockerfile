FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ../hw_django .

CMD [ "python", "manage.py", "runserver" ]