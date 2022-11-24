FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install --upgrade pip
COPY . /code/
RUN pip install -r requirements.txt

EXPOSE $PORT

CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
