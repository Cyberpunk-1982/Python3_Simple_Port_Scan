#! /usr/bin/python3

# Copyright 2019 Eliseu Silva Torres

import socket, sys

def port_scan(host):
	print('Port	Status')
	for port in range(1, 65536):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if sock.connect_ex((host, port)) == 0:
			print('{}	open'.format(port))
			sock.close()
			
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('IP is missing')
		sys.exit()
		
	port_scan(sys.argv[1])	
