#Objective: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite. Start with your guestlist.py program. Add a print() call at the end of your program, stating the name of the guest who can't make it. Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting. Print a second set of invitation messages, one for each person who is still in your list.

guestlist = ['Rihanna', 'oklou', 'Kiki Rockwell']

print(f"I would like to formally invite you to my dinner party I am hosting, {guestlist[0]}?\n")

print(f"Would you like to come over for dinner, {guestlist[1]}?\n")

print(f"Would you be interested in eating dinner with me, {guestlist[2]}?\n")

#print call stating the name of the guest who can't make it
print(f"{guestlist[0]} cannot make it to my dinner party.\n")

#modify the list, replacing the name of the guest who can't make it with the name of the new person invited
guestlist[0] = 'Pomme'

#print a second set of invitation messages, one for each person who is still in your list

print(f"Would you like to come to my dinner party, {guestlist[0]}?\n")

print(f"I would like to invite you over for dinner, {guestlist[1]}.\n")

print(f"Would you be interested in eating dinner with me and a few other people, {guestlist[2]}?\n")