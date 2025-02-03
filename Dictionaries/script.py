laptops = {'Macbook M1 pro': 999.00, 'Macbook M2 pro': 1100.00, "Macbook M3 pro": 1399.00, "Macbook M4 pro": 1500.00}

print(type(laptops))

print(laptops.items())

print(list(laptops.items()))

laptops["Macbook M5 pro"] = 2000.00
print(laptops)

del laptops["Macbook M1 pro"]
print(laptops)

# pop( ) stores the value not the key
deleted_laptop = laptops.pop('Macbook M2 pro')
message = f"We have discontinued the Macbook M2 Pro thats costs {deleted_laptop} as it is 4 years old."

print(message)

brands = ['lenovo', 'apple', 'hp', 'dell']
models = ['ideapad', 'macbook air', 'hd+', 'inspiron']
sizes = [15.6, 13.3, 17.3, 16.0]
prices = [399.99, 749.99, 349.99, 599.99]

laptop_data = {'brand': brands, 'model': models, 'size': sizes, 'price': prices }
print(laptop_data)
print("The size column:", laptop_data['size'])
print("HP size:", laptop_data['size'][2])
