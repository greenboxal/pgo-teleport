# Pokemon Go Teleport

This is a [mitmproxy](https://mitmproxy.org) script that teleports you around the globe.

It's useful for playing Pokemon Go before it is released in your country.

## How It Works

This scripts intercepts all messages between the client and the server and translates all used coordinates.

The server thinks that you're in the target location. The client still behaves like it's in your current location like the pokemons were really spawned in your local area.

## Usage

First, you need to install [mitmproxy](https://mitmproxy.org).

Then do the following:

1. Edit `local_lat`, `local_lng`, `target_lat` and `target_lng` variables
2. Run `mitmdump -s tunnel.py --ignore '^(?!pgorelease\.nianticlabs\.com)' -q`
3. Change your cellphone proxy settings and install mitmproxy CA
4. Profit

## Dependencies

* s2sphere
* protobuf >= 3

