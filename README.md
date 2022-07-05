# Média Manager (nom de code initial R2M)

## Contexte de l'application

Cette application a pour but de faciliter le monitoring et la gestion d'un service de prestation vidéo d'une entreprise pour des avocats, experts-comptables et maires. Concrètement les clients (avocats, experts-comptables, maires) cherchent à gagner en visibilité. L'entreprise propose de réaliser des vidéos interview pour eux et diffusée sur le média de l'entreprise.

## Comment ouvrir l'application ?

Une fois dans le dossier ```r2m```, entrez la commande ci-dessous dans votre terminal pour installer toutes les dépendances nécessaires pour utiliser l'application
```bash
pip install -r requirements.txt
```
Ensuite rentrer cette commande dans le même dossier pour lancer le server local
```bash
python manage.py runserver
```
Rentrez l'adresse locale générée dans votre barre d'URL de votre navigateur pour accéder à l"application

## Comment lire le code de mon projet ?

Chaque page web de l'application possède un URL. les URLs sont codés dans le fichier python ```r2m/dashboard/urls.py```. Chaque url, une fois ouvert active une fonction python codée dans le fichier ```r2m/dashboard/views.py```. Chaque fonction retourne des données dans le fichier HTML de la page concernée afin de pouvoir les afficher (les fichiers HTML sont disponible dans le dossier ```r2m/dashboard/templates/dashboard/```). Chaque donnée traitée par python provient d'une base de données. Chaque base de données a été conçue par un modèle. Tous les modèles sont codés dans le fichier python ```r2m/dashboard/models.py```. Le fichier ```r2m/dashboard/forms.py``` contient les fonctions permettant d'enrichir la base de données directement dans l'application.


