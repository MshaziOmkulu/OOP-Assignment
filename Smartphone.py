# Base class: ElectronicDevice
class ElectronicDevice:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
    
    def power_on(self):
        print(f"{self.brand} {self.model} is now ON.")
    
    def power_off(self):
        print(f"{self.brand} {self.model} is now OFF.")
    
    def device_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Battery life: {self.battery_life} hours")

# Derived class: Smartphone inherits ElectronicDevice
class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, battery_life, camera_megapixels, os):
        super().__init__(brand, model, battery_life)
        self.camera_megapixels = camera_megapixels
        self.os = os  # Operating system
    
    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels} MP camera on {self.brand} {self.model}.")
    
    def device_info(self):
        # Overriding method with more details
        super().device_info()
        print(f"Camera: {self.camera_megapixels} MP, OS: {self.os}")

# Example usage
phone1 = Smartphone("Apple", "iPhone 13", 20, 12, "iOS")
phone1.power_on()
phone1.take_photo()
phone1.device_info()
phone1.power_off()
