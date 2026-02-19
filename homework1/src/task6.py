import string

#return word count of file
def countWords(file):
    #read in file
    with open(file, "r") as file:
        text = file.read()
    
    #remove punctuation
    for char in string.punctuation:
        text = text.replace(char, "")

    words = text.split()
    return len(words)


