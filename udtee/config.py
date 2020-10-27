"""Handles configuration parsing"""

import os
from argparse import ArgumentError


def parse(source_arg, destinations_arg):
    """Parse configuration from CLI"""
    if source_arg:
        source = source_arg
    elif os.getenv("UDTEE_SOURCE"):
        source = os.getenv("UDTEE_SOURCE")
    else:
        raise ArgumentError

    if destinations_arg:
        destinations = destinations_arg.split(",")
    elif os.getenv("UDTEE_DESTINATIONS"):
        destinations = os.getenv("UDTEE_DESTINATIONS").split(",")
    else:
        raise ArgumentError

    return source, destinations
