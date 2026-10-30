#Objective: Think of at least five places in the world you'd like to visit. 
# Store the locations in a list. Make sure the list is not in alphabetical order. 
# Print your list in its original order. Don't worry about printing the list neatly; just print it as a raw Python list. 
# Use sorted() to print your list in alphabetical order without modifying the actual list. 
# Show that your list is still in its original order by printing it. 
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list. 
# Show that your list is still in its original order by printing it again. 
# Use reverse() to change the order of your list. Print the list to show that its order has changed. 
# Use reverse() to change the order of your list again. Print the list to show it's back to its original order. 
# Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed. 
# Use sort() to change your list so it's stored in reverse-alphabetical order. Print the list to show that its order has changed.

#Think of at least five places in the world you'd like to visit.
#Canada, Korea, France, New Zealand, London

#Store the locations in a list. Make sure the list is not in alphabetical order.
places = ["Canada", "Korea", "France", "New Zealand", "London"]

#Print your list in its original order.
print(places)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(places))

#Show that your list is still in its original order by printing it.
print(places)

#Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print(sorted(places, reverse=True))

#Show that your list is still in its original order by printing it again.
print(places)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print(places)

#Use reverse() to change the order of your list again. Print the list to show it's back to its original order.
places.reverse()
print(places)

#Use sort() to change your list so it's stored in alphabetical order. Print the list to show its order has been changed.
places.sort()
print(places)

#Use sort() to change your list so it's stored in reverse-chronological order. Print the list to show that its order has changed.
places.sort(reverse=True)
print(places)


