#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------- #
# binary search
# ----------------------------------------------- #
# Author: Fabian Sarmiento
# Description: this works when you have to find an element in a order list
# first you find the middle of the list and compare, if its the same object,good, you find it
# otherwise if the element is minor than the middle value adjust the top of the list
# if the element is higher than the midle value adjust the bottom of the list

def binarySearch(element, myList):
    found = False
    bottom = 0
    top = len(myList)-1
    while bottom <= top and not found:
        middle = (bottom+top)//2 #this calculate the middle position of the list
        if myList(middle)==element:
        	found = True
    	elif myList(middle) < element:
    		bottom = middle+1
		elif myList(middle) > element:
    		top = middle-1
    return found


if __name__ == '__main__':
	my_list=[2,4,6,8,12,15,17,32,45,56,65,99]
	item = int(input('insert the number to find'))
	result = binarySearch(item,my_list)
	if result:
		print 'the number is in the list'
	else:
		print 'the number is not on the list'