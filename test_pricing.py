"""
Exercices Bloc 1 & 3 — voir J3_exercices_eleves.md.
Lancez : pytest test_pricing.py -v
"""
from booking import ticket_price, line_total, apply_promo, order_total
import pytest

# À vous d'écrire les tests.

def test_ticket_price():
    assert ticket_price("early_bird")==2495
    assert ticket_price("standard")==3500
    assert ticket_price("vip")==7500

##

def test_line_total():
    assert line_total("early_bird", 1) == 2495
    assert line_total("standard",2) == 7000
    assert line_total("vip",3) == 22500


def test_ticket_price_categ_inc():
    with pytest.raises(ValueError, match="Catégorie de billet inconnue"):   ##on met les erreurs
         ticket_price("early_birdddd")

 
def test_line_total_qinvalide():
    with pytest.raises(ValueError, match="La quantité doit être strictement positive"):
        line_total("early_bird", 0)

def test_line_total_qinvalide():
    with pytest.raises(ValueError, match="La quantité doit être strictement positive"):
        line_total("early_bird", 0)

####pas reussi ver solucionario de davit


def test_apply_promo_inactive():
    with pytest.raises(ValueError, match="Code promo inactif"):
        apply_promo(10000, promo)

def test_apply_promo_quota():
    with pytest.raises(ValueError, match="Code promo épuisé"):
        apply_promo(10000, promo)

def test_apply_promo_remise():
    with pytest.raises(ValueError, match="Pourcentage de remise invalide"):
        apply_promo(10000, promo)