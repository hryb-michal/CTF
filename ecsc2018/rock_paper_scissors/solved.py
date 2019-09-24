#!/usr/bin/env python

import socket
import select
import time
import random

def read_response(sock):
	ready = select.select([sock], [], [], 0.05)
	response = ''
	while(ready[0]):
		data = sock.recv(4096)
		if(len(data) > 0):
			response += str(data);
			ready = select.select([sock], [], [], 0.05)
		else:
			break
	return response

moves = ['8<', 'O', '__', '8<', '__', 'O', '8<', '8<', '__', 
'__', '8<', '8<', 'O', '8<', 'O', 'O', '8<', '8<', 'O', 'O', 
'8<', 'O', '__', '8<', '__', '__', 'O', '__', '8<', 'O', '8<',
 'O', 'O', '__', '8<', '__', '__', 'O', '8<', 'O', '__', '8<',
  'O', '__', 'O', '__', '__', 'O', '8<', 'O']

orig_moves = ['_', '8', 'O', '_', 'O', '8', '_', '_', 'O', 'O', '_', '_', '8',
 '_', '8', '8', '_', '_', '8', '8', '_', '8', 'O', '_', 'O', 'O',
  '8', 'O', '_', '8', '_', '8', '8', 'O', '_', 'O', 'O', '8', '_',
   '8', 'O', '_', '8', 'O', '8', 'O', 'O', '8', '_', '8']

transform = {
	'8' : 2,
	'O' : 0,
	'_' : 1
}

moves_int = []

for i in orig_moves:
	moves_int.append(transform[i])
print(moves_int)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('ecsc18.hack.cert.pl', 10021))
print(read_response(sock))	#welcome message

for i in moves:
	sock.send(str.encode(i + '\n'))
	resp = read_response(sock)
	print(resp)

	if(resp.find('cheated') != -1):
		print('magic num: ' + str(313487))
		sock.send(str.encode(str(313487) + '\n'))
		resp2 = read_response(sock)
		print(resp2)
		break

sock.close()

#i = 0
'''

for seed in range(0,65536):
	random.seed(seed)
	ctr = 0
	temp_moves = []
	for i in moves_int:
		move = random.randint(0, 2)
		if (i != move):
			break
		ctr += 1
		temp_moves.append(move)
		if (ctr == 50):
			print ('suspected seed: ' + str(seed))
			print(temp_moves)
			print(random.randint(0, 10**6))
			'''