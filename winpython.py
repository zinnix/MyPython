#My whiteboard

import math
import statistics
from math import sqrt
from itertools import count, islice

#Continue
                                      
exit()


"""
import urllib.request
#with urllib.request.urlopen('http://www.cnn.com/') as response:
   #html = response.read()



#to find go to page's FB page, at the end of URL find username
#e.g. http://facebook.com/walmart, walmart is the username
list_companies = ["walmart", "cisco", "pepsi", "facebook"]
graph_url = "http://graph.facebook.com/"
 

    #create db connection
    connection = connect_db()
    cursor = connection.cursor()
    
    #SQL statement for adding info to database
    insert_info = ("INSERT INTO page_info "
                   "(fb_id, likes, talking_about, username)"
                   "VALUES (%s, %s, %s, %s)")
 
for company in list_companies:
    #make graph api url with company username
    current_page = graph_url + company
        
    #open public page in facebook graph api
    
    #wp = urllib.request.urlopen("http://google.com")
#pw = wp.read()

#with urllib.request.urlopen('http://www.cnn.com/') as response:
 #  html = response.read()

    with urllib.request.urlopen(current_page) as response:
        readable_page=response.read()    
    
  #  web_response = urllib2.request.urlopen(current_page)
   # readable_page = web_response.read()
    json_fbpage = json.loads(readable_page)
        
    #print page data to console
    print  (company + " page"  )
    print  (json_fbpage["id"])
    print  (json_fbpage["likes"])
    print  (json_fbpage["talking_about_count"])
    print  (json_fbpage["link"])
    print  (json_fbpage["username"])
    print  (json_fbpage["website"])
    print  ("            ")
        
 
    #gather our JSON Data
    page_data = (json_fbpage["id"], json_fbpage["likes"],
                    json_fbpage["talking_about_count"],
                    json_fbpage["username"])
                     
    #insert the data we pulled into db
    #cursor.execute(insert_info, page_data)
    print (page_data)

        #commit the data to the db
        connection.commit()
        
    connection.close()
 
if __name__ == "__main__":
    main()
"""





#Returns if array is   Arithmetic,     Geometric or none (-1)
def ArithGeoII(arr): 
    diffart=arr[0]-arr[1]
    diffmul=arr[0]/arr[1]
    i=0
    art=True
    mul=True
    for i in range(0,len(arr)-1):
        if diffart!=arr[i]-arr[i+1]:
            art=False
        if diffmul!=arr[i]/arr[i+1]:
            mul=False
    if art:
        return ("Arithmetic")
    if mul:
        return "Geometric"
    return -1
print(ArithGeoII([4,14,24,34,44]))
exit()

#returns true if the string is a palindrome (skippin non-characters
def PalindromeTwo(str):
    newstr=("".join(i.lower() if i.isalpha() else "" for i in str))
    return newstr[::-1]==newstr
    
print(PalindromeTwo("Q1Noel - sees Leon1!!!!Q1726381W"))




#checks if number is prime
def isprime(n):
        if n < 2: return False
        return all(n%w for w in islice(count(2), int(sqrt(n)-1)))
     

#Prints the #num's prime
def PrimeMover(num):     
    count=1
    i=3
    while count<num:
       if isprime(i):
           count+=1
       i+=2
    return(i-2) 

print (PrimeMover(100))
exit()



#prints how many times each char is presented in string
def RunLength(str1): 
    print(str1)
    i=0
    newstr=""
    while i<len(str1):
        counter=0
        n=i
        while i<len(str1) and str1[i]==str1[n]:
            i+=1
            counter+=1    
        newstr+=str(counter)+str1[n]
    return(newstr)
print(RunLength("aabbcdeeeee"))






"""
def PrimeTime(num):

    i=3
    while num%i!=int(math.sqrt(num)):
      i+=1
    if i==int(math.sqrt(num)):
        return True
    print (i)
    return False
"""
    
print (PrimeTime(1571))




#How many times to cycle multiplying number's digits to get less then 10
def MultiplicativePersistence(num): 
    def product_digits(n):
        t=n
        product=1
        while t>0:
            product*=t%10
            t=int(t/10)
        print ("product of ",num,"=",product)
        return product

    if num<10:
        return(0)
    AdditiveCounter=1 # total count of cycles
    currentproduct=product_digits(num)
    while currentproduct>9:
        currentproduct=product_digits(currentproduct)
        AdditiveCounter+=1
    return(AdditiveCounter)
print(MultiplicativePersistence(2235))

    

exit()


# return 1 if the mode equals the mean
def MeanMode(arr): 

  print (arr)
  print ("mean=",statistics.mean(arr))
  print ("mode=",statistics.mode(arr))
  print ("mode=",max(arr, key = arr.count))
    
  arr.sort()
  i=0
  totalmax=0
  while i<len(arr)-1:
      currentmax=0
      while arr[i]==arr[i+1]:
          currentmax+=1 # increase recurrence 
          i+=1      # goes to next items
      if totalmax<currentmax:
          maxitem=arr[i-1]
          totalmax=currentmax
      i+=1
  print ("my mode is",maxitem,"it is repeated %d times"%totalmax)


(MeanMode([12,3,2,3,5,10,3,8,10,-3,8,0,0,-3,8,10,5,-8,11,-8,-8,-8,20,3,-8]))









#calculate difference between two times; returns minutes
def CountingMinutesI(str):  #9:00am-10:00am 60; 1:00pm-11:00am 1320 
    """
    09:15
    9:15
    11:15
    00:15
    1:01 
    1:11 
    """
    
    print (str)
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
    
    
        
    
    
    print (start_h,":",start_m,start_24)
    print (finish_h,":",finish_m,finish_24)
    
    
    
result=CountingMinutesI("4:10am-1:08pm")        
print (result, "Minutes; ",int(result/60),":",result%60," in hours")        
exit ()




# for the string to be true each letter must be surrounded by a + symbol
def SimpleSymbols(str): 
    def ischar(char):
        if char.upper()>="A" and char.upper()<="Z":
            return True
        else:
            return False
    
    if ischar(str[0]) or len(str)<3 or ischar(str[len(str)-1]):
        return False
    i=1
    status=False
    while i<len(str):
        if ischar(str[i]) and not (str[i-1]=="+" and str[i+1]=="+"):
            return False
        i+=1
    return True
print ( SimpleSymbols(input()))

exit()








def LongestWord(sen): 

  # code goes here
  text = "Code must be properly"
  more = " indented in Python!"
  current=""
  longest=""  
  i=0
  sen=sen+" "
  for n in range(len(sen)):
    if sen[n].upper()>="A" and sen[n].upper()<="Z":
      current+=sen[n]
    elif len(current)>len(longest):
        longest=current
        current=""
    else:
        current=""
  return longest 
print (LongestWord("This longer than usual but nowIamvery longssssdddddddsss longssssdddddddXXiis longssssdddddddssQa"))











  




my_list = "Mark"
backwards=my_list[::-1]

print (backwards)

exit()


arry=[]
num=input("Enter number till space: s")

while num!=" ":
    arry.append(int(num))
    num=input("Enter number till space: ")

print ("biggest number is: ",max(arry),". Sum of all numbers is: ",sum(arry))

exit ()


def abcheck(str):    
    for i in range(len(str)):
        try:
          if str[i] == "a" and str[i + 4] == "b":
            return "true"
          elif str[i] == "b" and str[i + 4] == "a":
            return "true"
        except:
          return "false"
    return "false"

print (abcheck("Mark bbbbis me"))






exit ()

first=int(input("Enter start:"))
finish=int(input("Enter finish:"))
steps=int(input("Enter steps:"))

outcome=[]
for i in range (first,finish,steps):
    outcome.append(i)
print (outcome)




list01 = ["Chess","Football","Swimming","Running","Cycling"]
list02=["Dan","Yosi","Julia","Charles","Rafi"]
dict01={}
for i in range (len(list01)): 
    dict01[list01[i]]=list02[i]
print (dict01)


exit()










import webbrowser, sys, pyperclip


import requests, bs4


res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)




exit ()


res = requests.get('http://www.cnn.com/')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(1000):
    playFile.write(chunk)






import tkinter
from tkinter import messagebox
#import messagebox 


top = tkinter.Tk()

def helloCallBack():
   #messagebox.showinfo( "Hello Python", "Hello World")
   messagebox.showwarning("Title", "Message")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()




#Working with the Web   
import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


