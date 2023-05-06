#author:jiangjixiang
#仅用于长安和北斗的内部交流，禁止传给第三方
#!/usr/bin/env python3

import binascii
import time
import socket
import struct
import sys

def main(filename, ip, port, mode):
    addr = (ip, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if mode == 'multicast':
        # Set the time-to-live for messages to 1 so they don't go beyond the local network segment
        ttl = struct.pack('b', 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    f = open(filename)
    for data in f.readlines():
        data = data.strip()
        if len(data) % 2 != 0:
            print('len(data) must be 2*n, but len(data): %d, data: %s' %
                  (len(data), data))
            continue
        try:
            data = binascii.a2b_hex(data)
            sock.sendto(data, addr)
            time.sleep(0.005)
        except Exception as e:
            print(e)
            print("current data: " + data)
    sock.close()


if __name__ == '__main__':
    data_file_name = "data.txt"
    ip = "127.0.0.1"
    port = 10000
    mode = "unicast"
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == 'multicast':
            ip = "225.0.6.21"
    assert mode in ["multicast", "unicast"]
    print("ip: %s, port: %d, mode: %s" %(ip, port, mode))
    main(data_file_name, ip, port, mode)
