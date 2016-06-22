#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------- #
# bubble sort
# ----------------------------------------------- #
# Author: Fabian Sarmiento
# Description: this is a sorting algorithm, you take the first element of the list
# and compare with the next value, if the first one is higher you swap the elements
# if you run all the list and you don't change any value, congratulations, 
# the list is already sorted.


def bubbleSort(myList):
    notSorted = True
    while notSorted:
        notSorted = False
        for index,element in enumerate(myList):
            try:
                if myList[index] > myList[index+1]:
                    notSorted = True
                    myList[index], myList[index+1] = myList[index+1], myList[index]
            except IndexError:
                pass
    return myList


if __name__ == '__main__':
    my_list=[32,45,1,5,76,23,86,12,52]
    result = bubbleSort(my_list)
    print result
