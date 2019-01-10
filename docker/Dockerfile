FROM python:3.6-slim-stretch
LABEL maintainer="PolySwarm Developers <info@polyswarm.io>"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN set -x && pip install --no-cache-dir -r requirements.txt
RUN set -x && pip install gunicorn

COPY . .
RUN set -x && pip install .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-k", "gevent", "-w", "4", "flask_profiler.wsgi"]
