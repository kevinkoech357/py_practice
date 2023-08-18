#!/usr/bin/python3
# This program illustrates the chaotic function

def main():  # sourcery skip: use-fstring-for-formatting
    print("This program illustrates the chaotic function")
    # Test using 0.25
    x = eval(input("Enter a number between 0 and 1: "))
    # Test using 0.26 to see the difference
    y = eval(input("Enter a number between 0 and 1: "))
    print()
    formula = "3.9 * x * (1 - x)"
    print(f'formula = {formula}')
    print(f'x \t y')
    for _ in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * x * (1 - x)
        print(f"{x:.2f} \t {y:.2f}")
    print()

main()
