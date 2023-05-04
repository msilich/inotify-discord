FROM python:3.9-slim

# Setze Arbeitsverzeichnis
WORKDIR /app

# Kopiere Anforderungen und installiere sie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere das Python-Skript
COPY main.py .

# Setze Umgebungsvariable für den Discord-Webhook
ENV DISCORD_WEBHOOK_URL ""

# Starte das Skript
CMD ["python", "main.py"]
