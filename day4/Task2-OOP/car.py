
class Car:
    def __init__(self,name,fuelRate,velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity
    
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self, value):
        if value < 0:
            self._velocity = 0
        elif value > 200:
            self._velocity = 200
        else:
            self._velocity = value
    
    @property
    def fuelRate(self):
        return self._fuelRate
    
    @fuelRate.setter
    def fuelRate(self, value):
        if value < 0:
            self._fuelRate = 0
        elif value > 100:
            self._fuelRate = 100
        else:
            self._fuelRate = value
    
    def run(self, velocity, distance):
        self.velocity = velocity
        if self.fuelRate >= distance:
            self.fuelRate -= distance
            self.stop(0)
        else:
            remain_distance = distance - self.fuelRate
            self.fuelRate = 0
            self.stop(remain_distance)
    

    def stop(self, remain_distance=0):
        self.velocity = 0
        if remain_distance == 0:
            print("You have arrived to your point")
        else:
            print(f"Car stopped Remain distance: {remain_distance}")
        