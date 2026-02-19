import task6

#Test for correct word count
def testWordCount():
    count = task6.countWords("task6_read_me.txt")
    assert count == 104