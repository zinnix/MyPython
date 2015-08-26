#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']
message=""

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())

   message =message+ 'The file "' + fn + '" was uploaded successfully to /tmp/' 
   
else:
   message = 'No file was uploaded'
   
print ("Content-type:text/html\r\n\r\n")
print("<html><body>   <p>%s</p></body></html>" % (message,))