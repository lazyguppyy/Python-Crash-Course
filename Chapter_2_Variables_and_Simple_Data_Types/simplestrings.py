#Changing case in a string with methods

##.title()
name = "captain america"
print(name.title())
print()

##.upper() & .lower()
name = "Steve Rogers"
###prints the string to all uppercase
print(name.upper())
###prints the string to all lowercase
print(name.lower())
print()



#Using variables in strings
first_name = "Steve"
last_name = "Rogers"
#f-strings: formats the string by replacing the name of any variable in braces with its value
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
print()



#Adding whitespace to strings with tabs or newlines
##adding a tab \t
print("\t", full_name)
print()

##adding a newline
print("\nSteve\nRogers")
print()


#Stripping whitespace
##.rstrip(), .lstrip(), .strip()
hero = ' Captain America '
print(hero)
print(hero.rstrip())
print(hero.lstrip())
print(hero.strip())
print()

#Removing prefixes
hero_url = "https://en.wikipedia.org/wiki/Captain_America"
hero_url = hero_url.removeprefix("https://")
print(hero_url)




