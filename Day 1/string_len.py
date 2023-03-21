
def numbers(list1):
    count=[]
    for i in list1:
     count.append(len(i))
    return count
    
def counting():
        list1=["Hello","hi","hello siri"]
        calling=numbers(list1)
        print(calling) 
counting()