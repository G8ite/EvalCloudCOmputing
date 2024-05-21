# EvalCloudComputing
## Présentation

EvalCloudCOmputing est une application web développée avec le framework Django qui permet aux utilisateurs de télécharger et de stocker des images en ligne. L'application offre des fonctionnalités telles que la génération automatique de tags et de descriptions pour les images téléchargées, l'affichage des images et des tags, la recherche d'images par tags ou descriptions, ainsi que la priorisation de l'optimisation. De plus, l'application est conçue pour être flexible, permettant une transition aisée entre les fournisseurs de services cloud.
Fonctionnalités

1. Téléchargement et Stockage d'Images

    Les utilisateurs peuvent télécharger des images via l'interface web, et les images sont stockées de manière sécurisée en ligne.

2. Génération de Tags et de Descriptions

    Lors du téléchargement d'une image, l'application génère automatiquement des tags et des descriptions pour les images à l'aide d'algorithmes basés sur l'IA.

3. Affichage des Images et des Tags

    Les utilisateurs peuvent consulter une liste complète des images téléchargées et des tags associés dans l'application.

4. Fonctionnalité de Recherche

    L'application prend en charge la recherche d'images basée sur les tags ou les descriptions, offrant aux utilisateurs un moyen pratique de trouver des images spécifiques.

5. Flexibilité du Fournisseur Cloud

    L'application est conçue pour permettre une transition facile entre les fournisseurs de services cloud, assurant ainsi une flexibilité et une évolutivité.

6. Priorité à l'Optimisation

    L'application accorde la priorité à l'optimisation pour garantir des performances rapides et efficaces, offrant aux utilisateurs une expérience fluide.

7. Suppression des images et réinitialisation des filtres
    Le bouton de suppression sur chaque image permet de supprimer une image du blob et de la db Azure, pour éviter d'être surcharger d'images de test.
    Le bouton réinitialiser les filtres permet lui d'annuler l'affichage des images par filtre

8. Affichage des images par filtre
    Lorsque vous être sur la page affichant tous les filtres, cliquer sur un filtre vous permettra d'afficher seulement les images concernées par ce filtre.


## Démonstration 

Vous pouvez accéder à une démo de l'application hébergée sur Microsoft Azure à l'adresse suivante : http://20.40.156.221/.


## Installation

Pour installer et exécuter EvalCloudCOmputing, suivez ces étapes :

Clonez le dépôt sur votre machine locale.
 - Installez Python et Django si ce n'est pas déjà fait.
 - Configurez les variables d'environnement requises pour le stockage 

    ```bash
    SECRET_KEY=
    AZURE_SECRET_KEY=
    DEBUG=True // si en local sinon False
    AZURE_SECRET_NAME=
    AZURE_SECRET_CONTAINER=
    BLOB_SECRET_URL=
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=
    COMPUTER_VISION_SUBSCRIPTION_KEY=
    COMPUTER_VISION_ENDPOINT=
    ```

- Accédez au répertoire du projet et exécutez les commandes suivantes :

    ```bash
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

 - Accédez à l'application via votre navigateur web à l'adresse http://localhost:8000.

## Docker 

Ce repo contient un Dockerfile permettant de lancer l'application dans un docker, il facilitera son déploiement sur différentes plateformes

## Architecture

EvalCloudCOmputing est développé avec le framework Django, qui suit une architecture de type Modèle-Vue-Contrôleur (MVC). Voici une vue d'ensemble de l'architecture mise en place :

 - Modèles (Models) : Les modèles Django sont utilisés pour définir la structure des données de l'application. Dans le cas d'EvalCloudCOmputing, les modèles sont utilisés pour représenter les images téléchargées, les tags associés et d'autres informations pertinentes. Par exemple, le modèle Image contient des champs tels que image, original_name, generated_name, tags, etc.

 - Vues (Views) : Les vues Django gèrent la logique métier de l'application et contrôlent le flux de données entre les modèles et les templates. Dans EvalCloudCOmputing, les vues sont responsables de fonctions telles que le téléchargement d'images, la génération de tags, l'affichage de listes d'images et de tags, la recherche d'images, etc.

 - Templates : Les templates Django sont utilisés pour générer et afficher les pages web de l'application. Les templates contiennent du code HTML avec des balises spéciales Django pour intégrer des données dynamiques. Par exemple, le template image_list.html est utilisé pour afficher la liste des images téléchargées, tandis que tag_list.html affiche la liste des tags disponibles.

 - Middleware : Un middleware personnalisé est utilisé pour dynamiquement mettre à jour les ALLOWED_HOSTS en fonction de l'URL du conteneur Azure. Cela permet une configuration flexible de l'application, en particulier lors du déploiement sur des plates-formes cloud telles que Microsoft Azure.

L'application utilise également le service de stockage Azure pour stocker les images téléchargées de manière sécurisée et efficace. En intégrant les services cloud, EvalCloudCOmputing garantit la scalabilité, la fiabilité et la performance de l'application, offrant ainsi une expérience utilisateur optimale.


## Remerciement

Merci à mes camarades Antoine et Marin pour leur soutien et leurs débloquages quand je ne savais plus quoi faire
Merci à Matthieu de m'avoir laissé expérimenté le Cloud Computing et de nous avoir fait confiance