#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    x = int(input("x: "))
    y = int(input("y: "))
    
    # swaping
    # first step
    x ^= y
    # second step
    y ^= x
    # last step
    x ^= y

    print(f'x is {x}')
    print(f'y is {y}')

main()

