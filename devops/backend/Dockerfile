FROM python:3.12-slim-bookworm
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apt-get update && \
    apt-get install -y locales apt-transport-https ca-certificates unixodbc unixodbc-dev gnupg2 wget git && \
    apt-get install -y build-essential libffi-dev libldap2-dev libsasl2-dev libssl-dev python3-dev libpq-dev && \
    apt-get install -y librdkafka-dev libxml2-dev libxslt-dev &&  \
    apt-key adv --fetch-keys https://packages.microsoft.com/keys/microsoft.asc && \
    wget -S -O - https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=y apt-get install -y mssql-tools18 msodbcsql18 && \
    echo ru_RU.UTF-8 UTF-8 >> /etc/locale.gen && \
    locale-gen && \
    apt-get remove wget gnupg2 -y && \
    apt-get autoremove -y && \
    apt-get clean autoclean && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/
RUN     pip install poetry=="1.7.1"

COPY /src/backend/ /app/
RUN poetry config virtualenvs.create false && poetry install --no-cache

RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD gunicorn --config gunicorn.conf.py
