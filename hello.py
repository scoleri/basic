#!/usr/bin/python2.4

import sys

def Hello(name):
	if name == 'Alice' or name == 'Nick':
		name = name + '????'
	else:
		print 'Else'
	name=name+'!!!!!'
	print "Hello",name

def main():
	Hello(sys.argv[1])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()

