# Docker Compose Demo

A minimal Python (Flask) webserver that simulates a data processing job,
containerized for a docker-compose walkthrough.

## Files

- `app.py` — Flask server with `/` (view files) and `/process` (run the job) routes
- `input/` — sample input files, mounted **read-only** into the container
- `output/` — where processed results are written, mounted **read-write**
- `requirements.txt` — Python dependencies
- `Dockerfile` — builds the image
- `docker-compose.yml` — defines the `web` service with ports, env vars, and volumes

## Configuration

| Variable     | Default          | Purpose                              |
|--------------|------------------|--------------------------------------|
| `GREETING`   | `Hello`          | Heading shown on the page            |
| `APP_ENV`    | `development`    | Environment label shown on page      |
| `INPUT_DIR`  | `/mnt/input`     | Directory the app reads source files from |
| `OUTPUT_DIR` | `/mnt/output`    | Directory the app writes results to  |

## Run it (plain Docker)

```bash
# Build the image, tagging it "compose-demo"
docker build -t compose-demo .

# Run a container, mapping the port, passing env vars, and mounting the volumes
docker run --rm -p 8000:8000 \
  -e GREETING="Hello from docker run" \
  -e APP_ENV="plain-docker" \
  -e INPUT_DIR="/mnt/input" \
  -e OUTPUT_DIR="/mnt/output" \
  -v "$(pwd)/input:/mnt/input:ro" \
  -v "$(pwd)/output:/mnt/output" \
  compose-demo
```

## Run it (Docker Compose)

```bash
# Build and start
docker compose up --build

# In another terminal, trigger the processing job
curl -X POST http://localhost:8000/process

# Or just open http://localhost:8000 and click the button

# Stop and clean up
docker compose down
```

## What to observe

1. Open `http://localhost:8000` — input files are displayed, output is empty.
2. Click **Process input files** — the app reads from `/mnt/input` (read-only) and
   writes `processed_*.txt` files to `/mnt/output` (read-write).
3. Processed files appear in `output/` on the host immediately.
4. Try writing to the input mount from inside the container — it will be rejected:
   ```bash
   docker compose exec web touch /mnt/input/nope.txt
   # touch: cannot touch '/mnt/input/nope.txt': Read-only file system
   ```
