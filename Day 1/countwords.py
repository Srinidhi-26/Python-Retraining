def getCount(c):
    words = len(c.split())
    return words


def dummyString():
    c = input('enter the string')
   
    b = getCount(c)
    print('number of words',b)

dummyString();