#!/usr/bin/python3
# This program illustrates the chaotic function

def main():
    print("This program illustrates the chaotic function")
    # Test using 0.25
    x = eval(input("Enter a number between 0 and 1: "))
    for _ in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()