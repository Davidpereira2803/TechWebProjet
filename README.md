# Projet Technologies Web
## Introduction
Ce projet présente un site web pour un restaurant et propose une présentation du restaurant ainsi que les fonctionalitées pour les clients de passer des commandes et de réserver une table. Pour le staff on a la possibilité d'éditer le menu, c’est-à-dire ajouter, effacer et éditer les plats. De plus le staff peut aussi voir les commandes et les marquer comme prêtes. Les utilisateurs peuvent aussi laisser des commentaires qui seront visibles pour le staff dans la base de données. Quelques pages web sont différentes ou que accessible pour l'administrateur(staff), comme par exemple la page ***'order_management.html'*** pour gérer les commandes et les pages de manipulations des plats.

## Comment lancer le site
Afin de lancer le site web, il faut tout d'abbord lancer le serveur, avec la commande ```python main.py```. Dans la console il y aura l'addresse du site ainsi que le message ***''Le coin de Namur' is on AIR!'*** afin d'indiquer que le serveur est bien lancé.

## Routes
### Routes pour les menus
Prefix: '/menu'
- '/all/dishes'
- '/add/dish'
- '/remove/dish'
- '/edit/dish'

### Routes pour les orders
Prefix: '/orders'
- '/order'
- '/my/orders'
- '/add/basket'
- '/remove/basket'
- '/checkout'
- '/cancel/order'
- '/get/orders'
- '/complete'

### Routes pour les table bookings
Prefix: '/table'
- '/book/table'
- '/manage'
- '/change/availability'

### Routes pour les users
Prefix: '/users'
- '/me'
- '/new/user'
- '/change/password'
- '/change/user/information'
- '/home'
- '/login'
- '/logout'
- '/profile'

### Routes pour le feedback
Prefix: '/feedbacks'
- '/feedback'

## Fonctionalités
Comme dit avant quelques pages ne sont que accessible pour le staff, par contre toutes les fonctionalités des clients est aussi disponibles pour le staff:





### Utilisateur (Client)
- Voir les élèments du menu (sans un login)
- Création d'un compte
- Login/ Logout
- Accèder à la page Profile 
    - Changer le prènom, nom et email
    - Changer le mot de passe, en fournissont le mot de passe actuel
- Accèder à la page My Orders, pour voir les commandes de l'utilisateur
- Laisser un commentaire, en indiquant l'email ainsi que le password
- Réserver une table en indiquant le jour, l'heure ainsi que le nombre de personnes
- Passer des commandes
    - Ajouter des éléments au panier
    - Retirere des éléments du panier
    - Faire un checkout
    - Annuler la commande
    - Dans la page My Orders, suivre le status de la commande ("working", "finished")

### Administrateur (Staff)