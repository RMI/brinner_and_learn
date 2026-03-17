# Tiny demo: libraries can't run themselves

This is a deliberately small `uv` project for the slide deck.

It shows three different roles in one repo:

- `src/mini_house/tools.py`: a tiny reusable library
- `scripts/frame_wall.py`: a script for one task
- `src/mini_house/app.py`: a micro-application with a supported CLI

## Run it

Create the environment:

```bash
uv sync
```

Run the task-focused script:

```bash
uv run python scripts/frame_wall.py
```

Run the supported application interface:

```bash
uv run mini-house --room kitchen
uv run mini-house --room office --boards 12
```

## The point

The library contains reusable logic.
The script runs one piece of work.
The application is the supported way a user would interact with the project.
