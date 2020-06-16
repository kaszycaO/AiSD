#!/usr/bin/python3

import sys

from priority_queue import PriorityQueue

def get_input():
    args = sys.stdin.readlines()
    args = [arg.split() for arg in args]
    try:
        args[0][0] = int(args[0][0])
    except ValueError:
        pass


    return args

def main():
    args = get_input()
    if len(args) - 1 == int(args[0][0]):
        queue = PriorityQueue()
        for command in (args[1:]):
            if command[0] == "insert":
                if len(command) == 3:
                    queue.insert(command[1], int(command[2]))
                else:
                    print("Insert failure!")
            elif command[0] == "empty":
                print("Empty: ", queue.empty())
            elif command[0] == "top":
                print("Top: ", queue.top())
            elif command[0] == "pop":
                print("Pop: ", queue.pop())
            elif command[0] == "priority":
                if len(command) == 3:
                    queue.priority(command[1], int(command[2]))
                else:
                    print("Priority failure!")
            elif command[0] == "print":
                queue.my_print()
            else:
                print("Invalid command: ", command)

    else:
        print("Incorrect input!")


if __name__ == "__main__":
    main()
