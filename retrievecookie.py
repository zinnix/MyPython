#!/usr/bin/python

# Import modules for CGI handling 
#from os import environ
from http import cookies
import os
import cgi, cgitb

print ("Content-type:text/html\r\n\r\n")
print ("*********<br>")

for param in list(os.environ.keys()):
    #print (param,os.environ[param],"<br>")
    if (param=="HTTP_COOKIE"):
        print((param,"<br>"))
        newparam=os.environ[param].split(";")
        #print (os.environ[param])
        print ("<br><br><br><br><br>")
        print (newparam)
        #print ("<b>%20s</b>: %s<br>" % (param, os.environ[param]))


"""
        for cookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
            (key, value ) = split(cookie, '=')
            if key == "UserID":
                user_id = value
            if key == "Password":
                password = value

print ("User ID  = %s" % user_id)
print ("Password = %s" % password)



if environ.has_key('HTTP_COOKIE'):
   for cookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
      (key, value ) = split(cookie, '=');
      if key == "UserID":
         user_id = value

      if key == "Password":
         password = value

print ("User ID  = %s" % user_id)
print ("Password = %s" % password)


"""