print("\033c")


class Vehicle:
    
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed =  max_speed
        self.mileage = mileage
        self.capacity = capacity
        
        
    def fare(self):
        return self.capacity * 100
    
    
class Bus(Vehicle):
    
    def fare(self):
        amount = super().fare()
        amount = amount + ((amount * 10) / 100)
        return amount
    
    
school_bus = Bus("School Volvo", 180 , 12, 50)

print(f"Vehicle Name: {school_bus.name}\nSpeed: {school_bus.max_speed}\n Mileage: {school_bus.mileage}")

print(f"For Capacity {school_bus.capacity} the fare is : {school_bus.fare()}")