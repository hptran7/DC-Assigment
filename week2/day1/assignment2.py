list =[]

def display():
    print("Here is your shopping list:")
    for i in range(0,len(list)):
        print(f'{i+1} - {list[i].title} - {list[i].address}')

def display3():
    print("Here is your list of stores: ")
    for i in range(0,len(list)):
        print(f'{i+1} - {list[i].title}')

def display2():
    print("Here is your shopping List")
    for i in range(0,len(list)):
        print(f"{list[i].title}")
        for m in range(0,len(list[i].item_list)):
            print(f"{list[i].item_list[m]}")
class Shopping:
    def __init__(self,title,address):
        self.title = title
        self.address = address
        self.item_list = []

    def __str__(self):
        return f"{self.item_list}"
    
class Items:
    def __init__(self,item_title,item_price,item_quantity):
        self.item_title = item_title
        self.item_price = item_price
        self.item_quantity = item_quantity
    def __repr__(self):
        return f"{self.item_title} - Price: {self.item_price} - Quantity: {self.item_quantity}"



# while True:
    print("""
Press 1 to add store location:
Press 2 to add items to store:
Press 3 to view grocery list:
Press q to stop:
    """)
while True:
    choice = input("Please make your selection: ")
    if choice == "1":
        while True:
            shopping_title = input("Enter your location name or press \"q\" to stop: ")
            if shopping_title != "q":
                shopping_address = input("Please enter your location address: ")
                address = Shopping(shopping_title,shopping_address)
                list.append(address)
                display3()
            else:
                break
    elif choice == "3":
        display2()
    elif choice == "2":
        display3()
        while True:
            location = int(input("Enter the shopping location you want to add of press \"0\" to stop: "))
            if location != 0:
                item_title = input("Please enter your item's name: ")
                item_price = input("Please enter your item's price: ")
                item_quantity = input("Please enter your item's quantity: ")
                item = Items(item_title,item_price,item_quantity)
                list[location-1].item_list.append(item)
            else:
                break
    elif choice == "q":
        break
