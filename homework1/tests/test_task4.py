import task4

#Test if correct discounted values are returned
def testDuckTypeInt():
    assert task4.DuckType(100, 10) == 90

def testDuckTypeFloatFirst():
    assert task4.DuckType(50.5, 50) == 25.25

def testDuckTypeFloatSecond():
    assert task4.DuckType(100, 20.5) == 79.5

