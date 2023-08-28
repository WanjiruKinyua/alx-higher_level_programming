#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print()
        return True
    except ValueError:
        return False


print(safe_print_integer(42))
print(safe_print_integer("hello"))
