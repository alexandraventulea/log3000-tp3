# Module backend
## Raison d’être du module

Ce module regroupe la logique de l'application Flask qui reçoit une expression arithmétique entrée par l’utilisateur, délègue le calcul aux fonctions du module `operators`, puis renvoie le résultat à la page HTML.

L’objectif est de séparer la **logique métier** (les opérations arithmétiques) et la **logique web** (routes Flask, formulaires, rendu du template).

## Principaux fichiers et responsabilités
- `app.py`  
  - Point d’entrée de l’application Flask.
  - Définit la route `/` (GET/POST).
  - Récupère l’expression envoyée par le formulaire HTML.
  - Appelle la fonction `calculate` pour évaluer l’expression.
  - Passe le résultat (ou un message d’erreur) au template `index.html` via `render_template`.

- `operators.py`  
  - Regroupe les opérations arithmétiques de base : `add`, `subtract`, `multiply`, `divide`.
  - Chaque fonction prend deux nombres en entrée et retourne le résultat de l’opération.

## Dépendances/Hypothèses
- Flask pour la partie serveur web.
- Le module `operators` est importé depuis `app.py`
- Le template `index.html` doit être présent dans le répertoire `templates/` attendu par Flask.
- On suppose que l’utilisateur saisit des expressions simples de la forme `a op b` (un seul opérateur parmi `+`, `-`, `*`, `/`), sans priorités d’opérations ni parenthèses.

