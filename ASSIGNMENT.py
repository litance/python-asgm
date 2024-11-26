import datetime
import os
import tkinter as tk
from tkinter import messagebox

MAX = 100
NOTES_ID = 0  # Define first notes id
NOTES_ARY = [""] * MAX  # Define notes array
NOTES_TITLE_ARY = [""] * MAX  # Define notes title function array

def display_welcome():
    print("Welcome to Notes Organizer")
    print()
    display_menu()  # Display menu here

def display_menu():
    print("COMMAND MENU")
    print("add   -  ADD  NOTE")
    print("view  -  VIEW NOTE")
    print("edit  -  EDIT NOTE")
    print("del   -  DELETE NOTE")
    print("cls   - !CLEAR ALL NOTE!")
    print("exit  -  EXIT PROGRAM")
    print()

def add_function():
    def add_display():
        print("ADD FUNCTION")
        print("1  -  ADD")
        print("2  -  RETURN")
        choose = input("PLEASE ENTER YOUR CHOOSE[1/2]:")
        if choose == "1":
            add_notes()
        elif choose == "2":
            clear()
            main()
        else:
            clear()
            print("NOT AVAILABLE INPUT")
            main()

    def add_notes():
        global NOTES_ID  # Allow NOTES_ID can be appended
        if NOTES_ID < MAX:  # If notes quantity didn't reach maximum = 100
            title = input("Please enter your notes title:\n")  # Notes title
            NOTES_TITLE_ARY[NOTES_ID] = title
            notes = input("Please enter your notes:\n")  # Notes
            NOTES_ARY[NOTES_ID] = notes
            NOTES_ID += 1
            clear()
            print("NOTES ADD SUCCESSFUL")
            add_display()
        else:
            clear()
            print("NOTES QUANTITY REACH LIMIT(100)")
            add_display()

    add_display()

def view_function():
    global NOTES_ID
    print("VIEW FUNCTION  -  NOTE LIST")
    print("ID NOTE-TITLE")
    for i in range(NOTES_ID):
        print(f"{i} {""} {NOTES_TITLE_ARY[i]}")

    print("\nCHOOSE:")
    print("1  -  VIEW NOTE")
    print("2  -  RETURN")
    view_choose = input("PLEASE ENTER YOUR CHOOSE[1/2]:")
    if view_choose == "1":
        view_notes()
    elif view_choose == "2":
        clear()
        main()
    else:
        clear()
        print("NOT AVAILABLE INPUT")
        view_function()

def view_notes():
    global NOTES_ID
    if 0 > NOTES_ID + 1:
        print("NO NOTES CURRENTLY FOUND")
    else:
        ID_INPUT = input("ENTER NOTE ID: ")
        print("NOTES:")
        print(NOTES_ARY[int(ID_INPUT)])
        print("\nCHOOSE:")
        print("1  -  RETURN TO VIEW NOTE")
        print("2  -  RETURN TO MAIN MENU")
        notes_choose = input("PLEASE ENTER YOUR CHOOSE[1/2]:")
        if notes_choose == "1":
            view_function()
        elif notes_choose == "2":
            clear()
            main()
        else:
            clear()
            print("NOT AVAILABLE INPUT")
            main()

def edit_function():
    print("EDIT FUNCTION")

def delete_function():
    global NOTES_ID
    print("DELETE FUNCTION")
    print("NOTES LIST:")
    print("ID NOTE-TITLE")
    for i in range(NOTES_ID):
        print(f"{i} {""} {NOTES_TITLE_ARY[i]}") #Print out the note list
    delete_choose = input("PLEASE INPUT THE NOTE ID:")
    NOTES_ARY.pop(int(delete_choose))
    NOTES_TITLE_ARY.pop(int(delete_choose))

    for i in range(int(delete_choose), int(NOTES_ID - 1)):
        NOTES_ARY[i + 1] = NOTES_ARY[i]

    NOTES_ID -= 1

def clear_function():
    conform_choose = input("!!!-- DID YOU CONFORM TO CLEAR DATA? --!!! (YES/NO): ").upper()
    if conform_choose == "YES":
        NOTES_ARY.clear()
        NOTES_TITLE_ARY.clear()
        clear()
        main()
    elif conform_choose == "NO":
        clear()
        main()
    else:
        print("WRONG INPUT")
        clear()
        main()

def exit_function():
    exit()  # Quit() in Jupyter Notebook, Exit() in .py / Stop() to stop cell input running

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    display_welcome()
    while True:
        command = input("Command: ").lower()  # User input command
        if command == "add":
            add_function()

        elif command == "view":
            view_function()

        elif command == "edit":
            edit_function()

        elif command == "del":
            delete_function()

        elif command == "cls":
            clear_function()

        elif command == "exit":
            exit_function()

        else:
            print("WRONG COMMAND!")
            clear()


main()
