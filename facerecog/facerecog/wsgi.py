"""
WSGI config for facerecog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

# wsgi.py
import os
import sys
import pymysql # import pymysql

pymysql.install_as_MySQLdb() # call this method before any Django import

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facerecog.settings')

application = get_wsgi_application()

