#!/usr/bin/python

import http
import datetime
import random
import os ,http.cookiejar


def CountingMinutesI(str):     
    
    s=str.split("-")
    s1=s[0].split(":")
    start_24=s[0][-2:]
    start_h=int(s1[0])
    start_m=int(s1[1][0:len(s1[1])-2])
    
    
    s1=s[1].split(":")
    finish_24=s[1][-2:]
    finish_h=int(s1[0])
    finish_m=int(s1[1][0:len(s1[1])-2])
    
    if start_24==finish_24: #same time zone
        if start_h<finish_h or (start_h==finish_h and finish_m>=start_m) :  # Simple
            return 60*(finish_h-start_h)+finish_m-start_m
        else:        
            return 12*60+60*(12-start_h)-start_m+60*finish_h+finish_m
            
    return 12*60-start_h*60-start_m+60*finish_h+finish_m
    


# Import modules for CGI handling 
import cgi, cgitb 



# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
str= form.getvalue('str')
result=CountingMinutesI(str) #"3:00pm-2:00am")
print("")
print("<html>")
print("<head>")
print("</head>")
print("<body>")
print("<h1>",str,"</h1>")
print (result, "Minutes; ",int(result/60),":",result%60," in hours")     

#print("<h2>Hello: %s %s</h2>" % (first_name, last_name))
    
         
