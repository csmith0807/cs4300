import task2

#check test case for each given data type
def testInt():
    assert isinstance(task2.getInt(), int)
    assert task2.getInt() == 1

def testFloat():
    assert isinstance(task2.getFloat(), float)
    assert task2.getFloat() == 1.1

def testString():
    assert isinstance(task2.getString(), str)
    assert task2.getString() == "test"

def testBoolean():
    assert isinstance(task2.getBoolean(), bool)
    assert task2.getBoolean() == False
