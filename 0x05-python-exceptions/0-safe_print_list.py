#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_count = 0
    try:
        iterator = iter(my_list)
        while printed_count < x:
            print(next(iterator), end=' ')
            printed_count += 1
    except StopIteration:
        pass
    print()
    return printed_count
