import inotify.adapters
import os
import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to send a notification to Discord using a webhook
def send_discord_notification(webhook_url, message):
    data = {"content": message}
    response = requests.post(webhook_url, json=data)

    if response.status_code != 204:
        raise ValueError(f"Request failed: Status {response.status_code}, Text: {response.text}")

def main():
    folder = "/folderwatch"
    discord_webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

    # Check if the webhook URL environment variable is set
    if not discord_webhook_url:
        raise ValueError("DISCORD_WEBHOOK_URL Umgebungsvariable ist nicht gesetzt!")

    # Create an InotifyTree to monitor the folder and its subfolders
    inotify_tree = inotify.adapters.InotifyTree(folder)

    # Iterate through the generated events
    for event in inotify_tree.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

        # Filter the events we are interested in
        if "IN_CREATE" in type_names or "IN_DELETE" in type_names:
            message = f"Ordner: [{path}] Datei:[{filename}] Typ: {type_names}"
            logging.info(message)

            # Send a Discord notification with the timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            discord_message = f"{timestamp} - {message}"

            # Send a Discord notification
            #send_discord_notification(discord_webhook_url, message)
            send_discord_notification(discord_webhook_url, discord_message)



if __name__ == "__main__":
    main()
