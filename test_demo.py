
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
    assert my_div(8,4)== 2

def test_my_div_error():
    with pytest.raises(ZeroDivisionError,match="division by zero"):
        my_div(8,0)

    


