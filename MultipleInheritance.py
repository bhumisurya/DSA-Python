class Camera:
    def take_photo(self):
        print("Taking Photo")

class GPS:
    def location(self):
        print("Location")

class Smartphone(Camera, GPS):
    pass

phone = Smartphone()
phone.take_photo()
phone.location()