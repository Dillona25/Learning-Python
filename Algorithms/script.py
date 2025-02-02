film_genres = ['SCIFI', 'drama', 'Thriller', 'comedy', 'Action']

# use .lower() to lower case the letters
for genre in film_genres:
    print(genre.lower())

for i in range(len(film_genres)):
    film_genres[i] = film_genres[i].lower()

print(f"Processed data: {film_genres}")

#Initialization

sales = [10, 20, 50, 10, 100]
total_sales = 0

for sale in sales:
    total_sales = total_sales + sale
    
print(f"Total sales were equal to: {total_sales}")

# Building a new list 
numbers = [2, 10, 100, 1000]
squared_numbers = []

for num in numbers:
    # Use append since we are appending to a list
    squared_numbers.append(num ** 2)

print(squared_numbers)

# Task
# In the code below, the string wrong_message is backward! Initialize an empty string variable called message, 
# then write a loop that iterates over the characters in wrong_message and concatenates them with message such that the characters are in the correct 
# order after the loop is finished. Print message after the loop to make sure you got it right.

wrong_message = "!emocleW"
message = ""

for char in wrong_message:
    # The code is reading from left to right in the varible and preprending the character
    # !
    # e!
    # me!
    # ect..
    message = char + message


print(message)

scores = [61, 99, 72, 87]

# Initialize the sum and counter
total = 0
counter = 0

for score in scores:
    counter = counter + 1
    total = total + score

print(f"The loop ran {counter} times")
print(f"The total is {total}")

name = "Steven"
age = 40

if (name == "Steven" or name == "Carol") and age <= 30:
    print("Getting customer data...")
else:
    print("Cannot find customer")

# ! Conditional Statements

# name = 'Steven'

# if name == 'Carol':
#     print("Hello again, Carol!")

# if name == 'Steven':
#     print("Welcome, Steven!")

#     name = 'Steven'

# if name == 'Carol':
#     print("Hello again, Carol!")
# elif name == 'Steven':
#     print("Top of the morning to you, Steven!")
# else:
#     print(f"Welcome, {name}!")

age = 10
is_member = True

if age < 12 or age >= 65:
    print("You get a free entry!")
elif age >= 12 and age <= 18 and is_member:
    print("You get a discounted entry!")
else:
    print("You pay the regular entry fee.")

# Task
# Below is a variable called sept_sales that contains the September sales from a business. Write a set of conditional statements that print:

# 'low sales' if the sales were below $30,000
# 'okay sales' if the sales were at $30,000 or above, and below $100,000
# 'good sales' if the sales were $100,000 or above

# sept_sales = 55000

# if sept_sales < 30000:
#     print('low sales')
# elif sept_sales >= 30000 and sept_sales < 100000:
#     print('okay sales')
# else:
#     print("good sales")

# numbers = [5, 20, 15, 3, 10]

# for num in numbers:
#     if num < 10:
#         print(f"{num} is small!")
#     elif num < 20:
#         print(f"{num} is medium!")
#     else:
#         print(f"{num} is large!")

# words = ['cat', 'elephant', 'dog', 'hippo', 'bee', 'antelope']

# # Initialize a counter variable to track how many words were changed
# k = 0

# # Loop through each index in the words list
# for i in range(len(words)):
#     # Check if the word's length is less than 5 characters
#     if len(words[i]) < 5:
#         # If it is, convert the word to uppercase and assign it back to its index in the list
#         words[i] = words[i].upper()
#         # Increment the counter since we made a change
#         k = k + 1

# # Print the number of words that were changed and the updated list of words
# print(f"There were {k} words with less than 5 characters")
# print(words)


animals = ['Koala', 'antelope', 'Gibbon', 'Alligator', 'manatee', 'Capybara']

k = 0

for i in range(len(animals)):
    if not animals[i].islower():
        animals[i] = animals[i].lower()
        k = k + 1

print (animals)

