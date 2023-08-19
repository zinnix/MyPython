mainarray={}


def calculate(num):
    if num<15:
        return mainarray[num]    
    return mainarray[num%14+1]


def main():
    global mainarray
    mainarray={}
    for i in range(2,15):
        mainarray[i]=i-1
    # print(mainarray)
    n=22
    print(n,calculate(n))

    print ( n%14+1  )
main()
