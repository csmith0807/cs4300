#create list of books
books = [("One fish, two fish, red fish, blue fish","Dr. Seuss"),
 ("The Very Hungry Caterpillar", "Eric Carle"),
 ("The Cask of Amontillado", "Edgar Allan Poe"),
 ("Rooster can't cock-a-doodle-doo","Karen Rostoker-Gruber")]

#return first 3 books
def getFirstBooks():
    return books[:3]

#create dictionary of students
studentDB = {
    "Kerblop": "1234",
    "Jorge": "1111",
    "Dongus": "0101",
    "Fleep": "2222",
    "Larry": "1342"
}

#return student ID associated with student name
def getStudentID(name):
    return studentDB.get(name)