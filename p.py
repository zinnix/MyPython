﻿#!/usr/bin/python

import http
import datetime
import random
import os ,http.cookiejar

"""
print("Set-Cookie:UserID=XYZ;\r\n")
print("Set-Cookie:Password=XYZ123;\r\n")
print("Set-Cookie:Expires=Tuesday, 31-Dec-2027 23:12:40 GMT\r\n")
print("Set-Cookie:Domain=www.tutorialspoint.com;\r\n")
print("Set-Cookie:Path=/perl;\n")
print("Content-type:text/html\r\n\r\n")

"""

print("")
print("<html>")
print("<head>")
print("</head>")
print("<body>")
print("<h1>Mark Loves Python</h1>")


# Import modules for CGI handling 
import cgi, cgitb 



# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
fish  = form.getvalue('fish')
beer  = form.getvalue('beer')

print("<h2>Hello: %s %s</h2>" % (first_name, last_name))
print("Fish:",fish==form.getvalue('fish'),"<br>")
print("Beer:",fish==form.getvalue('beer'),"<br>")
print("Gender:",form.getvalue('Gender'),"<br>")
print("About yourself:",form.getvalue('textcontent'),"<br>")
print("Country:",form.getvalue('Country'),"<br>")






print("<br>==================START==================<br>")





#for param in list(os.environ.keys()):
    #print(param,os.environ[param],"<br>")


cookie_string = os.environ.get('HTTP_COOKIE')
#print("HTTP_COOKIE=",cookie_string)
if 'HTTP_COOKIE' in list(os.environ.keys()):
    #print("<br>yes<br>")
    cookies = os.environ['HTTP_COOKIE']
    cookies = cookies.split(';')
    #print(("cookies=",cookies))
    handler = {}
    for cookie in cookies:
       cookie = cookie.split('=')
       handler[cookie[0]] = cookie[1]
       print(handler)

print("<br>==================FINISH==================<br>")

#print((list(os.environ.keys()),"<br>------------<br>"))  # holds all the environment variables 
for param in list(os.environ.keys()):
    #print(list(param,os.environ[param]),"<br>")
    if (param=="HTTP_COOKIE"):
        print("<br><br><hr><font color=blue size=+3>Here are your cookies driven from<b>",param,"</b>:</font><br>")
        print("complete string:<font color=green>",os.environ[param],"</font><br>")
        newss=os.environ[param].split(";")
        print (newss)
        #print("newss=",newss[1],"<br>")
        for n in newss:
            (key, value ) = n.split('=')
            first=key
            second=value
            print( "<font color=blue>",first, "</font>;",second,"<br>" )
    if  (param=="SERVER_SOFTWARE"):
        print("SERVER_SOFTWARE=",os.environ[param],"<br>")
print("</body>")
print("</html>")
