# Utiliser une image Python officielle, stable (exemple 3.11)
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements.txt et main.py
COPY requirements.txt .
COPY main.py .

# Installer les dépendances sans cache pour alléger l'image
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du projet (si besoin)
COPY . .

# Exposer le port si Flask ou autre API est utilisée (exemple 8080)
EXPOSE 8080

# Commande pour lancer le bot (adapter selon ton script)
CMD ["python", "main.py"]
