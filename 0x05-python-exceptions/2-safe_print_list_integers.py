#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
printed_count = 0

  try:
      for element in my_list[:x]:
          try:
              print("{:d}".format(int(element)), end='')
              printed_count += 1
          except ValueError:
              pass
          except IndexError:
              pass
          print()
          return printed_count
