class CreditCard: # Creates a class called CreditCard to rep a credit card object
    def __init__(self, name, number, bank="ABC Bank"): # __init__ method(constructor) takes 3 parameters: name, number and bank
        self.name = name # stores the name, card number and bank as instance variables 
        self.number = number
        self.bank = bank
        self.balance = 0 # initializes the balance to 0 for every new card

    def change(self, amount): # method to add money to card
        if not(isinstance(amount, int)) or isinstance(amount, float) or (amount <=0): # checks if the amount is valid 
            print("Change denied") # this is a bug meaning if invalid, print denial message
        else:
            self.balance += amount # if valid, add the amount to the balance
        
    def pay(self, amount): # method to pay/deduct money from the card
        if not(isinstance(amount, int)) or isinstance(amount, float) or (amount <=0) or (amount > self.balance): # checks if amount is invalid OR exceeds the current balance
            print("Change denied") # denies the payment if conditions fail
        else:
            self.balance -= amount # deducts the amount from balance if valid
    
    def __str__(self):
        info = f"Name: {self.name} \n Number: {self.number} \n Bank: {self.bank} \n Balance: {self.balance}"
        return info # creates a formatted string with all card details, \n adds new lines for readability
    

u1 = CreditCard("Robert Welker", 123456789) # creates a card for Robert Welker with number 1234..., bank defaults to "ABC Bank", balance starts at 0
print(u1) # prints the card info (calls __str__ method)

u1.change(2000) # adds 2000 to the balance
print(u1) # prints updated card info (balance now 2k)

u1.pay(500) # deducts 500 from balance
print(u1) # prints final card info (balance now 1500)


