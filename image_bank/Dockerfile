# Utilisez l'image Python officielle en tant qu'image de base
FROM python:3.11

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le contenu de l'application dans le conteneur
COPY . .

# Exposez le port sur lequel l'application fonctionne
EXPOSE 80

# Commande pour démarrer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
