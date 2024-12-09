# Utiliser une image Python légère comme base
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt pour installer les dépendances
COPY requirements.txt requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Commande par défaut pour lancer l'application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
