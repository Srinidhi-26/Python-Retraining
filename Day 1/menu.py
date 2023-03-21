def getCount(c):
    words = len(c.split())
    return words

def dummyString():
    c = input('enter the string')
   
    b = getCount(c)
    print('number of words',b)


def getCount1(c,d):
   if d in c:
       count = 0

       for i in range(0, len(c)):
           if c[i] == d:
               count = count + 1
       return count
     
   else:
       return -1
   
def sampleString():
    c = input('enter the string')
    d = input('enter the character to search')
   
    b = getCount1(c,d)
    print('list existing characters',b)


def callWhile():
    while True:
        print("1. View count of words \n2. check the repeated characters\n3. Exit")
        ch = int(input("Enter Your Choice: "))
        
        if ch == 1:
            dummyString()

        elif ch ==2:
            sampleString()

        elif ch == 3:
            break
        else:
            print("Invalid Choice")

callWhile();