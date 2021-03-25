#!/usr/bin/python3

import sys
import os
import json

boom=open('boom.gz', 'rb').read()
secret=sys.argv[1]
ip=sys.argv[2]
token=sys.stdin.buffer.read(16).decode('utf-8').strip()

if token == secret:
    sys.stderr.write(ip)
    os.execlp('socat', 'socat', f'TUN:{ip},tun-name=sslvpn_server,up', '-')
else:
    if token.find('/react.js') > 0:
        sys.stdout.write('\r\n'.join([
            'HTTP/1.1 200 OK',
            'server: nginx/3.0',
            'connection: close',
            'content-type: application/javascript',
            'content-encoding: gzip',
            'content-length: %d' % len(boom),
            '\r\n']))
        sys.stdout.flush()
        sys.stdout.buffer.write(boom)
    else:
        sys.stdout.write('\r\n'.join([
            'HTTP/1.1 200 OK',
            'server: nginx/3.0',
            'connection: close',
            'content-type: text/html',
            '\r\n',
            '<html><body><script type="text/javascript" src="react.js"></body></html>']))
    sys.stdout.close()
