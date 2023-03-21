def most_occured(List):
    counter = 0
    num = List[0]

    for i in List:
        curr = List.count(i)
        if(curr>counter):
            counter = curr
            num = i

    return num

def callOccured():
    List = input('enter list')
    b= most_occured(List)
    print('most occured value is', b)

callOccured();