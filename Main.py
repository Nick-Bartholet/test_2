class Temperature:
    def __init__(self, temperature):
        self._temperature = temperature

    def setTemperatur(self, temperature):
        self._temperature = temperature

    def getTemperatur(self, temperature):
        return self._temperature
    
    def __str__(self):
        return f"Celsius: {self._temperature}"
    
    def __int__(self):
        return 1
    
    def __float__(self):
        return float(self._temperature)
    
    def __add__(self, addValue):
        return Temperature(self._temperature + float(addValue))
    
    def __mul_(self, multiplicator):
        if type(multiplicator)
    
    def __gt__(self, compareValue):
        return float(self) > float(compareValue)

    def __add_(self, addVector):
        return Vector3(self.x + addVector.x, self.y + addVector.y, self.z + addVector.z)
    
    x = property(getX, setX)
    y = property(getY, setY)
    z = property(getZ, setZ)

#    temperature = property(getTemperatur, setTemperatur)  

# t0 = Temperature(50)
# t1 = Temperature(100)

v0 = Vector3(1,2,1)
v1 = Vector3(2,0,0)

v2 = v0.addition(v1)
v2 = v0 + v1

# print(str(t0 > t1))

value1 = 100
value1 += 50
print(value1)

