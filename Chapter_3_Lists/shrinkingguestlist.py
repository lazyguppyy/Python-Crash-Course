#Objective: There is news that the new dinner table won't arrive in time for the dinner, and now you have space for only two guests. Start with the moreguests.py program. Add a new line that prints a message saying that only two people can be invided for dinner. Use pop() to remove guests from the list one at a time until only two names remain in the list. Each time a name is popped from the list, print a message to that person letting them know of condolences over the un-invite. Print a message to each of the two people still on the list, letting them know they're still invited. Use del to remove the last two names from the list, so an empty list can be had. Print the list to make sure that an empty list is actually at the end of the program.

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



#shrinking guest list --
print("Unfortunately, I can only invite two people for dinner because the new dinner table won't arrive in time for dinner. I only have space for two guests now.\n")

guestlist_0 = guestlist.pop(0)
print(f"I'm sorry I cannot invite you anymore, {guestlist_0}.\n")

guestlist_1 = guestlist.pop(1)
print(f"Let's hang out some other time, {guestlist_1}.\n")

guestlist_2 = guestlist.pop(0)
print(f"Can we reschedule, {guestlist_2}?\n")

guestlist_3 = guestlist.pop(0)
print(f"We should get together some other time, {guestlist_3}.\n")

print(f"I hope you are still able to attend, {guestlist[0]}.\n")

print(f"You are still invited, {guestlist[1]}.\n")

#checks who is remaining on the guest list
#print(guestlist)

del guestlist[0]
del guestlist[0]

print(guestlist)