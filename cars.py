
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

# Ordered list (temporary)
print("\nHere is the sorted list:")
print(sorted(cars))

print("Here is the original list again:")
print(cars)

# Reverse order list (permanent)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


