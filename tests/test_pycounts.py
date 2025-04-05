from pycounts import pycounts
from pycounts.pycounts import count_words

def test_count_words():
    test_file = "test.txt"
    with open(test_file, "w") as f:
        f.write("hello hello world")
    expected = {"hello": 2, "world": 1}
    assert count_words(test_file) == expected
