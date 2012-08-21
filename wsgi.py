import os
import sys
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'mezzanine')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mezzanineapp.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

