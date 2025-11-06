# Module static
# Raison d'être du module
Ce répertoire contient les fichiers **statiques** utilisés par l’application Flask.  Il sert uniquement à stocker la feuille de
style qui définit l’apparence de la calculatrice.

# Principaux fichiers et responsabilités
- `style.css`  
  - Définit la mise en page de la calculatrice (centrage, tailles, couleurs).
  - Gère l’apparence de l’afficheur, des boutons numériques et des boutons d’opérateurs.
  - Utilise une grille CSS pour organiser les boutons en 4 colonnes comme une calculatrice physique.

# Dépendances/Hypothèses
- Le fichier est chargé dans le template html par le lien ci dessous :
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
