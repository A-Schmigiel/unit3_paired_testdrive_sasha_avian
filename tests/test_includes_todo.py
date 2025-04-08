from lib.includes_todo import *

# test for call
# testing what happens if it's an empty str
# test a normal one
# test for lower case
# test for if it doesnt have todo
# test todo without the hash
# test To.........Do

# def test_calling_todo():
#     assert includes_todo('str') == True

def test_empty_str():
    assert includes_todo('') == False

def test_normal_todo():
    assert includes_todo('Walk dog #TODO') == True

def test_lower_case():
    assert includes_todo('Drink water #todo') == False

def test_without_todo():
    assert includes_todo('some other random task') == False

def test_without_hash():
    assert includes_todo('no hash to find here... TODO') == False

def test_to_do():
    assert includes_todo('today I need #TO find something to DO') == False

def test_other_tests():
    assert includes_todo("#TODO buy milk") == True

def test_tea_test():
    assert includes_todo("drink tea") == False

def test_normie_test():
    assert includes_todo("learn to test-drive my code #TODO") == True
