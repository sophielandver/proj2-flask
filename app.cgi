#! /usr/bin/env python3

""" For deployment on ix under CGI """

import site
from pathlib import Path  # For debugging
#
# The following should refer to your own 
# directories.  Broken into pieces so it's 
# easy to vary just the part that changes from 
# project to project.
#
ClassDir="~slandver/public_html/cis399/htbin"
ProjDir="{}/proj2-flask".format(ClassDir)
EnvLib="{}/env/lib/python3.4/site-packages".format(ProjDir)

# A little self-check to make sure we got it right ... 
p = Path(EnvLib)
assert p.exists() and p.is_dir()

site.addsitedir(EnvLib)  # Use the modules we installed

from wsgiref.handlers import CGIHandler
from flask_syllabus import app

CGIHandler().run(app)
