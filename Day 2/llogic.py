import random
occurrences ={}
a = []

def rand1():
    for x in range(0,10):
        a.append(random.randint(0,100))
    return a
                    
def display_list():
    print("List of Numbers:")
    return a

def change_number(c,b):
    if c not in a:
        return "number not in list"
    elif b in a:
        return 'number already exist'
    else:
        i = a.index(c)
        a[i]=b
    return a

def remove_number(c):
    if c in a:
        a.remove(c)
    return a

def ascend():
    ascend = a.copy()
    ascend.sort()
    return ascend

def descend():
    descend = a.copy()
    descend.sort(reverse=True)
    return descend

def occur1(a):
    occurrences = {}

    for number in a:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1

    result = []
    for number, count in occurrences.items():
        result.append((number, count))

    return result


def exit():
    return
