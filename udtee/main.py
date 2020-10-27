"""Functions to export"""

from urllib.parse import urlparse


def tee(source, destinations):
    """Mirror UDP traffic from soruce to destinations"""
    print(split_host_and_port(source))
    for destination in destinations:
        print(split_host_and_port(destination))


def split_host_and_port(address):
    """Parse address string into host and port"""
    url = urlparse(f"//{address}")
    if not url.port:
        raise ValueError
    return url.hostname, url.port
