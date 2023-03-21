def getCount(c,d):
   if d in c:
       count = 0

       for i in range(0, len(c)):
           if c[i] == d:
               count = count + 1
       return count
     
   else:
       return -1
   
def dummyString():
    c = input('enter the string')
    d = input('enter the character to search')
   
    b = getCount(c,d)
    print('list existing characters',b)

dummyString();