class Romb:
    def __init__(self, side:int, angle_a:int):
        self.side = side
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side":
            if not isinstance(value, int):
                raise TypeError("Side should be just int.")
            if value<=0:
                raise TypeError("side should be positive and greater than 0")

        if key == "angle_a":
            if not isinstance(value, int):
                raise TypeError("Angle should be number (int)")
            if value<=0 or value>=180:
                raise TypeError("Angle should be between 0-180")
            self.__dict__["angle_b"] = 180 - value

        self.__dict__[key] = value

    def __str__(self):
        return f"Romb --->>> sides = {self.side}, Angle A = {self.angle_a}, Angle B = {self.angle_b}"

www = Romb(100, 80)
print(www)