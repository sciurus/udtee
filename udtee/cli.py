"""CLI-specific functions"""

from udtee import config
from udtee import main


def run():
    """Entry point for the CLI"""
    source, destinations = config.parse("foo", "bar")
    main.tee(source, destinations)
