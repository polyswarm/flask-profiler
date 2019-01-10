# -*- coding: utf8 -*-
import click
import flask_profiler

from flask import Flask

app = Flask(__name__)

def init_app(app, db_uri, auth_user, auth_password):
    app.config['flask_profiler'] = {
        'enabled': True,
        'verbose': False,
        'endpointRoot': '',
        'measurement': False,
        'gui': True,
        'storage': {
            'engine': 'sqlalchemy',
            'db_url': db_uri,
        },
    }

    if auth_user and auth_password:
        app.config['flask_profiler']['basicAuth'] = {
            'enabled': True,
            'username': auth_user,
            'password': auth_password,
        }
    else:
        app.config['flask_profiler']['basicAuth'] = {
            'enabled': False
        }

    flask_profiler.init_app(app)

@click.command()
@click.option('--db-uri', envvar='DB_URI',
              help='URI for the deployment database')
@click.option('--auth-user', envvar='AUTH_USER', default='admin',
              help='Username for HTTP basic auth')
@click.option('--auth-password', envvar='AUTH_PASSWORD',
              help='Password for HTTP basic auth')
@click.option('--host', envvar='HOST', default='0.0.0.0',
              help='Address to listen on')
@click.option('--port', envvar='PORT', default=5000,
              help='Address to listen on')
def main(db_uri, auth_user, auth_password, host, port):
    init_app(app, db_uri, auth_user, auth_password)
    app.run(host=host, port=port)

