import random 
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start,end))
    return res 

def callRand():
    num = int(input('enter the num'))
    start = int(input('enter the start value'))
    end = int(input('enter the end value'))
    v = Rand(start, end, num)
    print('Random values are', v)

callRand();