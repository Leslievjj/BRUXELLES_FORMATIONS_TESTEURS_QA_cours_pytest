"""
Exercices Bloc 1 & 3 — voir J3_exercices_eleves.md.
Lancez : pytest test_pricing.py -v
"""
from booking import ticket_price, line_total, apply_promo, order_total

# À vous d'écrire les tests.

MAX_TICKETS_PER_ORDER = 6  # RM3 EventFlow : 6 billets maximum par commande

TICKET_PRICES_CENTS = {
    "early_bird": 2495,
    "standard": 3500,
    "vip": 7500,
}


# --- Fonctions "pures" (sans dépendance externe) ---------------------------

def ticket_price(category):

    """Prix unitaire d'une catégorie de billet, en centimes.

    Lève ValueError si la catégorie n'existe pas.
    """
    if category not in TICKET_PRICES_CENTS:
        raise ValueError(f"Catégorie de billet inconnue : {category!r}")
    return TICKET_PRICES_CENTS[category]

def test_ticket_price():
    assert ticket_price("early_bird")==2495
    assert ticket_price("standard")==3000
    assert ticket_price("vip")==7500


def line_total(category, quantity):
    """Prix total pour une catégorie et une quantité, en centimes.

    Lève ValueError si la quantité n'est pas strictement positive.
    """
    if quantity <= 0:
        raise ValueError("La quantité doit être strictement positive")
    return ticket_price(category) * quantity

def test_line_total():
    assert line_total("early_bird")*1==2495
    assert line_total("standard")*1==3000
    assert line_total("vip")*1==7500
