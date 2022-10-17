FROM python

RUN mkdir code
COPY . /code
WORKDIR /code

RUN python -m pip install --upgrade-pip
RUN python -m pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=app.py
ENTRYPOINT["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]