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