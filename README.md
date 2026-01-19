## Build & Run Cron Container

Build:
```bash
docker build -t soundcloud-cron:latest
```

Run:
```bash
docker run --rm \
    -v /mnt/ssd/media/Music:/app/media \
    -e MEDIA_DIR=/app/media \
    -e MEDIA_URL=https://soundcloud.com/vertical-asymptote/sets/edm \
    soundcloud-cron
```