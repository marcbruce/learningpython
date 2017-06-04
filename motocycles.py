motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
too_expensive = 'suzuki'
motocycles.remove(too_expensive)
print(motocycles)
print("\nA " + too_expensive.title() + " is too expensive for me")
del motocycles[-1]
del motocycles[-1]
print(motocycles)
# Removes the value name from the list
# motocycles.remove('yamaha')
# print(motocycles)


# Pops the last variable and makes it into a sentence using it
# last_owned = motocycles.pop()
# print("The last motocycle I owned was a " + last_owned.title() + ".")
# print(motocycles)


# Pops the last list item and moves it to its own variable
# popped_motocycle = motocycles.pop()


# Inserts Ducati at the beginning of the list
# motocycles.insert(0, 'ducati')


# Appends ducati to the list
#motocycles.append('ducati')
#print(motocycles)

# First value changed
# motocycles[0] = 'ducati'
# print(motocycles)