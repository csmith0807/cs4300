import task3

#test if "ifCheck" returns appropriate catagories 
def testIfCheckPos():
    assert task3.ifCheck(1) == "positive"

def testIfCheckNeg():
    assert task3.ifCheck(-1) == "negative"

def testIfCheckZero():
    assert task3.ifCheck(0) == "zero"

#test if the correct values were returned for primes
def testPrimes():
    assert task3.primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#test for correct sum of 1-100
def testSumWhile():
    assert task3.sumWhile() == 5050