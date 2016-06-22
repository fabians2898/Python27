#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------- #
# linear search
# ----------------------------------------------- #
# Author: Fabian Sarmiento
# Description: It is not really an algorithm, given a list of elements in any order
# element by element start to find a coincidence, thatś all.

def linearSearch(element, myList):
    found = False
    position = 0
    while position < len(myList):
        if myList[position]==element:
            found = True
        position += 1
    return found
