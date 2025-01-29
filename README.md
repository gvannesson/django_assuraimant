# django_assuraimant

# Application de Prédiction des Primes d'Assurance

## Contexte

Ce projet vise à développer une application Django fonctionnelle pour prédire les primes d'assurance en fonction des données des utilisateurs. L'application inclura une interface utilisateur intuitive et des fonctionnalités pour gérer les informations des utilisateurs et prédire leurs primes d'assurance.

## Fonctionnalités

### Fonctionnalités principales

1. **Base de données SQLite** : 
   - Stockage des informations utilisateurs (nom, email, caractéristiques liées à l’assurance).
   - Sécurisation des mots de passe (hachage).

2. **Page d’accueil** : 
   - Présentation de l’application avec boutons pour l'inscription et la connexion.

3. **Système d’authentification** :
   - Inscription, validation des données, connexion et déconnexion.

4. **Page Profil** :
   - Affichage et mise à jour des informations personnelles.

5. **Page de prédiction** :
   - Prédiction de la prime d’assurance en fonction des données utilisateur.

6. **Interface utilisateur** :
   - Design avec Tailwind CSS, expérience utilisateur fluide.

7. **Production** :
   - Mode DEBUG désactivé pour la production.

### Fonctionnalités bonus

1. **Historique des prédictions** :
   - Enregistrement des prédictions avec utilisateur, date et résultats.

2. **Formulaire interactif** :
   - Prévisualisation des résultats avant soumission.

3. **Améliorations UX** :
   - Notifications dynamiques et thème responsive.


## Livrables

1. **Application Django fonctionnelle** :
   - Code propre et documenté, fichiers statiques pour le front-end (CSS, JS).

2. **Présentation** :
   - Slides expliquant les objectifs, la solution technique et une démo de l’application.

3. **Documentation** :
   - Instructions d’installation et explication des choix techniques.

## Technologies Utilisées

- **Back-end** : Django MVT, SQLite
- **Front-end** : HTML, CSS, Tailwind CSS, JavaScript
- **Sécurité** : Hachage des mots de passe, validation des entrées utilisateur

## Structure du Projet

- **Tables** :
  - Utilisateur personnalisé
  - Historique

- **Routes** :
  - `/`: Page d’accueil
  - `/signup`: Inscription
  - `/login`: Connexion
  - `/profile`: Profil utilisateur
  - `/predict`: Prédiction de prime
  - `/appointment`: Rendez-vous (bonus)
  - `/docs`: Documentation technique (bonus)

## Instructions d’installation

1. Clonez le projet :
   git clone https://github.com/gvannesson/django_assuraimant


2. Créez un environnement virtuel et activez-le :
    python3 -m venv venv
    source venv/bin/activate  # Windows : venv\Scripts\activate

3. Installez les dépendances :
    pip install -r requirements.txt

4. Appliquez les migrations  puis lancez le serveur :
    cd assuraimant
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
    python manage.py runserver

5. Accédez à l’application sur :
    http://127.0.0.1:8000


## Choix Techniques

- **Django** : Framework robuste pour la gestion des données et des formulaires.
- **SQLite** : Base de données légère pour le développement rapide.
- **Tailwind CSS** : Framework CSS pour un design flexible et responsive.
- **Sécurité** : Hachage des mots de passe avec Django.
