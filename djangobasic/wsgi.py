"""
WSGI config for djangobasic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
# File ที่ใช้เก็บข้อมูล Project สำหรับการ Deployment(Production)

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobasic.settings')

application = get_wsgi_application()
