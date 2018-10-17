#! /usr/bin/env python

def NumerosR(n):
	if n!=101:
		print(n)
		return NumerosR(n+1)
NumerosR(1)