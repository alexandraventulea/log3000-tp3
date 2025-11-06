"""
Implémentation des opérations arithmétiques de base utilisées par la calculatrice.

Ce module isole les opérations (+, -, *, /) pour faciliter les tests unitaires et la correction de bogues sans toucher au reste de l'application.
"""

def add(a,b):
    """
    Additionne deux nombres.

    Paramètres:
        a: Premier opérande (nombre).
        b: Deuxième opérande (nombre).

    Retourne:
        La somme de a et b.
    """
    return a + b

def subtract(a,b):
    """
    Soustrait deux nombres.

    Paramètres:
        a: Premier opérande (nombre).
        b: Deuxième opérande (nombre).

    Retourne:
        La différence a - b.
    """
    return a - b

def multiply(a,b):
    """
    Multiplie deux nombres.

    Paramètres:
        a: Premier opérande (nombre).
        b: Deuxième opérande (nombre).

    Retourne:
        Le produit a * b.
    """
    return a * b

def divide(a,b):
    """Divise deux nombres.

    Paramètres:
        a: Numérateur (nombre).
        b: Dénominateur (nombre, non nul).

    Retourne:
        Le quotient a / b.

    Exceptions levées:
        ZeroDivisionError: Si b vaut zéro.
    """
    return a / b
