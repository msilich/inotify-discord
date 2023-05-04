# Inotify Discord Notifier

This Python script monitors a folder and its subfolders for file changes and sends a Discord notification through a webhook when a file is created, modified, or deleted. The script runs inside a Docker container, and the folder is mounted as a read-only volume.

## Prerequisites

- Docker Engine installed on your Linux system

## Usage

1. Clone this repository:

```bash
git clone https://github.com/msilich/inotify-discord.git
cd inotify-discord
```

2. Build the Docker container:
```bash
docker build -t inotify-discord .
```

3. Run the Docker container:
```bash
docker run -d \
  --name inotify-discord \
  -e DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/your-webhook-url" \
  -v /cinema:/path/to/your/folder:ro \
  inotify-discord
