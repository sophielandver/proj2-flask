Author: Sophie Landver

Path to project2 on ix: slandver@ix-trusty: ~/public_html/cis399/htbin/proj2-flask 

URL: http://ix.cs.uoregon.edu/~slandver/cis399/htbin/proj2-flask/app.cgi/
(I could not get this ix cgi URL to work). 


# proj2-flask
A starter project for using the Flask framework

## What this project does:
This is a flask web page displaying the CIS 399 course schedule for Winter 2016. The beginning date of each week is displayed and the current week is highlighted. 

## How to set up on your workspace:

Copy CONFIG.base.py to CONFIG.py, and edit it. You can probably use
the standard port 5000 if you are the only user of the computer. 

type `make install`

You might have to edit the Makefile to find the right version of
pyvenv.  

If you can run flask applications in your development environment, the
application would be run by
`   python3 syllabus.py`
and then reached with url
`   http://localhost:5000`

This should work on MacOS, or on your own Linux box if you have one. I
don't know about Windows. 
 

