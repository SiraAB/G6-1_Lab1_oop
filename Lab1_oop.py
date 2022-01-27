class Aircraft:
    def __init__(self, Engine, Name, Colour, Price):
        self.Engine = Engine
        self.Name = Name
        self.Colour = Colour
        self.Price = Price
    
    def Full(self):
        return "{} {} {} {}".format(self.Engine, self.Name, self.Colour, self.Price)

Aircraft_1 = Aircraft("Jet", "F-15", "Red", 200000000)
Aircraft_2 = Aircraft("Turbosharf", "AH-64", "Black", 70000000)
Aircraft_3 = Aircraft("Turbofan", "S-3", "Green", 120000000)

Aircraft_2.Price -= 1000000
Aircraft_3.Price -= 800000

print(Aircraft.Full(Aircraft_1))
print(Aircraft.Full(Aircraft_2))
print(Aircraft.Full(Aircraft_3))

class Tank:
    def __init__(self, Gun, Name, Colour, Price):
        self.Gun = Gun
        self.Name = Name
        self.Colour = Colour
        self.Price = Price
        
    def Full(self):
        return "{} {} {} {}".format(self.Gun, self.Name, self.Colour, self.Price)

Tank_1 = Tank("120mm. Gun", "M1", "Green", 30000000)
Tank_2 = Tank("155mm. Gun", "M109", "Dark_Green", 32000000)
Tank_3 = Tank("25mm. Gun", "M3", "Tan", 10000000)

Tank_3.Price -= 100000

print(Tank.Full(Tank_1))
print(Tank.Full(Tank_2))
print(Tank.Full(Tank_3))

class Customer:
    def __init__(self, Country, Delivery_Date, Demand_Order, Demand_Quantity):
        self.Country = Country
        self.Delivery_Date = Delivery_Date
        self.Demand_Order = Demand_Order
        self.Demand_Quantity = Demand_Quantity
    
    def Full(self):
        return "{} {} {} {}".format(self.Country, self.Delivery_Date, self.Demand_Order, self.Demand_Quantity)

Customer_1 = Customer("Thai", "15 December 2025", "Tank/M1", 2)
Customer_2 = Customer("USA", "10 January 2023", "Aircraft/F-15", 500)
Customer_3 = Customer("China", "30 June 2077", "Aircraft/S-3", 150)

Customer_2.Demand_Quantity -= 100
Customer_3.Demand_Quantity += 50

print(Customer.Full(Customer_1))
print(Customer.Full(Customer_2))
print(Customer.Full(Customer_3))
