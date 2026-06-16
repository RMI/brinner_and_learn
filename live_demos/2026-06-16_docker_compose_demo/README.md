# Docker Compose Demo

A minimal Python (Flask) webserver, containerized for a docker-compose walkthrough.

## Files

- `app.py` — Flask webserver that reads env vars + a data file and shows them on `/`
- `data/data.txt` — sample data read by the app at request time
- `requirements.txt` — Python dependencies
- `Dockerfile` — builds the image
- `docker-compose.yml` — defines the `web` service (incl. environment variables)

## Configuration

The app reads three environment variables (all optional, with defaults):

| Variable    | Default       | Purpose                          |
|-------------|---------------|----------------------------------|
| `GREETING`  | `Hello`       | Heading shown on the page        |
| `APP_ENV`   | `development` | Environment label shown on page  |
| `DATA_FILE` | `data.txt`    | Path to the file whose contents are displayed |

## Run it (plain Docker)

```bash
# Build the image, tagging it "compose-demo"
docker build -t compose-demo .

# Run a container, mapping the port, passing env vars, and mounting the data file
docker run --rm -p 8000:8000 \
  -e GREETING="Hello from docker run" \
  -e APP_ENV="plain-docker" \
  -e DATA_FILE="/mnt/data/data.txt" \
  -v "$(pwd)/data:/mnt/data" \
  compose-demo
```

With the volume mount, edit `data.txt` on the host and refresh the page —
the change shows up immediately, no rebuild needed.

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
