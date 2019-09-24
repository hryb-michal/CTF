#!/usr/bin/python
import time
import random
from zlib import crc32
import buffering_hack

ROUND_NO = 50
FLAG = open('flag', 'rb').read()
MOVES = ['O', '__', '8<']
WELCOME_TEXT = "Welcome, win with me %d times and I'll give you the flag" % ROUND_NO

def wins_over(what, second_what):
	return (second_what + 1) % 3 == what

with open('flag') as f:
	magic_numb = crc32(f.read()) & 0xffff
random.seed(magic_numb)

print(WELCOME_TEXT)

for r in range(ROUND_NO):
	my_move = random.randint(0, 2)
	
	your_move = raw_input("Enter your move: ").strip()
	if your_move not in MOVES:
		print("That is not a valid move!\nYou lose!")
		exit()

	your_move = MOVES.index(your_move)

	print("My move: %s" % MOVES[my_move])
	print("Your move: %s" % MOVES[your_move])

	if my_move == your_move:
		print("It's a draw... So you don't win... Goodbye!")
		exit()

	if wins_over(my_move, your_move):
		print("I WIN, GET LOST")
		exit()

	print("...")

print("That is not fair, you cheated!")
print("I'll get you this time, I'm guessing a number between 0 and a milion, which one is it?")
my_guess = random.randint(0, 10**6)
your_guess = int(raw_input('The magic number is: '))

if my_guess == your_guess:
	print(FLAG)
	print("NOW GET OUT")
else:
	print("Nope!, I guess you still have a lot to learn")
