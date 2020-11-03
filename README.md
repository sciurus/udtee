# UDTee

UDTee is a utility for mirroring UDP traffic sent to a source to multiple destinations. It may be useful for dual-writes during a migration between systems whose protocols use UDP, like statsd or syslog. For example, you could configure your application to send statsd to UDTeee and have UDTee send it to both datadog and telegraf.

# Installation

UDTee may be installed from PyPI via `pip install udtee`.

It is also available as a docker image via `docker pull brianpitts/udtee`.

# CLI Usage

The source and destination may be set via the command-line, like so

```
usage: udtee [-h] [-s SOURCE] [-d DESTINATIONS]

Mirror UDP traffic from source to destinations.

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Address to listen on. Example: localhost:10000
  -d DESTINATIONS, --destinations DESTINATIONS
                        Comma-seperated list of addresses to mirror to. Example: example.com:20000,example.com:30000
```

Alternately, you can set them via the `UDTEE_SOURCE` and `UDTEE_DESTINATIONS` environment variables.

## Examples

* `udtee --source=localhost:10000 --destinations=example.com:20000,example.com:30000`
* `docker run --network='host' -e UDTEE_SOURCE='localhost:10000' -e UDTEE_DESTINATIONS='example.com:20000,example.com:30000' brianpitts/udtee`

# Library Usage

The udtee module exports a tee function, which takes two arguments: an address to listen on, and a list of addresses to send to. In both cases, the address must be a tuple of the host and port.

## Example

```
import udtee

udtee.tee(("localhost", 10000), [("example.com", 20000),("example.com", 30000)])
```