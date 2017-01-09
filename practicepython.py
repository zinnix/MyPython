
#Exercise 20
#binary search of a number in a sorted list

import random
def findbinary(listnums,mynum):
    istart=0
    iend=len(listnums)-1
    while True:
        i=int(round((iend-istart)/2))+istart
        if listnums[i]==mynum:
            return(True)       
        if listnums[i]>mynum:
            iend=int(round((iend-istart)/2))+istart
        else:
            istart=int(round((iend-istart)/2))+istart
        if mynum>listnums[i] and mynum<listnums[i+1]:
            return(False)
while True:
    listnums=sorted((random.sample(range(250),35)))
    mynum=random.sample(range(listnums[0],listnums[len(listnums)-1]),1)[0]
    print(listnums,mynum,findbinary(listnums,mynum))
    x=input("any key")

quit()



import random
mynum=random.sample(range(200),1)[0]
listnums=sorted((random.sample(range(500),20)))
def findbinary(listnums,mynum):
    i=int(round(len(listnums)/2,0))
    while i in range (0,len(listnums)):
        if listnums[i]==mynum:
            return(True)
        if listnums[i]>mynum:
            if listnums[i-1]<mynum:
                return(False)
            else:
                i-=1
        else:
            if listnums[i-1]>mynum:
                return(False)
            else:
                i+=1
    return(False)
print ( listnums,mynum,findbinary(listnums,mynum))

quit()





#Exercise 19
import requests
from bs4 import BeautifulSoup


res = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
soup = BeautifulSoup(res.text, "html.parser")
data1=soup.find_all('div',{"class:","dek"})
for item in data1:
    pass #print (item.text.encode('utf-8'))
data2=soup.find_all('section',{"class:","content-section"})
for item in data2:
    print (item.text.encode('utf-8'))
    print()

#for lines in soup.find_all('p'):
#    print(str(lines.getText()).encode('utf-8'))










import requests
from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")

for elem in all_p_cn_text_body[7:]:
  print(elem.text)






r = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
soup = BeautifulSoup(r.text,"html.parser")
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip().encode('utf-8'))
    else: 
        print(story_heading.contents[0].strip().encode('utf-8'))

print ("==================Done==================")
quit()

quit ()



#Exercise 18
import random

def checkit(secret,userguess,cows,bulls):
    for i in range(0,len(secret)):
        for j in range(0,len(userguess)):
            if secret[i]==userguess[i]:
                cows+=1
                break
            else:
                if secret[i]==userguess[j]:
                    bulls+=1
                    break
    print("   ===>",cows," cows, ",bulls," bulls\n")

if __name__=="__main__":
    userguess="1"
    tries=cows=bulls=0
    print ("Welcome to the Cows and Bulls Game! ")
    secret=str(random.randint(1000,9999))
    print ("The secret number is",secret)
    while not userguess==secret and not userguess=="exit":
        tries+=1
        userguess=input("Guess #"+str(tries)+ ". Enter your guess number: ")
        if not userguess==secret and not userguess=="exit":
            checkit(secret,userguess,cows,bulls)
    

print ("\n=====================Awesome!  You guessed the right number in",tries,"tries.=====================")




#Exercise 17
import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.nytimes.com")
soup = BeautifulSoup(r.text,"html.parser")
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip().encode('utf-8'))
    else: 
        print(story_heading.contents[0].strip().encode('utf-8'))

print ("==================Done==================")
quit()

url = 'http://www.alltop.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,"html.parser")
for link in soup.find_all('a'):
    ppp=link.get('title')
    if ppp!=None:
        print(ppp)

#title = soup.find('span', 'title').string


#print(title)

#soup = BeautifulSoup(open("index.html"))

print ("==================Done==================")

quit()
 




#Exercise 16
#Generate strong password

import string
import random



s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
print ("".join(random.sample(s,passlen )))


def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))
print(pw_gen(int(input('How many characters in your password?'))))


#Exercise 15
# Print strings backwards 

Userstring=input("Enter string:")
print(" ".join(Userstring.split()[::-1]))



#Exercise 14
#Returns unique elements from a list
import random
thelist=[]
for i in range (0,20):
    thelist+=(random.sample(range(35),1))

def newelement(element,list2check):
    for i in list2check :
        if i==element:
            return False
    return True



newlist=[]
newlist2=[]
newlist3=[]
for element in thelist:
    if element not in newlist:
            newlist.append(element)
    if newelement(element,newlist3)==True:
        newlist3.append(element)


[newlist2.append(x) for x in thelist if x not in newlist2]

print("Original:",sorted(thelist))
print(sorted(newlist))
print (sorted(newlist2))
print (sorted(newlist3))
print(sorted(set(thelist)))



#Exercise 13
#Fibonnaci
#1, 1, 2, 3, 5, 8, 13,

nums=int(input ("Enter how many numbers you want in fibonacci series:"))
a=b=c=1
print (1)
print(1)
for i in range (nums-2):
    c=a+b
    a=b
    b=c
    print(c)

fibo=[1,1]
while len(fibo) < nums:
    fibo += [fibo[-1] + fibo[-2]]
print(fibo)

fin=[1,1]
for i in range (1,nums-1):
    fin.append( fin[i]+fin[i-1])
print(fin)



#Exercise 12
#Print first and last elements of a list
import random
a = [5, 10, 15, 20, 25]
print(a,a[0],"-",a[len(a)-1])
x = []
first, *mid, last = a
x.append(first)
x.append(last)
print("-",x,"-")



#Exercise 11
#Is a numer a prime
from math import sqrt
def isprime(num):
    for i in range (2,round(sqrt(num))):
        if num%i==0:
            return(False)
    return(True)

num=input("give me a number to check if it is a prime number:")
print (num, "is prime:",isprime(int(num)))


#Exercise 10
#unique numbers from two lists
import random
a = random.sample(range(25), 10)
b = random.sample(range(25), 15)
a=sorted(a)
b=sorted(b)
print (a)
print(b)
print("common:",[x for x in set(a) if (x in b)])




#Exercise 9

import random
a = random.randint(1,9)
tries=0
guess=4
while guess!="exit":
    guess=input ("Enter your guess. Type exit to quit the game:")
    if guess=="exit":
        break
    guess=int(guess) 
    tries+=1
    if guess>a:
        print ("Too big")
    elif guess<a:
        print ("Too small")
    else:
        print ("Well done! You guessed within",tries,"tries.")
        break

       
#Exercise 8
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

print ("Options: Rock, scissors, Paper")
quit1=""
quit2=""
def iswinner(p1,p2):
    if p1=="rock" and p2=="scissors" or p1=="scissors" and p2=="paper"or p1=="paper" and p2=="rock":
        return(True)
    return(False)

while quit1!="quit" and quit2!="quit":
    quit1=input("Player1: Enter your guess; Type quit to quit:")
    quit2=input("Player2: Enter your guess; Type quit to quit:")
    if quit1=="quit" or quit2=="quit":
        break
    if iswinner(quit1,quit2):
        print("Player1 won")
    elif iswinner(quit2,quit1):
        print("Player2 won")
    

#Exercise 7
#return only even elements of a list
a = [1, 4, 9, 161, 25, 361, 49, 64, 81, 100]
print("Original:",a)
print("Seconds",a[1::2])
print("Even", list(filter(lambda x: x%2==0, a)))
print("Even",[x for x in a if (x % 2 == 0)])

 






a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,103,100,145]
sum=75

for i in a:
    for j in a:
        if int(i)+int(j)==sum:
            print (i,j)
 


#Exercise 6
#String is a palindrome or not. 
userinput=input('Enter a string and I will tell you if it is a palindrome:') 
print(userinput[::-1]==userinput)
 

#Exercise 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,103,100,45]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,45,103,93,121,32]
print (list(filter(lambda x: x in b, a)))
d=[]
for i in a:
    if i in b:
        d.append(i)
print(d)


#Exercise 4
number=int(input('Enter a number and I will list all its divisors:'))
print (datetime.now())
print (list(filter(lambda x: number%x==0, range(2,number))))
print (datetime.now())
for i in range (2,number):
    if number%i==0:
        print (i)

print (datetime.now())


#Exercise 3
list1=[3,5,1,3,7,8,12,43,34,2,12,-9,70,100,45,73,45,23,17]
l=[]
block=int(input('Enter the number to show numbers smaller than it: '))

print ([x for x in list1 if x <block])
print (list(filter(lambda x: x <block, list1)))

for n in list1:
    if n<block:
        l.append(n)
print ('Original list: ',list1,'\nNew list with numbers smaller than ',block,': ',l)









#Exercise 2
num=int(input('Enter a number: '))
if (num%4==0):
    print('Divided by 4')
elif (num%2==0):
    print('Even')
else:
    print ('odd')



#Exercise 1
#Asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
Fullname=input('Enter your name:')
Age=input('Enter your Age:')
Repeating=input('How many times you want to repeat the answer:')
for x in range(0, int(Repeating)):
    print (x+1,') You will be 100 years old on',datetime.now().year+100-int(Age))
# I am now 45; I will 100 in (now year)+100-current age




#does sum can be made of list of numbers
import itertools 
def ArrayAdditionI1(arr): 
    maxn=max(arr)
    print (maxn)
    arr.remove(maxn)
    for n in range(2,len(arr)):
        for i in (itertools.combinations(arr,n)):
            if sum(i)==maxn:
                return i
    return -1
print (ArrayAdditionI1([1, 1, 2, 3, 5, 8, 13, 21, 34, 45,55, 89,103,100,145]))

quit()
