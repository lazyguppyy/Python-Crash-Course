#Objective: Python has a removessuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removessuffix() method to display the filename without the file extension, like some file browsers do.

filename = "python_notes.txt"
filename = filename.removesuffix(".txt")
print(filename)