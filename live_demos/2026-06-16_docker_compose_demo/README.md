# Docker Compose Demo

A minimal Python (Flask) webserver that simulates a data processing job,
containerized for a docker-compose walkthrough.

## Files

- `app.py` — Flask server: hit counter (Postgres), file viewer, and processing job
- `input/` — sample input files, mounted **read-only** into the container
- `output/` — where processed results are written, mounted **read-write**
- `requirements.txt` — Python dependencies
- `Dockerfile` — builds the `web` image
- `docker-compose.yml` — defines the `web` and `db` services

## Services

| Service | Image | Purpose |
|---------|-------|---------|
| `web` | built from `Dockerfile` | Flask app |
| `db` | `postgres:alpine` | hit counter storage |
| `adminer` | `adminer` | web-based DB admin UI (port 8080) |

## Configuration

| Variable       | Default                                      | Purpose                          |
|----------------|----------------------------------------------|----------------------------------|
| `GREETING`     | `Hello`                                      | Heading shown on the page        |
| `APP_ENV`      | `development`                                | Environment label                |
| `INPUT_DIR`    | `/mnt/input`                                 | Read-only source files           |
| `OUTPUT_DIR`   | `/mnt/output`                                | Read-write results directory     |
| `DATABASE_URL` | `postgresql://demo:demo@localhost:5432/demo` | Postgres connection string       |

## Run it (plain Docker)

With two containers you need to wire the network yourself — this is the pain Compose removes.

```bash
# Build the image
docker build -t compose-demo .

# Create a shared network
docker network create demo-net

# Start Postgres on that network
docker run -d --name db --network demo-net \
  -e POSTGRES_USER=demo \
  -e POSTGRES_PASSWORD=demo \
  -e POSTGRES_DB=demo \
  postgres:alpine

# Start the web container on the same network
docker run --rm -p 8000:8000 --network demo-net \
  -e GREETING="Hello from docker run" \
  -e APP_ENV="plain-docker" \
  -e INPUT_DIR="/mnt/input" \
  -e OUTPUT_DIR="/mnt/output" \
  -e DATABASE_URL="postgresql://demo:demo@db:5432/demo" \
  -v "$(pwd)/input:/mnt/input:ro" \
  -v "$(pwd)/output:/mnt/output" \
  compose-demo

# Clean up
docker stop db && docker rm db
docker network rm demo-net
```

## Run it (Docker Compose)

```bash
# Build and start both services
docker compose up --build

# Open http://localhost:8000 — hit count increments on each refresh

# Trigger the processing job
curl -X POST http://localhost:8000/process

# Check the health endpoint (reports db connectivity)
curl http://localhost:8000/health

# Stop and clean up containers (named volume pg-data persists)
docker compose down

# Stop AND delete the named volume (resets hit count)
docker compose down -v
```

## Adminer (DB admin UI)

Open `http://localhost:8080` and log in:

| Field    | Value        |
|----------|--------------|
| System   | `PostgreSQL` |
| Server   | `db`         |
| Username | `demo`       |
| Password | `demo`       |
| Database | `demo`       |

## What to observe

1. Each page refresh increments the hit counter stored in Postgres.
2. `docker compose down` then `up` again — counter resumes where it left off (named volume).
3. `docker compose down -v` then `up` — counter resets (volume deleted).
4. The `db` hostname in `DATABASE_URL` resolves automatically — Compose DNS, no `/etc/hosts` editing needed.
5. Try writing to the read-only input mount:
   ```bash
   docker compose exec web touch /mnt/input/nope.txt
   # touch: cannot touch '/mnt/input/nope.txt': Read-only file system
   ```
