from llogic import  rand1, display_list, change_number, remove_number, ascend, descend, occur1
def pres():
    exit = False
    while not exit:
        print("MENU")
        print("0. Exit")
        print("1. Fill up list with 10 random numbers")
        print("2. View all the list")
        print("3. Change a number in the list")
        print("4. Remove a number from the list")
        print("5. Ascending order")
        print("6. decending order")
        print("7. count of a number occuring")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            rand1()
            print('values added')
        elif choice == 2:
            a = display_list()
            print(a)

        elif choice == 3:
            c= int(input('enter number which to replace'))
            b= int(input('enter number which should replace'))
            v= change_number(c,b)
            print(v)
            
        elif choice == 4:
            c= int(input('enter the number want to remove'))
            while c not in a:
                print(c,'number is not in list enter another number')
                c= int(input('enter the number want to remove'))
            v = remove_number(c)
            print(v)

        elif choice == 5:
                v = ascend()
                print(v)
            
        
        elif choice == 6:
                v = descend()
                print(v)

        elif choice == 7:
             v = occur1(a)
             print(v)
             

        elif choice == 0:
            exit = True

        
