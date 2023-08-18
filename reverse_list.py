#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    list1 = [2, 3, 4, 5, 6, 7, 87, 99, 43, 23, 56, 77]

    print("Unsorted list: ")
    print(list1)

    # sort() is strictly a list method
    # sort doesnt return a new list
    list1.sort(reverse=True)

    print("Sorted list:")
    print(list1)

    # sort doesnt return a new list
    list2 = list1.sort(reverse=True)

    print("Sort() doest return a new list")
    print(list2)

if __name__ == '__main__':
    main()
