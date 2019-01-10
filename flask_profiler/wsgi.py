import os
from .__main__ import init_app, app as application

init_app(application, os.environ.get('DB_URI'), os.environ.get('AUTH_USER', 'admin'), os.environ.get('AUTH_PASSWORD'))
