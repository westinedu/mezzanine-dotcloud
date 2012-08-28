import os
import sys
print os.path.abspath(os.path.join(os.path.dirname(__file__),'mezzanine'))
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
print settings_dir
print PROJECT_ROOT
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'hellodjango/templates/'),
)
print TEMPLATE_DIRS




