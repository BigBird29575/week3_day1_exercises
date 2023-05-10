
#Exercise 1 - Turn the shopping cart program into an object-oriented program

############################
##      NOT FINISHED     ##
############################

item_prices={
    "beef": 14.99,
    "turkey": 12.99,
    "tomato": 2.99,
    "brussel sprouts": 6.99,
    "mini potatoes": 3.99,
    "brown eggs": 18.99,
    "milk": 6.99,
    "red onions": 8.99,
    "halibut": 129.99
}


shopping_cart = {}


class cart:

    def __init__(self):


        def add(self, item, quantity): 
            if item in self.item_prices:
                if item in shopping_cart:
                    shopping_cart[item] += quantity
                else:
                    shopping_cart[item] = quantity
                print(f"{quantity} {item} added to cart.")

        def delete(self, item, quantity):
            if item in shopping_cart:
                del shopping_cart[item]
                print(f"{item} removed.")
            else:
                shopping_cart[item] -= quantity
                print(f"Removed {quantity} {item} from the shopping cart.")
                    
        def view(self):
            print("Items currently in the shopping cart:")
            for item, quantity in shopping_cart.items():
                price = item_prices[item]
                total_price = price * quantity
                print(f"{item} (Quantity: {quantity}, Price: ${price}, Total: ${total_price})")

        def checkout(self):
            total_price = 0
            for item, quantity in shopping_cart.items():
                price = item_prices[item] 
                total_price += price * quantity + (price*.07)
                print(f"{item} (Quantity: {quantity}, Price: ${price}, Total: ${price * quantity})")
            print("Thank you for choosing Spensive Mart. Your total w/ tax is")
            print(f"Total: ${total_price}")
            shopping_cart.clear()


        def main():
                        
            welcome = input('\nHello, welcome to Spensive Mart. What is your name?')
            print(f"\nThank you for choosing Spensive Mart {welcome}. Please make a selction.\n")

            while True:
                print("1 ----- Add ------")
                print("2 ---- Delete -----")
                print("3 --- Your Cart ---")
                print("4 --- Checkout ----")
                print("5 ----- Quit ------\n")
                
                selection = input("Select a number:")
                
                if selection == "1":
                    print(item_prices)
                    item = input("\nWhich item would you like to add?:")
                    quantity = int(input("\nHow many?:"))
                    add(item, quantity)
                elif selection == "2":
                    item = input("\nType the item to delete: ")
                    quantity = int(input("\nEnter the quantity: "))
                    delete(item, quantity)
                elif selection == "3":
                    view()
                elif selection == "4":
                    checkout()
                    break
                elif selection == "5":
                    print("\nThank you come again!")
                    break
                
main()     


##############################################################################

#Exercise 2 - Write a Python class for an Animal that has a name and 
#energy attributes. The animal class should also have methods for eat, 
#sleep, and play that will take in an integer and increase/decrease the 
#energy of the animal with a formatted print statement

class animal:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        
    def eat(self, eat_energy):
        self.energy += eat_energy
        return f"{self.name} is eating for 5 minutes. His energy is now {self.energy}."
        
    def sleep(self, sleep_energy):
        self.energy += sleep_energy
        return f"{self.name} is sleeping for 10 minutes. His energy is now {self.energy}."
        
    def play(self, play_energy):
        self.energy -= play_energy
        return f"{self.name} is playing for 5 minutes. His energy is now {self.energy}."