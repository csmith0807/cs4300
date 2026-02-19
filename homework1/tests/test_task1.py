import sys
import os

sys.path.append(os.path.abspath("src"))

def testOutput(capsys):
    import task1
    captured = capsys.readouterr()
    #compare string to console output
    assert captured.out == "Hello, World!\n"