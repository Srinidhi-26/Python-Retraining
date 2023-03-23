from model import City
from logic import add_City,change_City,change_Area, view_City,pincode,sort_City,sort_Area,sort_Pin


def pres():
    exit = False
    while exit == False:
        print("\n1.Add city info\n2.Change city info\n3.View city info"
              "\n4.Find By pincode\n5.Sort\n0.Exit\n")
        
        ch = int(input("Enter your choice:"))

        if ch == 1:
            a = input("Enter city name:")
            b = input("Enter area name:")
            c = int(input("Enter pincode:"))
            info = City(a,b,c)
            g = add_City(info)
            if g == 1:
                print("Added Successfully")
            else:
                print("bye bye not added")

        elif ch == 2:
            print("\n1.Change city name\n2.Change area name")
            ch = int(input("Enter your choice:"))
            if ch == 1:
                a = input("Enter old city name:")
                b = input("Enter new city name:")
                v = change_City(a,b)
                if v == 1:
                    print("City Name Updated")
                else:
                    print("No such city name")

            elif ch == 2:
                a = input("Enter old area name:")
                b = input("Enter new area name:")
                v = change_Area(a,b)
                if v == 1:
                    print("Area Name Updated")
                else:
                    print("No such area name")

        elif ch == 3:
            a = input("Enter city name:")
            v = view_City(a)
            if len(v) == 0:
                print("No such City")
            else:
                print(v)

        elif ch == 4:
            a = input("Enter pincode:")
            v = pincode(a)
            if v.statuscode == 0:
                print("No such Pincode")
            else:
                print("City Found",v.city_obj)

        elif ch == 5:
            print("\n1.Sort by city_name\n2.Sort by area_name\n3.Sort by pincode")
            ch = int(input("Enter your choice:"))

            if ch == 1:
                v = sort_City()
                if len(v) != 1:
                    print("city Sorted")
                    print(v)
                else:
                    print("city Not Sorted")
            elif ch == 2:
                v = sort_Area()
                if len(v) != 1:
                    print("area Sorted")
                    print(v)
                else:
                    print("Area Not Sorted")
            elif ch == 3:
                v = sort_Pin()
                if len(v) != 1:
                    print("Pin Sorted")
                    print(v)
                else:
                    print("Pin Not Sorted")



        elif ch == 0:
            exit = True