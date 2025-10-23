# Calculatrice Flask (LOG300-TP3-ÉQUIPE14)
## Description et objectif du projet 
Ce projet vise à fournir une calculatrice web accessible permettant aux utilisateurs d'effectuer des calculs arithmétiques de base directement depuis leur navigateur, sans nécessiter l'installation de logiciels supplémentaires. L'application est construite avec Flask pour assurer une architecture modulaire et maintenable.

Nous y trouvons:
- Interface de calculatrice web
- Opérations arithmétiques de base: Multiplication, soustraction, addition, division.
- Système de validation des expressions et gestion des erreurs

## Installation
### Prérequis
- Python 3.7 ou supérieur
- Pycharm ou un autre environnement qui soutient python
### Installation sur pycharm
1. Cloner le dépot sur votre machine locale
2. Installer l'interpréteur python
* Aller dans fichiers puis dans les settings et selectionner python interpreteur
* Appuyer sur Add interpreter --> Add Local Interpreteur --> Virtualenv
5. Installer Flask
  * Ouvrir un terminal depuis la racine du projet
  * Effectuer la commande: `pip install flask`
 
## Utilisation

### Lancer l'application

1. Exécuter la commande suiante depuis la racine du projet:
   `python app.py`
2. Ouvrez votre navigateur web et accédez à la route fournit par le terminal. Exemple:
   ```cpp
   Running on http://127.0.0.1:5000
### Utiliser la calculatrice

**1. Saisir une expression :**
Cliquez sur les boutons numériques et opérateurs pour construire votre expression.
Exemples :
- `5 + 3`
- `12 * 4`

**2. Calculer le résultat :** 
Cliquez sur le bouton `=` pour soumettre l'expression et afficher le résultat.

**3. Effacer l'affichage :**
Cliquez sur le bouton `C` pour réinitialiser la calculatrice.

## Tests
### Contenu
- `test_operators.py` : tests unitaires pour les fonctions `add`, `subtract`, `multiply` et `divide`.

### Exécution des tests
1. Ouvrir un terminal dans le dossier racine (`TP3---LOG3000-main/TP3---LOG3000-main`)  
2. Lancer pytest :

```bash
pytest
  ```

### Couverture
- Test des opérations avec nombres positifs et négatifs
- Test avec zéro
- Test avec nombres décimaux
- Test des exceptions (division par zéro)
## Flux de contribution

### Workflow des branches
- **master** : code stable et testé. Les commits directs sont interdits.  
- **dev** : intégration continue des fonctionnalités.  
- **feature/<nom-fonctionnalité>** : nouvelles fonctionnalités.  
- **bugfix/<nom-bug>** : correction de bugs.  
- **hotfix/<nom-correction>** : corrections urgentes en production.  

### Processus de contribution

1. **Créer une issue**  
   Décrivez le problème ou la fonctionnalité, les critères d'acceptation et toute info contextuelle.

2. **Créer une branche**
```bash
git checkout dev
git pull origin dev
git checkout -b feature/nom-de-la-fonctionnalite
git push --set-upstream origin <nom-de-la-branche>
```

3. **Commits**
```bash
git add .
git commit -m <message décrivant les modifications>
```
 **Conventions de commits:**
- `feat:` nouvelle fonctionnalité
- `fix:` correction de bug

- `docs:` documentation

- `style:` formatage, pas de changement de code

- `refactor:` refactorisation du code

- `test:` ajout ou modification de tests

4. **Créer une Pull Request**
- De votre branche vers master ou dev
- Inclure : description, lien vers l’issue, checklist, etc

5. **Revue de code**
- Au moins un autre développeur doit approuver.
- Donner du feedback pour les modifications






