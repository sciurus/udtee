# UDTee

UDTee is a utility for mirroring UDP traffic sent to a source to multiple destinations. It may be useful for dual-writes during a migration between systems whose protocols use UDP, like statsd or syslog. For example, you could configure your application to send statsd to UDTeee and have UDTee send it to both datadog and telegraf.

The source and destination may be set via the command-line, like so

```
usage: udtee [-h] [-s SOURCE] [-d DESTINATIONS]

Mirror UDP traffic from source to destinations.

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Address to listen on. Example: localhost:1000
  -d DESTINATIONS, --destinations DESTINATIONS
                        Comma-seperated list of addresses to mirror to. Example: example.com:2000,example.com:3000
```

Alternately, you can set them via the `UDTEE_SOURCE` and `UDTEE_DESTINATIONS` environment variables.