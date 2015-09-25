#work with command line argument
import sys
address = ' '.join(sys.argv[1:])



#how many numbers are missing to set the array continuous 
def Consecutive(arr): 
    
    #magic solution in one line
    print (max(arr)-min(arr)-len(arr)+1,"!!!!")
    arr.sort()
    compl=1
    i=0
    while i<len(arr)-1:
        n=arr[i]
        while i<len(arr) and n<arr[i+1]:
            compl+=1
            n+=1
        i+=1
    return(compl-len(arr))

print ("=========",Consecutive([6,20,10,18]),"=====")




#returns the mode popular item in a list (array)
def SimpleMode(arr): 
    return max(arr, key=arr.count)
print (SimpleMode([10, 4, 5, 2, 4,10,10,4,4,4,10,6]) )



#return the first word with the greatest number of repeated letters.
def LetterCount1(str): 
  maxC = 0
  maxWord = ""
  for word in str.split():
    count = 0
    for i in range(len(word)):
      if word[i] in word[i+1:]:        
        count += 1 
    if (count > maxC):
    	maxC = count
    	maxWord = word
  if maxC == 0:
  	return -1
  else:
  	return maxWord  
print (LetterCount1("reeepeatd is a nice coununttrryy with mannny reeppeatd lakes!"))



# returns the first word with the greatest number of repeated letters
def LetterCount(str): 
    def maxcharrepeats(word):        # Canada - 3
        newword=sorted(word)
        i=1
        maxlength=1
        while i<len(newword)-1 and newword[i].isalpha():
            currentlength=1
            while i<len(newword)-1 and newword[i].isalpha() and newword[i]==newword[i+1]:
                currentlength+=1
                i+=1
            if maxlength<currentlength:
                maxlength=currentlength
            i+=1
        if maxlength==1:
            return -1
        return maxlength
    maxlength=1
    maxword=""
    currentword=""
    newarry=str.split(" ")
    for word in newarry:
        wordlength=maxcharrepeats(word)
        if maxlength<wordlength:
            maxlength=wordlength
            maxword=word
    return (maxlength,maxword)
print (LetterCount("Canada is a nice country with many repeated lakes!"))




def BinaryConverter(str1): 
    return(int(str(str1),2))
print(BinaryConverter(100101))


import itertools 
def ArrayAdditionI1(arr): 
    maxn=max(arr)
    arr.remove(maxn)
    for n in range(2,len(arr)):
        for i in (itertools.combinations(arr,n)):
            if sum(i)==maxn:
                return i
    return -1
print (ArrayAdditionI1([7,3,5,10,2,-5]))



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


#checks if string is substring of bigger string
def StringScramble(str1,str2): 
     for c in str2:
         if not c in str1:
             return False
     return True

print (StringScramble("helpmaAto","hpAlmot"))



#returns greatest common factor
from fractions import gcd
def Division(num1,num2): 
    print (gcd(num1,num2)) 
    i=min(int(num1/2),int(num2/2))
    while i>1:
        if num1%i==0 and num2%i==0:
            return i
        i-=1
    return 1
print (Division(216,448))



#returns true if the string is a palindrome (skipping non-characters)
def PalindromeTwo(str):
    newstr=("".join(i.lower() if i.isalpha() else "" for i in str))
    return newstr[::-1]==newstr
    
print(PalindromeTwo("Q1Noel - sees Leon1!!!!Q1726381W"))



#prints how much each char is presented in string
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
print(RunLength("aabbcde"))


#checks if a number is prime
from math import sqrt; from itertools import count, islice
def PrimeTime(n):
    if n < 2: return False
    return all(n%i for i in islice(count(2), int(sqrt(n)-1)))



#How many times to cycle summarizing number's digits to get less then 10
def AdditivePersistence(num): 
    def sum_digits(n):
        t=n
        sum=0
        while t>0:
            sum+=t%10
            t=int(t/10)
        return sum
    if num<10:
        return(0)
    AdditiveCounter=1 # total count of cycles
    currentsum=sum_digits(num)
    while currentsum>9:
        currentsum=sum_digits(currentsum)
        AdditiveCounter+=1
    return(AdditiveCounter)
print(AdditivePersistence(99999999999999999999999999999999999999999999999999999999999999999))


# Have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string true if any combination of numbers in the array can be added up to equal the largest number in the array, otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain negative numbers. 
import itertools 
def ArrayAdditionI(arr): 
  maxN = max(arr)
  for i in range(2, len(arr)):
    for item in itertools.combinations(arr,i):
      if sum(item)==maxN:
        return "true"
  return "false"
print (ArrayAdditionI([32,10,40,5,10,1,3,5,73]))




#Check if number is power of 2
def PowersofTwo(num): 
    return math.log(num,2)==math.floor(round(math.log(num,2)))
print (PowersofTwo(8192))


#print 3rd longest string in array
def ThirdGreatest(strArr): 
    print (strArr)
    return sorted([(word, -len(word)) for word in strArr], key=lambda x: x[1])[2][0]
ss=[ "hello", "world", "after1", "all"]
print (ThirdGreatest(ss))



#Swap case of characters in string
def SwapCase(str): 
    #one line solution:
    #return "".join([i.lower() if i.isupper() else i.upper() for i in str])
    print (str)
    news=""
    for c in str:
        if c.lower()==c:
            news+=c.upper()
        elif c.upper()==c:
            news+=c.lower()
        else:
            news+=c
    return news
print (SwapCase("MarkISl93weR"))



#Sum numbers in string
def NumberAddition(str): 
    def isnumber(n):
        if n>='0' and n<='9':
            return True
        return False
    print (str)
    i=0
    totalsum=0
    while i<len(str):
        tnum=0
        needincreament=1
        while i<len(str) and isnumber(str[i]):
            if isnumber(str[i]):
                tnum=tnum*10+int(str[i])
            i+=1
            needincreament=0
        if needincreament==1:
            i+=1
        if tnum: print(tnum,"+")
        totalsum+=tnum
    return totalsum
print (NumberAddition("Ma45k0120er34tj200s991"))


#insert dashes ('-') between each two odd numbers in str
def DashInsert(str): 
    def odd(n):
        return (int(n)%2==1)
    print("checking ",str)
    newstr=""
    i=0
    while i<len(str):
        if odd(str[i]) and odd(str[i-1]) and i>0:
            newstr+="-"+str[i]
            i+=1
        if i<len(str):
            if odd(str[i]) and odd(str[i-1]) and i>0:
                newstr+="-"
            newstr+=str[i]
        i+=1
    return(newstr)
print (DashInsert("777773055544448899281274727777"))


#count number of instances of each character in a string
sentence="This is a nice long sentence with many words"
count={}
for char in sentence:
    count.setdefault(char,0)    # if we don't have char, it will be added and 0 instances
    count[char]+=1                      # the previous command set the instance to 0 if this is the first time. now, number of instances is raised by 1; 
                                                        # so either it will be 1, or increased by 1.
print (count)




#variables
x3=7
def fun01():
    print (x3)
    #global x3 # by default, Python will scope variable inside block. adding "global" tells to use the global variable x3
    #x3=8 # it will take the global x3 and assign to it 8
    #x3=x3+5 #now global x3 equels 13
    return x3 #returns 13

print ("before fun01",x3) # will be 7
print ("after fun01",fun01()) # will be 13
print ("x3=",x3) # will be 13

exit ()




import calendar

cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)
exit()


import math # generic import
# from math import * // univeral import, so you don't need to add .math prefix to functions
# from math import sqrt // Import *just* the sqrt function from math


from datetime import datetime

#range is exclusive and starts at 0 by default
for i in range(20):  # will print 0..19
    print (i,)

#creates list of even numbers
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print (evens_to_50)

#Multiple Assignment
a, b, c = 1, 2, "john"
a = b = c = 1

print ("This is my first " + "Pyton" + " program")
x=5
print (x)
# this is a comment

fifth_letter = "MONTY"[4]
print (fifth_letter)
mystring="hello world"
print (len(mystring))
print (mystring.lower())
print (mystring.upper())
print ("dsfasfas"[-1]) # prints last character in string

monty=True
python=1.234
monty_python=python**2
print (monty_python)
meal = 44.50
tax = 0.0675
tip = 0.15
total=(1+tip)*(meal*(1+tax))
print("%.2f" % total)

string_1 = "Camelot"
string_2 = "place"
print ("Let\'s not go to %s. \'Tis a silly %s." % (string_1, string_2))

now=datetime.now()
print ("The date is:" + str(now.day) + "/" +str(now.month) +"/"+ str(now.year))
print ('The date is: %s/%s/%s' % (now.day, now.month, now.year))
print ('The time is: %s:%s:%s' % (now.hour, now.minute, now.second))



def using_control_once():
    if 5==5:
        return "Success #1"
def using_control_again():
    if 5**2>4:
        return "Success #2"
print (using_control_once())
print (using_control_again())



answer = "This but a scratch!"
def black_knight():
    if answer == "This but a scratch!":
        return True
    else:
        return  False      # Make sure this returns False
def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return   False     # Make sure this returns False



def greater_less_equal_5(answer):
	"""
    This is a multi-line remark and it describes the function
    """
	if (answer>5):
		return 1
	elif (answer<5):
		return -1
	else:
		return 0
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))



pyg = 'ay'
original = input('Enter a word:')
if len(original) > 0 and original.isalpha():
    print (original)
    word=original.lower()
    first=word[0]
    new_word=word+first+pyg
    new_word=new_word[1:len(new_word)]
    print (new_word)
else:
    print ('empty')



allfunctionsfrommath = dir(math) # Sets everything to a list of things from math module
print (allfunctionsfrommath)      # Prints 'em all!

# def biggest_number(*args): // Function with unkown number of parameters
# biggest_number(-10, -5, 5, 10)




zoo_animals = ["pangolin", "cassowary", "sloth", "dog"];  #Arrays (they call it lists)

if len(zoo_animals) > 3:
	print ("The first animal at the zoo is the " + zoo_animals[0])
	print ("The second animal at the zoo is the " + zoo_animals[1])
	print ("The third animal at the zoo is the " + zoo_animals[2])
	print ("The fourth animal at the zoo is the " + zoo_animals[3])

zoo_animals.append("cat") # adding "cat" as the last field

print (zoo_animals[1:4])  # will print fields on index from 1 to 3
print (len(zoo_animals))



#run through list
my_list = [1,9,3,8,5,7]
for number in my_list:
    # Your code here
    print (number*2)


#list slicing
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:16]            # The last two items (index four and five)




# split list
ss="var01=mark;var01=moshe;var03=david;var04=arba;var05=five"
newss=ss.split(";")
for n in newss:
    (key, value ) = n.split('=')
    first=key
    second=value
    print( first, ";",second )



#search from string inside other string - recursively
def locations_of_substring(sequence,item):
    """Return a list of locations of a substring."""
    newstrsequence = ''.join(sequence)
    newitem = ''.join(item)
    substring_length = len(newitem)
    def recurse(locations_found, start):
        location = newstrsequence.find(newitem, start)
        if location != -1:
            return recurse(locations_found + [location], location+substring_length)
        else:
            return locations_found

    return recurse([], 0)
print(locations_of_substring(["1","2","1","1","4","1","1","5","4","6","1","1","1","3","6","5","1","1","1","2"],["1","1"]))


start_list = [5, 3, 1, 2, 4]
square_list = []
for index in start_list:
    square_list.append(index**2)
square_list.sort()
print (square_list)


#Merging two lists into dictionary
list01 = ["Chess","Football","Swimming","Running","Cycling"]
list02=["Dan","Yosi","Julia","Charles","Rafi"]
dict01={}
for i in range (len(list01)): 
    dict01[list01[i]]=list02[i]
print (dict01)



# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print (residents['Puffin']) # Prints Puffin's room number
print (residents['Sloth'])
print (residents['Burmese Python'])
print (residents.keys())  # prints all dictionary keys
print (residents.values()) # prints all dictionary values


menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print (menu['Chicken Alfredo'])
# Your code here: Add some dish-price pairs to menu!
menu['bobo']=5.5
menu['number']=12
menu['float']=5.2
print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)

#remove entry from list
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")


# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines
# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper Penguin"]="new value"
print (zoo_animals)


inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()
inventory["pocket"]=['seashell', 'strange berry', 'lint']
inventory["backpack"].sort()
inventory["backpack"].remove('dagger')
inventory["gold"]=inventory["gold"]+50


#run through dictionary
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}
for word01 in webster:
    print (webster[word01])


#built in functions to go through dictionary
my_dict ={
    "drink":"coffee",
    "color":"black",
    "size":"medium",
    "Weight":45
}
print (my_dict.items())
print (my_dict.keys())
print (my_dict.values())

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in a:
    if (i%2==0):
        print (i)

a.pop(4) # will remove and return the 5th item (4)
a.remove(5) # will remove any instances of 4
del(a[10]) # removes the item in field #11 (10) but doesn't return it

# Merge two lists into dictionary (manually)
var1 = [1,2,3,4]
var2 = [5,6,7]
d = {1:var1, 2:var2}


#manipulate list and convert it to string
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
print (garbled[::-2])  #will print every second character, backwards 
print (''.join(list(filter(lambda x:not x=="X",garbled[::-1]))))  # going backwards and filtering 'X'


#Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.
threes_and_fives=list(filter(lambda x: x % 3 == 0 or x%5==0, range(1,16)))

# create new list to include only unique entries from current list
def remove_duplicates(nums):
    newarry=[]
    for i in nums:
        exists=0
        n=0
        for n in range(len(newarry)):
            if (i==newarry[n]):
                exists=1
        if exists==0:
            newarry.append(i)
    return newarry
print (remove_duplicates([3,2,1,3,2,2,3,5,6,7,1,1,1,9]))


def fizz_count(x):
    count=0
    for ind in x:
        if (ind=="fizz"):
            count=count+1
    return count
print (fizz_count(["fizz","cat","fizz"]))

#String looping
for letter in "Codecademy":
    print (letter)


# Empty lines to make the output pretty
print
print
word = "Programming is fun!"
for letter in word:
    # Only print out the letter i
    if letter == "i":
        print (letter)


prices={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for ind in prices:
    print ("%s " % ind)
    print ("price: %s" % prices[ind])
    print ("stock: %s" % stock[ind])


animal_sounds = {
    "bear": "John",
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
    "quizzes": [88.0, 40.0, 94.0],
    "fox": [],
}
print (animal_sounds["cat"])


lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students=[lloyd, alice, tyler]
for ind in students:
    print (ind["name"])
    print (ind["homework"])
    print (ind["quizzes"])
    print (ind["tests"])




#Function to calculate average of array
def average(numbers):
    total=sum(numbers)
    total=float(total)
    return total/len(numbers)



#Manipulate list
def double_first(n):
    n[0] = n[0] * 2
numbers = [1, 2, 3, 4]
double_first(numbers)
print (numbers)


#Run through list items
n = [3, 5, 7]
for i in range(0, len(n)):
    n[i] = n[i] * 2


# Tuples are like lists, but read only; defined via ( but accessed as list, by [ 
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
print (tuple[1:3]) # Will print (786, 2.23)  ---> places #1,#2


"""
manipulating list
range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
range(0,3,1) ==> 0,1,2
n = len(L)
item = L[index]
seq = L[start:stop]
seq = L[start:stop:step]
seq = L[::2] # get every other item, starting with the first
seq = L[1::2] # get every other item, starting with the second
If you need both the index and the item, use the enumerate function:
  for index, item in enumerate(L):
    print index, item

str = 'Hello World!'
print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string


"""


"""
List excerise
-------------
Create a list, to_21, that's just the numbers from 1 to 21, inclusive.
Create a second list, odds, that contains only the odd numbers in the to_21 list (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.
Finally, create a third list, middle_third, that's equal to the middle third of to_21, from 8 to 14, inclusive.
"""
to_21=[i for i in range(1,22)]
odds=to_21[0::2]
middle_third=to_21[7:14]



#reverse list
my_list = range(1, 11)
backwards=my_list[::-1]


#loop through list within list
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten (lists):
    results=[]
    for numbers in lists:
        for num in numbers:
            results.append(num)
    return results
print (flatten(n))



#Sort string
def AlphabetSoup(value):
    list = [c for c in value]  #Convert string into list
    list.sort()                #Sort List
    return "".join(list)       #Convert List to String
print (AlphabetSoup("hElP"))


#Check if in a string there is 'a' and 'b' 4 chars later
def ABCheck(str): 
    i=0
    while i<len(str)-4:
        if str[i]=="a" and str[i+4]=="b":
            return True
        i+=1
    return False
print (ABCheck("Laura sobs"))





#return true if the parameter is a palindrome,
def Palindrome(str): 
    newstr=str.replace(" ","")
    palin=False
    i=0
    while i<len(newstr)/2:
        if not newstr[i]==newstr[len(newstr)-1-i]:
            return False
        i+=1
    return True

print (Palindrome("never odd or even"))



# Arithmetic - same difference between members
# Geometric - same product between members
def ArithGeo(arr): 
    i=1
    ari=True
    diff=arr[0]-arr[1]
    mult=arr[0]/arr[1]
    geo=True
    while i<len(arr)-2:
        if not diff==arr[i]-arr[i+1]:
            ari=False
        if not mult==arr[i]/arr[i+1]:
            geo=False
        i+=1
    if ari:
        return "Arithmetic"
    if geo:
        return "Geometric"
    return -1
print (ArithGeo([2,4,8,16,32]))

#****List Comprehensions****
#[ expression-involving-loop-variable for loop-variable in sequence ]

#Create a list, squares, that consists of the squares of the numbers 1 to 10.
squars=[x**2 for x in range(1, 11)] 

#Print the last letter of each name in the list of names:
#print ( [ name[-1] for name in names ])

#Print the reverse of each name in the list of names:
#print ([ name[::-1] for name in names ])



#Battleship game
from random import randint
# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
board = []
for x in range(5):
    board.append(["O"] * 5)
def print_board(board):
    for row in board:
        print (" ".join(row))
print ("Let's play Battleship!")
print_board(board)
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print ("Turn", turn + 1)
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break # continue statement is also available in Python
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            # Print (turn + 1) here!
    if turn==3:
        print ("Game Over")
print_board(board)


num = 1
while num<11:  # Fill in the condition
    # Print num squared
    # Increment num (make sure to do this!)
    print (num**2)
    num+=1
else:
    print ("I am out of this while loop")


list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    # Add your code here!
    if a>b:
        print (a)
    else:
        print (b)


fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
print ('You have...')
for f in fruits:
    if f == 'tomato':
        print ('A tomato is not a fruit!') # (It actually is.))
        break  # will exit the whole for structure, so it will also skip "else". It is 'pear' and 'grape' will not be printed
    print ('A', f)
else:
    print ('A fine selection of fruits!')



for i in range(5):
    if i==3:
        print ("you are hitting 3!!")
    else:
        print (i)
else:
    print ("Ended the for loop!")



#Run through dictionary
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
def scrabble_score (word):
    sum=0
    i=0
    word=word.lower()
    while i<len(word):
        sum+=int((score[word[i]]))
        i+=1
    return sum
print (scrabble_score ("Helix"))



#run through string and replace string by string
def anti_vowel(text):
    str=""
    i=0
    while i<len(text):
        if not text[i]  in "aeiouAEIOU":
            str=str+text[i]
        i=i+1
    return str
print (anti_vowel ("Hey look Words!"))


#find longest word in a string
def LongestWord(sen): 
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



#Replace every letter in the string with the letter following it in the alphabet. Then capitalize every vowel in this new string 
def LetterChanges(str): 
  newstr=""
  for i in str:
      s=i
      if i.upper()>="A" and i.upper()<"Z":            # letter
        s=chr(ord(i)+1)
      if i.upper=="Z":
        s="a"
      if s.upper() in ["A", "E", "I", "O","U"]:
        s=s.upper()
      newstr+=s
  return newstr 
print (LetterChanges("hello*3"))


#perform a Caesar Cipher shift using num is shifting number counter
def CaesarCipher(str,num):
    def Cipher(c,num):
        if c.islower() and ord(c)+num>ord("z"):
            c=chr  (                     ord('a')+num-(ord('z')-ord(c)+1    ))
        elif c.isupper() and ord(c)+num>ord("Z"):
            c=chr  (                     ord('A')+num-(ord('Z')-ord(c)+1    ))
        else:
            c=chr(ord(c)+num)
        return c

    print(str)
    print ("".join(chr((ord('a') if i.islower() else ord('A'))+(ord(i)-(ord('a') if i.islower() else ord('A'))+num)%26) if i.isalpha() else i for i in str))
    newstr=""
    for c in str:
        if c.isalpha():
            newstr+=Cipher(c,num)
        else:
            newstr+=c
    return (newstr)
print (CaesarCipher("Hello tx12121aZ!!!!aaZZxx yywsDSsadfadf2 Beay",4))


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

# returns the first word with the greatest number of repeated letters.
def LetterCountI(str): 
    def ischar(char):
        if char.upper()>="A" and char.upper()<="Z":
            return True
        else:
            return False
    maxrepeatedtimes=0 
    maxrepeatedword=""
    i=0
    while i<len(str):
        count={}
        currentword=""
        while i<len(str) and not(str[i]==" "):
            currentword+=str[i]
            count.setdefault(str[i],0)    # if we don't have char, it will be added and 0 instances
            count[str[i]]+=1  
            i+=1
        
        maxtmp=max(count, key=count.get)
        #print ("for the word /",currentword,"/ max repeated letter numer is: ", count[maxtmp])
        if count[maxtmp]>maxrepeatedtimes:
             maxrepeatedtimes=count[maxtmp]
             maxrepeatedword=currentword
        i+=1
    if maxrepeatedtimes==0:
        return -1
    else:
        return   maxrepeatedword
print (LetterCountI("This is parallel programming. there is a test one two three swimmmminwmm"))


#Returns the second lowest and second greatest numbers
from random import randint
to_21=[i*5-randint(1, 110) for i in (range(1,22))]
to_21.sort()
if len(to_21)<3:
    print (to_21)
else:
    print (to_21[1],to_21[len(to_21)-2])




#convert minutes to hours:minutes format
def TimeConvert(num):
    mod=num%60
    return (str(int((num-(num%60))/60))+":"+str(mod))
print (TimeConvert(126))


name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")
print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))






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
    
result=CountingMinutesI("4:10am-1:08pm")        
print (result, "Minutes; ",int(result/60),":",result%60," in hours")   



#binary
twelve =0b1100
"""
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT
"""


garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message=''.join(list(filter(lambda x:not x=="X",garbled[::-1])))
print (message)

#print numbers in binary, oct and hexadimel base
for i in range(2,6):
    print ((bin(i), oct(i),hex(i)))

print (bin(0b1110&0b101)) # AND
print (bin(0b1110 ^ 0b101)) # XOR




cubes = [x**3 for x in range(1, 11)]
print(list(filter(lambda x: x % 3 == 0, cubes)))



 
def hetzi(num,num2):
    return num/2+num2
print (list((map(hetzi,range(45),range(10,30,2)))))



squares = list(map(lambda x: x**2, range(10)))
special_squares = list(filter(lambda x: x > 5 and x < 50, squares))
print (special_squares)

exit()

onelinefunc=lambda c,s:(c+s)*2
print (onelinefunc(4,2))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
#print (filter(lambda, languages))





#usage of anonymous function (lambda)
onelinefunc=lambda c,s:(c+s)*2
print (onelinefunc(4,2))
my_list = range(16)
print (filter(lambda x: x % 3 == 0, my_list))




to_21=[i for i in range(1,22)]
odds=to_21[0::2]
middle_third=to_21[7:14]

print (odds)



# prints cube of numbers between 1..10 that when cubed are divided by 4
cubes_by_four=[x**3 for x in range(1,11) if (x**3)%4==0]
print (cubes_by_four)




# finds mode (most repeated item in an array
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


#Classes #1
class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print ("Yep! I'm edible.")
        else:
            print ("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

#Class Basic
class Animal(object):
    def __init__(self,name):
        self.name=name
zebra=Animal("Jeffrey")
print (zebra.name)

#class #2
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry=is_hungry
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.
zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)
print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)

#Class #3
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name
    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print (product + " added.")
        else:
            print (product + " is already in the cart.")
    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print (product + " removed.")
        else:
            print (product + " is not in the cart.")
my_cart=ShoppingCart ("Moshe")
my_cart.add_item("apple",34)


#Class - example class Employee:
#Common base class for all employees
empCount = 0
def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1
   
def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


#class - override and inherit
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
         self.hours = hours
         return hours *12.00
         

#Class example
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a "+self.color+" "+ self.model + " with " +str(self.mpg)+" MPG."
my_car = Car("DeLorean", "silver", 88)
print (my_car.condition)
print (my_car.model)
print (my_car.color)
print (my_car.mpg)
print (my_car.display_car())


#Class example with inherit
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a "+self.color+" "+ self.model + " with " +str(self.mpg)+" MPG."
    def drive_car(self):
        self.condition="used"
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type=battery_type
my_car=ElectricCar("Ford","blue",15,"molten salt")

#represt class __repr__
class Point3D(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
my_point=Point3D(1,2,3)
print (my_point)
    
    
#I/O with files
my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10
f = open("output.txt", "w")
for item in my_list:
    f.write(str(item) + "\n")
f.close()

#Read from files
my_file=open("output.txt","r")
print (my_file.read())
my_file.close()



#good file handeling (auto close)
with open("text.txt", "w") as textfile:
	textfile.write("Success!")


#Work with files
with open("text.txt", "w") as my_file:
	my_file.write("Success!")
print (my_file.closed)
if my_file.closed==False:
    my_file.close()
print ( my_file.closed)


#specifing parameters in function in different order and with default values
def printinfo( name, age = 35 ):
   #This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return
# Now you can call printinfo function
printinfo( age=50, name="miki" );
printinfo( name="miki" );


#not fixed number of parameters
def printinfo1( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ( "Output is: ")
   print (arg1)
   for var in vartuple:
      print ( var)
   return
# Now you can call printinfo function
printinfo1( 10 )
printinfo1( 70, 60, 50 )



#Recursive sum
def SimpleAdding(num): 
  sum=num
  if num>0:
      sum+=SimpleAdding(num-1)
  return sum
print (SimpleAdding(12))  


#Capitalize first letter of each word
a="David He'lil is my Name. this is aMazing!!"
print(a.title())
print(a.capitalize())
print(' '.join(list(map(lambda x: x.capitalize(),a.split()))))








from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('mark.hanji@gmail.com')
passwordElem = browser.find_element_by_id('Gmailpassword')
passwordElem.send_keys('12345')
passwordElem.submit()



# UI - Graphical user interface
import tkinter
from tkinter import messagebox
top = tkinter.Tk()
def helloCallBack():
   #messagebox.showinfo( "Hello Python", "Hello World")
   messagebox.showwarning("Title", "Message")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
