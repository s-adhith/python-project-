from menu import show_menu, choose_file
from text_processing import analyse_file
from visualisation import print_statistics, show_charts
from report_export import export_results

# Runs the menu loop and keeps asking what you wanna do until you pick 4


def main():
    print("Welcome to the Text Analyser!")

    filename = ""
    stats = {}
    choice = ""

    while choice != "4":
        show_menu(filename)
        choice = input("Enter your choice (1-4): ").strip()

        # Option 1: load file
        if choice == "1":
            new_file = choose_file()
            if new_file != "":
                print(f'Analysing "{new_file}"...')
                try:
                    stats = analyse_file(new_file)
                    filename = new_file
                    print(f"Done! Processed {stats['lines']:} lines.")
                except OSError:
                    print("Could not read the file.")

        # Option 2:statistics
        elif choice == "2":
            if filename == "":
                print("No file loaded. Please load a file first.")
            else:
                print_statistics(filename, stats)
                show_charts(filename, stats)
                input("\nPress Enter to continue...")

        # Option 3: report export
        elif choice == "3":
            if filename == "":
                print("No file loaded. Please load a file first.")
            else:
                try:
                    export_results(filename, stats)
                except OSError:
                    print("Could not save the results.")

        # Option 4: quit
        elif choice == "4":
            print("Thank you for using Text Analyser!")

        else:
            print("Please enter a number from 1 to 4.")


main()
