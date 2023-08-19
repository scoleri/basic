#!/usr/bin/python2.4

import sys

def Hello(name):
	"""
	This function takes a name as input and prints a greeting message with the name.
	If the name is 'Alice' or 'Nick', it adds '????' to the name before printing the message.
	If the name is anything else, it adds '!!!!!' to the name before printing the message.
	"""
	if name == 'Alice' or name == 'Nick':
		name = name + '????'
	else:
		print 'Else'
	name=name+'!!!!!'
	print "Hello",name

def main():
	"""
	This function calls the Hello function with the first command line argument passed to the script.
	"""
	Hello(sys.argv[1])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()
