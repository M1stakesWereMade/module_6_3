import random

class Animal:
    def __init__(self, speed):
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        """Изменяет координаты с учётом скорости"""
        if self._cords[2] + dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        """Выводит координаты"""
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        """Выводит сообщение в зависимости от степени опасности"""
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        """Выводит звук животного"""
        print(self.sound if self.sound else "No sound")


class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True
        self._DEGREE_OF_DANGER = 1

    def lay_eggs(self):
        """Выводит количество яиц"""
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        """Метод для ныряния, уменьшает координату Z"""
        dz = abs(dz)
        self._cords[2] -= dz
        self.speed /= 2


class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)
        self.sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)
print(db.get_cords())

db.dive_in(6)
print(db.get_cords())

db.lay_eggs()
