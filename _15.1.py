class Transport():   

    def __init__(self, name, max_speed, mileage):
     self.name = name
     self.max_speed = max_speed
     self.mileage = mileage


Autobus  = Transport("Honda", 180, 5000)

print(f"Название автомобиля: {Autobus.name}, скорость - {Autobus.max_speed} Пробег - {Autobus.mileage}")