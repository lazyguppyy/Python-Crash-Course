#Objective: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner. Start with the guestlist.py program or changingguestlist.py program. Add a print() call to the end of the program, informing people that a bigger table was found. Use insert() to add one new guest to the beginning of the list, insert() to add one new guest to the middle of the list, and append() to add one new guest to the end of the list. Print a new set of invitation messages, one for each person in the list.


#creating a guest list--
guestlist = ['Charlie Brown', 'Snoopy', 'Linus']

print(f"{guestlist[0]}, would you like to come over for dinner?\n")

print(f"Would you like to eat dinner with me and a few guests tonight, {guestlist[1]}?\n")

print(f"{guestlist[2]}, does dinner this evening work for you?\n")



#changing guest list --
print(f"Awe, {guestlist[1]} cannot make it to the dinner party tonight.\n")

guestlist[1] = 'Sally'

print(f"The dinner party is still on tonight, {guestlist[0]}!\n")

print(f"Thank you for accepting my invitation, {guestlist[1]}!\n")

print(f"I cannot wait to see you tonight, {guestlist[2]}!\n")



#more guests --
print("Hey, everyone! I found a bigger table!\n")

guestlist.insert(0, 'Lucy')

guestlist.insert(2, 'Shroeder')

guestlist.append('Franklin')

print(f"You're invited, {guestlist[0]}!\n")

print(f"I hope to see you there, {guestlist[1]}!\n")

print(f"I hope you are ready for some yummy food, {guestlist[2]}!\n")

print(f"I would like to invite you to the dinner party I am hosting tonight, {guestlist[3]}.\n")

print(f"You are very much invited, {guestlist[4]}!\n")

print(f"Let me know if you can make it, {guestlist[5]}!\n")