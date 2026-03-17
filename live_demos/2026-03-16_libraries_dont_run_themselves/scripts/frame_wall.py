"""Task-focused script for one part of the tiny demo project."""

from mini_house.tools import estimate_boards


def main() -> None:
    print("Framing one wall...")
    print(estimate_boards(room_name="office", board_count=6))


if __name__ == "__main__":
    main()
