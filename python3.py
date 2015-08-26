import pymysql.cursors
"""
db = pymysql.connect(host='db4free.net',
                                 user='box01',
                                 password='K9-WF4af',
                                 db='glamordb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

"""

db = pymysql.connect(host='sql3.freemysqlhosting.net',
                                 user='sql385901',
                                 password='hY2*hJ6!',
                                 db='sql385901',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)



#Create DB
def create_db():
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # Create table as per requirement
    sql = "CREATE TABLE EMPLOYEE (FIRST_NAME  CHAR(20) NOT NULL, LAST_NAME  CHAR(20),         AGE INT,           SEX CHAR(1),         INCOME FLOAT )"
    cursor.execute(sql)

#Write into DB
def write_to_db():
    cursor = db.cursor()
    for i in range (1506,3426,186):
        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', '%d', '%c', '%d' )" % ('Ron', 'Ben Tzvi', 26, 'M', i)
        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()

#Read from DB
def read_from_db():   
    cursor = db.cursor()
    sql="SELECT  * FROM EMPLOYEE WHERE INCOME > '%d' and INCOME <'%d' and SEX='M'" % (1800,3700)
    i=1
    try:
       # Fetch all the rows in a list of lists.
     cursor.execute(sql)
     row=cursor.fetchone()
     while row:
         print (i,") ",row["FIRST_NAME"],"earns",(row["INCOME"]))
         row=cursor.fetchone()     
         i+=1
    except:
       print ("Error: unable to fecth data")

def update_db():
    cursor = db.cursor()
    # Prepare SQL query to UPDATE required records
    sql = "UPDATE EMPLOYEE SET INCOME = INCOME + 150  WHERE SEX = '%c'" % ('M')  # will increase INCOME by 150 for all males
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
    # disconnect from server
    
def del_data_from_db():
    # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to DELETE required records
        sql = "DELETE FROM EMPLOYEE WHERE INCOME > '%d'" % (3000)
        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()

           

def insert_data_to_db():
    cursor.execute("insert into products(id, name) values ('pyodbc', 'awesome library')")
    cnxn.commit()
    cursor.execute("insert into products(id, name) values (?, ?)", 'pyodbc', 'awesome library')
    cnxn.commit()


#create_db()
#write_to_db()
#update_db()
#del_data_from_db()

print ("------------------ before delete ------------------")
read_from_db()
#
print ("------------------after delete ------------------")
read_from_db()







# disconnect from server
db.close()

print ("00000000000  THE END 000000000000")












import calendar



Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

print (Money)
AddMoney()
print ( Money)

#specifing parameters in function in different order
def printinfo( name, age ):
   #"This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
# Now you can call printinfo function
printinfo( age=50, name="miki" );


def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   #mylist.append([1,2,3,4])
   print ("Values inside the function: ", mylist)
   return
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)






cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)




#Work with files
with open("text.txt", "w") as my_file:
	my_file.write("Success!")
print (my_file.closed)
if my_file.closed==False:
    my_file.close()
print ( my_file.closed)



#Classes
class Triangle(object):
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
    number_of_sides=3
    def check_angles(Triangle):
        return angle1+angle2+angle3==180
my_triangle=Triangle(90,30,60)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())





class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print (self.name)
        print (self.age)

hippo=Animal("Lion",11)
hippo.description()


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

#example of class 
class Greeting(object):
    def __init__(self, greeting='hello'):
        self.greeting = greeting
    def greet(self, name):
        return "%s! %s" % (self.greeting, name)
greeting = Greeting("hola")
print(greeting.greet("bob"))



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




# Add your for loop
for number in range(5):
    print(number,)

for letter in "Eric":
    print (letter,)


def median (nums):
    nums=sorted(nums)
    middle=len(nums)/2
    if middle==int(middle):
        middle=int(middle)
        return (nums[middle-1]+nums[middle])/2
    else:
        return (nums[int(middle)])

print (median([1,1,2]))








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



def purify(nums):
    newarr=[]
    i=0
    for i in nums:
        if not i%2:
            newarr.append(i)
    return newarr
print (purify([4,13,14,2,5,20,5]))




def count(sequence, item):
    total = 0
    for i in sequence:
        if i == item:
            total += 1
    return total

"""
    count=0
    i=0
    #item=str(item)
    #sequence=str(sequence)
    newstrsequence = ''.join(sequence)
    newitem = ''.join(item)
    while i<len(newstrsequence):
        if newitem==newstrsequence[i:i+len(newitem)]:
            count+=1
        i+=1
    return count
"""
print("----")
print (count(["1","2","1","1","4","SA","1.5","5.4","4","6","1","1.5","5.1","3","6","1.5","15.4","1","1","7"],["1","4"]))



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

#print(locations_of_substring(["1","2","1","1","4","1","1","5","4","6","1","1","1","3","6","5","1","1","1","2"],["1","1"]))







def censor (text,word):
    str=""
    i=0
    while i<len(word):
        str=str+"*"
        i+=1
    return (text.replace(word,str))
str="shalom"
print (censor ("this is a test iswow","is"))






#run through dictionary
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






def anti_vowel(text):
    str=""
    i=0
    while i<len(text):
        if not text[i]  in "aeiouAEIOU":
            str=str+text[i]
        i=i+1
    return str
print (anti_vowel ("Hey look Words!"))





def reverse (text):
    array=""
    i=len(text)-1
    while i>-1:
        array=array+text[i]
        i=i-1
    return array
print ("reserve of mesiba200boom:", reverse("mesiba200boom"))
print ("------------------------------------------------------------")



phrase = "A bird in the hand..."
print
for c in phrase:
    if c=="A" or c=="a":
        print ("X",)
    else:
        print (c,)






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

# Add your function below!
def get_average(input01):
    return average(input01)

def get_average(student):
    homework=average(student["homework"])
    quizzes=average(student["quizzes"])
    tests=average(student["tests"])
    return (0.1*homework+0.3*quizzes+0.6*tests)

def average(numbers):
    total=sum(numbers)
    total=float(total)
    return total/len(numbers)

#long if condition
def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    results=[]
    for ind in students:
        results.append(get_average(ind))
    return average(results)

def digit_sum(n):
    sum=0
    num=n
    while num>0:
        sum+=num-10*int(num/10)
        num=int(num/10)
    return sum
print ("The sum digits of: ", 282736, "is: ", digit_sum(282736))


def factorial (x):
    result=1
    i=x
    while i:
        result=result*i
        i=i-1
    return result
print ("The factorial of: ", 15, "is: ", factorial(15))

print ("************************")
def is_prime(x):
    if x<2:
        return False
    prime=True
    i=2
    while i<x-1 and prime==True:
        print (x,i)
        print (x%i)
        if not x%i:
            print ("not prime as it is divided by ", i)
            prime=False
        else:
            i=i+1
    return prime
print ("43 is prime:", is_prime(43))
print ("************************")



n=1
print ("n=",n)
print ("n=",n+1)
print ("n=",n+1)


param1=get_class_average( [lloyd, alice, tyler])
print ( param1)
print ( get_letter_grade(param1))
