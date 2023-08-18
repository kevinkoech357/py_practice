#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    from collections import Counter

    list1 = ["Kev", "Eve", "Steve", "Adam", "Kev", "Eve", "Kev", "KEV"]
    #using Counter
    print("Using counter method")
    count_kev = Counter(list1).get("Kev")
    print(f'Kev appears {count_kev} times')

    # using for loop
    print("Using for loop")
    count = 0
    for content in list1:
        if content == "Kev":
            count += 1
    print(f'Kev appears {count} times')

main()
