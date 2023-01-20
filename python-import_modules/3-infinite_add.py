#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    add = 0
    BOO = len(sys.argv)

    for i in range(1, BOO):
        add += int(sys.argv[i])
    print("{}".format(add))
