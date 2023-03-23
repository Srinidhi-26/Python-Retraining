class City:
    def __init__(self,city_name,area_name,pincode):
        self.city_name = city_name
        self.area_name = area_name
        self.pincode = pincode

    def __repr__(self):
        return f"{self.city_name},{self.area_name},{self.pincode}"
    
class city_Status():
    def __init__(self,status_code,message,city_obj):
        self.status_code = status_code
        self.message = message
        self.city_obj = city_obj

    def __repr__(self):
        return f"{self.status_code},{self.message},{self.city_obj}"