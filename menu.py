import os


# Prints the menu and tells you which file is loaded (if any)
def show_menu(filename):
    print()
    print("=" * 40)
    print("TEXT ANALYSER")
    print("=" * 40)
    print("1. Load text file")
    print("2. Display basic statistics")
    print("3. Export results")
    print("4. Exit")
    print("=" * 40)

    if filename == "":
        print("No file loaded")
    else:
        print("Current file:", filename)


# Looks in this folder and grabs all the .txt files in a sorted list
def find_text_files():
    text_files = []

    for name in os.listdir("."):
        if name.endswith(".txt"):
            text_files.append(name)

    text_files.sort()
    return text_files


# Shows the .txt files and lets you pick one by number or by typing its name
def choose_file():
    text_files = find_text_files()

    if len(text_files) == 0:
        print("There are no .txt files in this folder.")
        return ""

    print("\n--- File Selection ---")
    print("Available text files:")
    number = 1
    for name in text_files:
        print(f"  {number}. {name}")
        number += 1

    choice = input("Enter filename or number: ").strip()

    if choice.isdigit():
        index = int(choice) - 1
        if index >= 0 and index < len(text_files):
            return text_files[index]
        else:
            print("That number is not in the list.")
            return ""

    if os.path.isfile(choice):
        return choice

    print("File not found:", choice)
    return ""
