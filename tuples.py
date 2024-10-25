# 1. Formatting Flight Itineraries
def display_iteineraries(itin_list):
    index = 1
    for itin in itin_list:
        print(f"Itineary {index}: {itin[0]} - From {itin[1]} to {itin[2]}")
        index += 1

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
display_iteineraries(itineraries)

# 2. Python Data Structure challenges in Real-World Scenarios
def add_book(library, title, author):
    exists = False
    for book in library:
        if (title.lower() == book[0].lower()) and (author.lower() == book[1].lower()):
            print(f"{title} by {author} already exists in the library.")
            exists = True
            break
    if exists == False:
        library.append((title, author))
        print(f"{title} by {author} has been added to the library.")
    
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
add_book(library, "1984", "george Orwell")
add_book(library, "Of Mice and Men", "John Steinbeck")
print(library)

# 3. Mastering Tuple Packing and Unpacking in Python
def display_orders(orders):
    index = 1
    for order in orders:
        name, product, quantity = order
        if quantity > 1:
            product += 's'
        print(f"Order {index}: {name} ordered {quantity} {product}.")
        index += 1

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Matt", "Keyboard", 4)
]

display_orders(orders)