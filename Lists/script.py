
favorite_films = ['The Graduate', 'Reservoir Dogs', 'Fear and Loathing in Las Vegas', "Up", "I Am Legend"]
# indexing our list
print(favorite_films[2])
# slicing our list which returns a new list
print(favorite_films[0:2])
# Short hand notation if the first or last items in the list are being sliced
print(favorite_films[:2])

# We can also insert items to a list using insert() or append()

favorite_films.append("Dog Watch")
print(favorite_films)

favorite_films.insert(2, "Shrek")
print(favorite_films)

# We can then remove items by using pop()

favorite_films.pop()
print(favorite_films)

# OR

favorite_films.pop(3)
print(favorite_films)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997] 
years_sorted = sorted(years)
years_sorted_reversed = sorted(years, reverse=True)
print(years_sorted)
print(years_sorted_reversed)

words = ['Max\'s', 'favorite', 'film', 'is', 'The', 'Graduate.'] 
phrase = " space ".join(words)
print(phrase)


