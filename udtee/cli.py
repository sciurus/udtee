"""CLI-specific functions"""

import argparse
from udtee import config
from udtee import main


def run():
    """Entry point for the CLI"""
    parser = argparse.ArgumentParser(
        description="Mirror UDP traffic from source to destinations."
    )
    parser.add_argument(
        "-s", "--source", help="Address to listen on. Example: localhost:10000"
    )
    parser.add_argument(
        "-d",
        "--destinations",
        help="Comma-seperated list of addresses to mirror to. Example: example.com:20000,example.com:30000",  # pylint: disable=line-too-long
    )
    args = parser.parse_args()

    source, destinations = config.parse(args.source, args.destinations)
    main.tee(source, destinations)
