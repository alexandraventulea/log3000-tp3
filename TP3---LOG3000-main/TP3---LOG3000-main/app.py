""" 
Application Flash pour une calculatrice web simple.

Ce module expose:
- Une fonction 'calculate' qui évalue une expression arithmétique de la forme "a op b".
- Une route Flask qui affiche la page HTML et calcule le résultat à partir de l’expression saisie par l’utilisateur.

Dépend de:
- Flask pour la partie serveur web.
- Le module operators pour les opérations arithmétiques de base.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire qui fait le lien entre le symbole de l'opérateur dans l'expression
# et la fonction Python qui implémente réellement l'opération.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression arithmétique de la forme 'a op b'

    L'expression attendue contient exactement:
    - Un opérande gauche (nombre),
    - Un opérateur parmi +, -, *, /,
    - Un opérande droit (nombre),
    sans parenthèses ni priorité d'opérateurs.

    Paramètres:
        expr: Expression arithmétique fournie par l'utilisateur, par exemple "2+3".

    n:
        Le résultat de l'opération de type float.

    Exceptions levées:
        ValueError: Si l'expression est vide, mal formée, contient plusieurs opérateurs ou des opérandes non numériques.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")
    
    # On supprime les espaces pour tolérer des expressions comme "2 + 3".
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # On recherche la position (unique) de l'opérateur dans la chaîne.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                # On interdit plusieurs opérateurs pour garder une grammaire simple.
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # Cas où l'opérateur est au début, à la fin, ou absent :
        # dans tous ces cas, le format ne correspond pas à "a op b".
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        # On montre explicitement que seuls des nombres sont acceptés.
        raise ValueError("operands must be numbers")
    
    # À ce stade, on délègue le calcul à la fonction d'opérateur correspondante.
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application.

    - En GET : affiche la page de la calculatrice avec un affichage vide.
    - En POST : récupère l'expression envoyée par le formulaire, appelle `calculate`
      et affiche soit le résultat, soit un message d'erreur.

    Returns:
        Le rendu HTML du template 'index.html' avec la valeur à afficher dans le champ `result`.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # On retourne un message d'erreur lisible pour l'utilisateur.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Mode debug activé pour le développement local.
    # À désactiver sur le vrai site en ligne, il ne faut pas laisser debug= True car ça peut montrer des informations sensibles.
    app.run(debug=True)