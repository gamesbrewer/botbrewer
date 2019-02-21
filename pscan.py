import sys
import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host')
args = parser.parse_args()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((args.host, port))
        if result == 0:
            print("Port: {} Open".format(port))
        sock.close()
except KeyboardInterrupt:
    sys.exit()