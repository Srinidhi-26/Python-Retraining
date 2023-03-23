from db import add_City_Info,change_City_Info,change_Area_Info,view_City_Info,pincode_Info,sort_City_Info,sort_Area_Info,sort_Pin_Info

def add_City(info):
    v = add_City_Info(info)
    return v

def change_City(a,b):
    v = change_City_Info(a,b)
    return v

def change_Area(a,b):
    v = change_Area_Info(a,b)
    return v   

def view_City(info):
    v = view_City_Info(info)
    return v  

def pincode(info):
    v = pincode_Info(info)
    return v  

def sort_City():
    v = sort_City_Info()
    return v

def sort_Area():
    v = sort_Area_Info()
    return v

def sort_Pin():
    v = sort_Pin_Info()
    return v