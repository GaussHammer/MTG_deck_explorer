import csv
import sys
from search import *
def main():
    document = sys.argv[1]
    running = True
    while running:
        user_input = input("What are you looking for? (type \"help\" for a list of commands) ")
        match(user_input):
            case "search":
                search(document)
            case "help":
                multiline_str = ("search - begin a new search\n"
                                 "help - this menu\n"
                                 "quit - exit the application")
                print(multiline_str)

            case "quit":
                running = False




main()