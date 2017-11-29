from SpeedException import Overspeed

class Car:
    speed=0
    topSpeed=0
    registrationNumber=""

    def getSpeed(self):
        return self.speed

    def setSpeed(self,speed):
        self.speed=speed

    def getTopSpeed(self):
        return self.topSpeed

    def setTopSpeed(self, topSpeed):
        self.topSpeed = topSpeed

    def getRegistrationNumber(self):
        return self.registrationNumber

    def setRegistrationNumber(self, registrationNumber):
        self.registrationNumber = registrationNumber

    def accelerate(self,speed):
        self.speed+=speed
        if(self.speed>self.topSpeed):
            raise Overspeed()
