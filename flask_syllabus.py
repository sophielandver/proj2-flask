"""
Very simple Flask web site, with one page
displaying a course schedule. The beginning date of each week 
is displayed and, in addition, the current week is highlighted. 

"""

import flask
from flask import render_template
from flask import request
from flask import url_for

import json
import logging

# Date handling 
import arrow # Replacement for datetime, based on moment.js
import datetime # But we still need time
from dateutil import tz  # For interpreting local times

# Our own module
import pre  # Preprocess schedule file


###
# Globals
###
app = flask.Flask(__name__)
schedule = "static/schedule.txt"  # This should be configurable
import CONFIG


import uuid
app.secret_key = str(uuid.uuid4())
app.debug=CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)


###
# Pages
###

@app.route("/")
@app.route("/index")
@app.route("/schedule")
def index():
  app.logger.debug("Main page entry")
  if 'schedule' not in flask.session:
      app.logger.debug("Processing raw schedule file")
      raw = open('static/schedule.txt')
      syllabus_list = pre.process(raw) #here you collect, week, date, project, and topic per week. List of dicts
      for entry in syllabus_list:   
        arrow_date_low = arrow.get(entry['date'], 'ddd MM/DD/YYYY')
        arrow_date_high = arrow_date_low.replace(weeks=+1)
        arrow_date_now = arrow.now()
        if arrow_date_low <= arrow_date_now < arrow_date_high:
            curr_week = entry['week']
        
      flask.session['cur_week'] = curr_week 
      flask.session['schedule'] = syllabus_list  

  return flask.render_template('syllabus.html') 


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] =  flask.url_for("index")
    return flask.render_template('page_not_found.html'), 404

#################
#
# Functions used within the templates
#
#################

@app.template_filter( 'fmtdate' )
def format_arrow_date( date ):
    try: 
        normal = arrow.get( date )
        return normal.format("ddd MM/DD/YYYY")
    except:
        return "(bad date)"


#############
#    
# Set up to run from cgi-bin script, from
# gunicorn, or stand-alone.
#


if __name__ == "__main__":
    # Standalone, with a dynamically generated
    # secret key, accessible outside only if debugging is not on
    print("NOT GOING TO RUN")
"""
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.debug=CONFIG.DEBUG
    app.logger.setLevel(logging.DEBUG)
    if app.debug: 
        print("Accessible only on localhost")
        app.run(port=CONFIG.PORT)  # Accessible only on localhost
    else:
        print("Opening for global access on port {}".format(CONFIG.PORT))
        app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    # Running from cgi-bin or from gunicorn WSGI server, 
    # which makes the call to app.run.  Gunicorn may invoke more than
    # one instance for concurrent service. 
    app.secret_key = CONFIG.secret_key
    app.debug=False
"""

