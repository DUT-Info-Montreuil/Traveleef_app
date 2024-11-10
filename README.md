# Traveleef_frontend

# Guide d'utilisatation 

# Prérequis : 

- Node.js installé (version LTS recommandée)
- Npm (gestionnaire de paquet Node, inclut avec Node.js)
- Git
- Docker (version LTS recommandée)
- VsCode (éditeur de code) ou IDE (Environnement de développement) comme Webstorm (pour codé sur le web) et Pycharm (pour codé en python) (optionnel)

# Installation : 

1. Cloner le projet avec la commande : git clone ```<LIEN_DU_REPO_GITHUB>```
2. Accéder au dossier du projet "Traveleef_app"
3. Ouvrir un terminal sur le même chemin que le dossier contenant le frontend Angular ```cd Traveleef_app/frontend/traveleef-app```. Puis effectuée les commandes suivantes : ```npm install``` pour installé les dépendances Node, puis ```ng build``` pour construire l'application.
4. Revenez au répertoire racine du projet "Traveleef_app" et exécutez la commande suivante dans le terminal pour démarrer le projet : ```docker compose up -d```.

# Information utilitaire : 

. Pour accéder à l'application côté frontend, ouvrez votre navigateur et rendez-vous à l'adresse suivante : http://localhost:4200
. Le backend n'est pas directement accessible via le navigateur pour des raisons de sécurité. Toutefois, si vous souhaitez y accéder, vous pouvez configurer un port dans le fichier docker-compose.yml du backend afin de permettre un accès externe.
. La base de donnée est accessible depuis le terminal en utilisant la commande suivante : ```docker exec -it <ID_conteneur ou nom conteneur postgresql> psql -U <NOM_UTILISATEUR> -d <BASE_DE_DONNEE>```. Cela vous permet de vous connecter au conteneur PostgreSQL pour interagir avec la base de données.
