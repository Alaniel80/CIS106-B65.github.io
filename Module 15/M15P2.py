#Iana Vasileva  CIS160 B65   M15P2 11/25/26
#Create a Car class. This must have methods for make, model, sticker price and discount price (90% of sticker price).
#Then create a derived class called Sportcar. Inherit the Car class and add option methods. Set the option value to Y to include the option in the updated price method.
#Define a method for each option.
#   SportWheels 1000.00
#   SportEngine 3000.00
#   SportInterior 2000.00
#For each method set to Y add the respective amounts to the updated price and display using the updated price method.
#Write program to instantiate two Car objects and two Sportcar objects. Show the program works for all combinations of options.

class Car:
    def __init__(self,make,model,sticker_price):
       self.make=make
       self.model=model
       self.sticker_price=sticker_price

    def discount_price(self):
        price=self.sticker_price*.9
        return price

class Sportcar(Car):
    def __init__(self,make,model,sticker_price,sport_wheels, sport_engines,sport_interior):
        super().__init__(make,model,sticker_price)
        self.sport_wheels=sport_wheels
        self.sport_engines=sport_engines
        self.sport_interior=sport_interior

    def Sportwheels(self):
        if self.sport_wheels=="Y":
            return 1000.00
        else:
            return 0

    def Sportengines(self):
        if self.sport_engines=="Y":
            return 3000.00
        else:
            return 0

    def Sportinterior(self):
        if self.sport_interior=="Y":
            return 2000
        else:
            return 0

    def new_price(self):
        price=self.discount_price()
        price=price+self.Sportwheels()+self.Sportengines()+self.Sportinterior()
        return price

# Instantiate the CAR object
car1=Car("Nissan", "Rogue", 20000)
car2=Car("Subaru", "Forester", 15000)

# Instantiate the SPORTCAR object
sport1=Sportcar("Lamborgini", "123",80000,"Y","N","Y")
sport2=Sportcar("Ford", "Mustang",70000, "N", "Y","Y")

#Use the object
print(f"{'Make':<12}{'Model':<12}{'Sticker Price':<18}"
      f"{'Discount Price':<18}{'Updated Price':<18}")

print("-" * 78)

print(f"{car1.make:<12}{car1.model:<12}"
      f"${car1.sticker_price:<17,.2f}"
      f"${car1.discount_price():<17,.2f}"
      f"{'N/A':<18}")

print(f"{car2.make:<12}{car2.model:<12}"
      f"${car2.sticker_price:<17,.2f}"
      f"${car2.discount_price():<17,.2f}"
      f"{'N/A':<18}")

print(f"{sport1.make:<12}{sport1.model:<12}"
      f"${sport1.sticker_price:<17,.2f}"
      f"${sport1.discount_price():<17,.2f}"
      f"${sport1.new_price():<17,.2f}")

print(f"{sport2.make:<12}{sport2.model:<12}"
      f"${sport2.sticker_price:<17,.2f}"
      f"${sport2.discount_price():<17,.2f}"
      f"${sport2.new_price():<17,.2f}")






