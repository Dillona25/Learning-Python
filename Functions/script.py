# def square_and_halve(number):
#     result = (number ** 2) / 2
#     return result

# x = square_and_halve(20)

# print(int(x))

list = [2, 4, 6, 8, 10]

def square_and_halve_list(numbers):
    result_list = []
    for number in numbers:
        result = (number ** 2) / 2
        result_list.append(result)
    return result_list

x = square_and_halve_list(list)

print(x)

# Practice problem: sorting and lowercasing a list
# Now write your own function called sort_alph(), which takes a list of 
# strings as input and returns as output a list of strings in all lowercase that has
# been sorted alphabetically. 
# After creating the function, call it and pass the familiar animals list as input. Wrap the call in 
# a print() function to display the output from sort_alph().


# animals = ['Koala', 'antelope', 'Gibbon', 'Alligator', 'manatee', 'Capybara']

# def sort_alph(animals):
#     sorted_animals = []
#     for animal in animals:
#         animal_lower = animal.lower()
#         sorted_animals.append(animal_lower)
#         sorted_animals.sort()
#     return sorted_animals

# print(sort_alph(animals))

# # We can better this function

# def sort_alphabet(words):
#     sorted_words = []
#     for word in words:
#         sorted_words.append(word.lower())
#         sorted_words.sort()
#     return sorted_words

# print(sort_alphabet(animals))


# List of animals
animals = ['Koala', 'antelope', 'Gibbon', 'Alligator', 'manatee', 'Capybara']

# Function to sort animals and optionally change their case
def sort_animals(animals_list, lowercase=True):
    sorted_animals = []
    
    if lowercase:
        # Convert each animal name to lowercase before sorting
        for animal in animals_list:
            sorted_animals.append(animal.lower())
    else:
        # Keep the original case and add to the sorted list
        sorted_animals = animals_list[:]
    
    # Sort the list
    sorted_animals.sort()
    
    return sorted_animals

# Example calls to test the function
sorted_lowercase = sort_animals(animals)
sorted_original_case = sort_animals(animals, lowercase=False)

print(sorted_lowercase)
    
