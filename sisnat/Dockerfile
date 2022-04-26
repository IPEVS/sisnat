FROM python:3.9

EXPOSE 8000

RUN apt-get update && apt-get install -y gettext

WORKDIR /deploy/sisnat

COPY requirements/ /deploy/sisnat/requirements/

RUN pip install --upgrade pip && pip install -r requirements/deploy.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
