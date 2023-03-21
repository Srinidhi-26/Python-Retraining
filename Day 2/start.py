from presen import(init)
init();



def remove_number():
    num_to_remove = int(input("Enter the number you want to remove: "))
    if num_to_remove in a:
        a.remove(num_to_remove)
        print("Number has been removed")
    else:
        print(" Number not found in the list")