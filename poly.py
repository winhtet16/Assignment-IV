class MenuItem:
    def prepare(self):
        print("Hope you enjoy")
        
class Noodle(MenuItem):
    def prepare(self):
        print("Boiling hot noodles. (Comes with extra soup and meat)")
        super().prepare()
        
class FriedRice(MenuItem):
    def prepare(self):
        print("Frying delicious fried rice. (Topped with a fried egg)")
        super().prepare()
        
class Coffee(MenuItem):
    def prepare(self):
        print("Brewing a hot cup of coffee.")
        super().prepare()
    
def main():
    print("Welcome from the restaurant")
    print("Menu: 1. Noodle, 2. Fried Rice, 3. Coffee")
    
    Cus = int(input("Choose the Menu Number: "))
    
    if Cus == 1:
        order = Noodle()
    elif Cus == 2:
        order = FriedRice()
    elif Cus == 3:
        order = Coffee()
    else:
        print("The menu item you selected is not available. Preparing a generic dish.")
        return
        
    
    print("Your Order is :")
    order.prepare()
    print("Please Wait a few minutes")
    
main()
