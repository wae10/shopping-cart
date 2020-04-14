# shopping_cart.py
#from pprint import pprint
import datetime # for date and time 

def enlarge(i):
    return i * 100

#to US dollar currency formatting function
def to_usd(num):
    return "$" + str(format(num, '.2f'))

#date and time conversion function
def human_friendly_timestamp(date):
    output = ""
    for element in range(10):
        output += date[element]
    output += " "

    if int(date[11]) >= 1 and int(date[12]) >= 3:
        newDate = str(date[11]) + str(date[12])
        newDate = int(newDate) - 12
        output += str(newDate)
        for element in range(13, 16):
            output += date[element]
        output += " PM"

    else:
        output = ""
        for element in range(16):
            output += date[element]
        output += " AM"

    return output

# finding product function
def find_product(identifier, product_list_length, name_list, price_list):
    while str(identifier.upper()) != "DONE":

        if identifier.upper() != "DONE" and identifier.isnumeric():
            identifier = int(identifier)
            if identifier >= 1 and identifier <= product_list_length:
                name_list.append(products[identifier - 1]["name"])
                price_list.append(products[identifier -1]["price"])
                identifier = input("Please input a product identifier: ")

            else:
                identifier = input(("Invalid. Please input a product identifier: "))

        elif identifier.upper() != "DONE" and identifier.isalpha():
            identifier = input(("Invalid. Please input a product identifier: "))
    
    return name_list, price_list

# needed to remove from global scope
if __name__ == "__main__":

    # to be passed in human_friendly_timestamp() function
    date = str(datetime.datetime.now())

    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017



    # print(products)

    # TODO: write some Python code here to produce the desired output

    print("Welcome to the Everett Foods Palace Register System. Please input desired identifier from the products list. Enter 'done' when finished.")
    response = input("\nReady to proceed? [Y/N] ")

    if response.upper() == "Y":
        identifier = input("Please input a product identifier: ")

        product_list_length = len(products)

        # empty list for names of products to be added to
        name_list = []

        # empty list for corresponding prices to be added to
        price_list = []

        find_product(identifier, product_list_length, name_list, price_list)

        print("#> ---------------------------------")
        print("#> EVERETT FOODS PALACE")
        print("#> WWW.EVERETT-FOODS-PALACE.COM")
        print("#> ---------------------------------")
        print("CHECKOUT AT: " + human_friendly_timestamp(date))
        print("#> ---------------------------------")
        print("SELECTED PRODUCTS: ")
        subtotal = 0
        for product in range(0, len(name_list)):
            print("... " + name_list[product] + " (" + to_usd(price_list[product]) + ")") #to_usd()
            subtotal = subtotal + price_list[product]
        print("#> ---------------------------------")
        print("SUBTOTAL: " + to_usd(subtotal)) # to_usd()
        tax = .0875 * subtotal
        print("TAX: " + to_usd(tax)) # to_usd()
        total = subtotal + tax
        print("TOTAL: " + to_usd(total)) # to_usd()
        print("#> ---------------------------------")
        print("THANKS, SEE YOU AGAIN SOON!")
        print("#> ---------------------------------")

    else:
        print("Exiting program.....Restart when you are ready to proceed.")
