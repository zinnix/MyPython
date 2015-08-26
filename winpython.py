#My whiteboard



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


