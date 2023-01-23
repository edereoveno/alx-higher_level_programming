#!/usr/bin/python3

def uppercase(str):
	for character in str:
		if ord(character) in range(97, 123):
			print("{}".format(chr(ord(character) - 32)), end="")
		else:
			print("{}".format(character), end="")
