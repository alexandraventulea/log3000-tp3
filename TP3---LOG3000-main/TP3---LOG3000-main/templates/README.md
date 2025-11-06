# Module templates
# Raison d'être du module
Ce répertoire contient les **templates HTML** pour afficher et interagir avec la calculatrice.
Les templates sont responsables de l’interface utilisateur : structure de la page, champs de saisie et boutons de la calculatrice.

# Principaux fichiers et responsabilités
- `index.html`  
  - Page principale de la calculatrice.
  - Affiche :
    - l’afficheur (`input` readonly) qui montre l’expression ou le résultat,
    - les boutons numériques (0–9),
    - les boutons d’opérations (+, -, *, /),
    - le bouton `=` qui envoie l’expression au serveur,
    - le bouton `C` qui efface l’afficheur côté client.
  - Contient un peu de JavaScript pour :
    - construire l’expression dans le champ `display`,
    - effacer le champ (fonction `clearDisplay`).

# Dépendances/Hypothèses
- Dans app.py, c’est la route `/` qui affiche le template `index.html` en utilisant return render_template('index.html', result=result).
