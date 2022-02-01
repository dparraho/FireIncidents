 FROM python:3.8.7-slim-buster
 ENV PYTHONUNBUFFERED 1
 WORKDIR /appuser/code
 ADD requirements.txt /appuser/code
 RUN pip install -r requirements.txt
 ADD --chown=appuser:appuser . /appuser/code/
 CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
 EXPOSE 8000