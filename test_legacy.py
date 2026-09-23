"""
Exercice Bloc 2 — Code hérité (voir énoncé).
Lisez la spécification dans legacy_pricing.py, concevez vos cas, écrivez vos
tests, lancez-les, et diagnostiquez tout écart avec la spécification.
Lancez : pytest test_legacy.py -v
"""
from legacy_pricing import loyalty_discount_percent, price_with_loyalty

# À vous d'écrire les tests.

def test_loyalty_discount_percent():

    ##a tester valeurs: 0,2,3,9,10,100

    assert loyalty_discount_percent(0)==0
    assert loyalty_discount_percent(2)==0
    assert loyalty_discount_percent(3)==5
    assert loyalty_discount_percent(9)==5
    assert loyalty_discount_percent(10)==10
    assert loyalty_discount_percent(100)==10

def test_price_with_loyalty():
    #a tester 
    assert price_with_loyalty(100,2)==100-(100*0//100)
    assert price_with_loyalty(200,20)==200-(200*10//100)
    assert price_with_loyalty(150,200)==150-(150*10//100)
    assert price_with_loyalty(100,0)==100-(100*0//100)
    assert price_with_loyalty(100,3)==100-(100*5/100)
  

