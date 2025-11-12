#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)
    if argc == 0:
        print("0 arguments.")
    else:
        s = "argument" if argc == 1 else "arguments"
        print("{} {}:".format(argc, s))
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
