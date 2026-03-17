"""Micro-application: the supported interface for the tiny demo."""

from __future__ import annotations

import argparse

from mini_house.tools import summarize_house


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mini-house",
        description="Micro-application for the tiny demo house project.",
    )
    parser.add_argument("--room", default="kitchen", help="Room to frame.")
    parser.add_argument(
        "--boards",
        type=int,
        default=8,
        help="How many boards to use for the framing estimate.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(summarize_house(room_name=args.room, board_count=args.boards))


if __name__ == "__main__":
    main()
