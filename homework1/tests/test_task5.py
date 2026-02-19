import task5

#Test if correct books are returned
def get3Test ():
    first3 = task5.getFirstBooks()
    assert len(first3) == 3
    assert first3[0] == ("One fish, two fish, red fish, blue fish","Dr. Seuss")
    assert first3[1] == ("The Very Hungry Caterpillar", "Eric Carle")
    assert first3[2] == ("The Cask of Amontillado", "Edgar Allan Poe")

#Test for correct student IDs
def studentDBTest ():
    assert task5.getStudentDB("Dongus") == "0101"
    assert task5.getStudentDB("Kerblop") == "1234"

#Test for student not in DB
def studentDBTestNA ():
    assert task5.getStudentDB("Not There Magoo") is None