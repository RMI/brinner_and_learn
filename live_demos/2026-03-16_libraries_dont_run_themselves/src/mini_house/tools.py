"""Reusable library code for the tiny demo project."""


def estimate_boards(room_name: str, board_count: int) -> str:
    """Return a tiny framing estimate for a room."""
    return f"For the {room_name}, bring {board_count} boards and a measuring tape."


def summarize_house(room_name: str, board_count: int) -> str:
    """Return a user-facing summary for the micro-application."""
    plan = estimate_boards(room_name=room_name, board_count=board_count)
    return f"Mini house plan: {plan} Then call paint and inspection later."
