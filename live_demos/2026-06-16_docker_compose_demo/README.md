# Docker Compose Demo

A minimal Python (Flask) webserver, containerized for a docker-compose walkthrough.

## Files

- `app.py` — placeholder Flask webserver with `/` and `/health` routes
- `requirements.txt` — Python dependencies
- `Dockerfile` — builds the image
- `docker-compose.yml` — defines the `web` service

## Run it (plain Docker)

```bash
# Build the image, tagging it "compose-demo"
docker build -t compose-demo .

# Run a container, mapping host port 8000 to container port 8000
docker run --rm -p 8000:8000 compose-demo
```

`--rm` cleans up the container when it stops; press Ctrl+C to stop it.

## Run it (Docker Compose)

```bash
# Build and start
docker compose up --build

# In another terminal, hit the server
curl http://localhost:8000
curl http://localhost:8000/health

# Stop and clean up
docker compose down
```

The server listens on port 8000 inside the container, published to
`localhost:8000` on the host.
