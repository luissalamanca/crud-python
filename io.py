# -- coding utf-8 --
import os.path
import fileinput

# Welcome message
print("Welcome to a note-taking program")

# Temporary line numbers
linesdict = {}

# Action options
actionOptions = {
    1: "Read", 
    2: "Delete", 
    3: "Append", 
    4: "Update"
}

# Read file function
def reading(fileName):
    readFile = open(fileName, "r")
    read = readFile.read()
    print("--- FILE CONTENT ---")
    print(read)
    #read.close()

# Delete file function
def deleting(fileName):
    print('Type "yes" for deleting or hit any key to quit.')
    # Protecting the file for being removed
    question = input("Are you sure to delete this file? ")
    # If you type yes the file is removed
    if question == "yes":
        # File is removed
        os.remove(fileName)
        print("The file has been removed!")
        # If file is remove the program ask for a new file name
        main()

# Append function
def appending(fileName):
    addText = input("Write a new line text to this file: \n")
    appendfile = open(fileName, "a+")
    # Adding a new line in file
    appendfile.write("\n" + addText)
    # Close file
    appendfile.close()
    print("A new line was added!")

# Update a single line in file
def udpdating(fileName):
    counter = 0
    upfile = open(fileName, "r")
    readfile = upfile.read()
    countlines = readfile.split("\n")
    # Display the content in file
    print("--- CONTENT FILE FOR UPDATING ---")
    for line in countlines:
        counter += 1
        # Counting lines and adding a temporary key number of a line
        print(f"{counter}. {line}")
        # We store the data in a dictionary temporarily
        linesdict.update({counter: line})
    # Ask the user what number line wants to update
    lineNumber = int(input("Select the number line for updating: "))
    # Checking if the key exists in the dictionary
    if lineNumber in linesdict:
        # Selecting the current text
        oldtext = linesdict[lineNumber]
        print(f"You have selected line {lineNumber}: {linesdict[lineNumber]}")
        # Asking the user the new text
        newText = input("Enter the new text: \n")
        # Replacing the old the text for the new one
        fileupdating = readfile.replace(oldtext, newText)
        save = open(fileName, "w")
        save.write(fileupdating)
        save.close()
        print("The file was updated!")
    else:
        # The key does not exist in the dictiorany
        print("The line number does not exist.")


# Program actions
def actions(fileName):
    # If the file exist in the folder
    print("The file is already exist.")
    print("What do you want to do with this file?")
    print(f"Option: Action")
    print(f"--------------")
    # Displays a file options
    for action in actionOptions:
        print(f'({action}) {actionOptions[action]}')
    options = input("Select a option number: ")

    if options.isdigit() == True:
        if int(options) == 1:
            # Reading file
            reading(fileName)
        elif int(options) == 2:
            # Deleting file
            deleting(fileName)
        elif int(options) == 3:
            # Adding new lines
            appending(fileName)
        elif int(options) == 4:
            # Updating file
            udpdating(fileName)
        else:
            print("This option does not exist.")
    else:
        print("You have to choose a option number.")


# Creates new file if the file does not exists in folder.
def insertText(inputText):
    text = input("Write your note: \n")
    # Adding text in file
    inputText.write(text)
    inputText.close()

# Condition if file exist or not
def files(fileName):
    # If file exists
    file = fileName + ".txt" 
    if os.path.exists(file):
        # Actions file
        actions(file)
    else:
        # File does not exist
        filen = open(file, "w")
        insertText(filen)

def main():
    # Asking for the File Name
    fileName = input("Please insert a file name: ")
    files(fileName)

if __name__ == "__main__":
    main()