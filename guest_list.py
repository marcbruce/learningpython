dinner_guests = ['Victor Hugo', 'Warren Buffet', 'Charlie Munger']
print("Dear " + dinner_guests[0].title() + ", You are invited for dinner with me at 7pm.")
print("Dear " + dinner_guests[1].title() + ", You are invited for dinner with me at 7pm.")
print("Dear " + dinner_guests[2].title() + ", You are invited for dinner with me at 7pm.")
print("Drats! " + dinner_guests[1].title() + " cannot attend my dinner, l'll have to invite someone new!")
dinner_guests[1] = "Barack Obama"
print("Dear " + dinner_guests[0].title() + ", You are invited for dinner with me at 7pm.")
print("Dear " + dinner_guests[1].title() + ", You are invited for dinner with me at 7pm.")
print("Dear " + dinner_guests[2].title() + ", You are invited for dinner with me at 7pm.")
print("ALERT: New spots available for my dinner!")
dinner_guests.insert(0, 'Mandy Moore')
dinner_guests.insert(2, 'Justin Beiber')
dinner_guests.append('Oprah')
print("Dear " + dinner_guests[0].title() + ", You are invited for dinner with me at 7pm.")
print("Dear " + dinner_guests[1].title() + ", You are invited for dinner with me at 7pm.")
print("Dear " + dinner_guests[2].title() + ", You are invited for dinner with me at 7pm.")
print("Dear " + dinner_guests[3].title() + ", You are invited for dinner with me at 7pm.")
print("Dear " + dinner_guests[4].title() + ", You are invited for dinner with me at 7pm.")
print("Dear " + dinner_guests[5].title() + ", You are invited for dinner with me at 7pm.")
print("LOLZ, soooo the table size shrank to 2 instead of 6!")
pop_1 = dinner_guests.pop(5)
print("Sorry " + pop_1.title() + ", but I can't host you anymore!")
pop_2 = dinner_guests.pop(4)
print("Sorry " + pop_2.title() + ", but I can't host you anymore!")
pop_3 = dinner_guests.pop(3)
print("Sorry " + pop_3.title() + ", but I can't host you anymore!")
pop_4 = dinner_guests.pop(2)
print("Sorry " + pop_4.title() + ", but I can't host you anymore!")
print("Dear " + dinner_guests[0].title() + ", I can't wait to see you tonight!")
print("Dear " + dinner_guests[1].title() + ", I can't wait to see you tonight!")
del dinner_guests[-1]
del dinner_guests[-1]
print(dinner_guests)