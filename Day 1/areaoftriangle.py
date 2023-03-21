def getArea(a,b,c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area
    

def areaOfTriangle():
    a = float(input('Enter first side: '))
    b = float(input('Enter second side: '))
    c = float(input('Enter third side: '))

    v = getArea(a,b,c)
    print('area of a triangle is ',v)

areaOfTriangle();
