
import pytest

def somme (a,b):
    resultat = a+b
    return resultat
     
def my_min(a,b):
    resultat= a-b
    return resultat

def test_somme():
    assert somme(5,6) == 11 #test unitaire
    assert somme (-5,5)==0
    assert somme (-5,2)==-3

def test_my_min():
    assert my_min(8,5)==3
    assert my_min(9,8)==1

def my_div(a,b):
    return a/b

def test_my_div():
    assert my_div(8, 2) == 4
    assert my_div(9, 3) == 3

def test_my_div_zero_error():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        my_div(8, 0)

# print(my_div(8, 0))

# msg_error_pif.py
ERROR_WHILE_STRING = "La value ne peut pas être un string"

def function_au_pif(value):
    if type(value) == str:
        raise ValueError(ERROR_WHILE_STRING)
    if type(value) == bool:
        raise ValueError('La value ne peut pas être un bool')
    return True

def test_pif_str():
    with pytest.raises(ValueError, match=ERROR_WHILE_STRING):
        function_au_pif(True)

