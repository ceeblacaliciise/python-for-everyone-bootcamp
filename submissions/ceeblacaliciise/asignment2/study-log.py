# ==================================================
# Name: hamdi ali
# Program: Study Log
# Description:
# This program allows the user to add, list,
# save, and load study notes using a text file.
# ==================================================


# ==================================================
# SECTION 1
# Comments, variables, print, and input
# ==================================================


# ==================================================
# SECTION 4 & 5
# Functions + File Handling + Error Handling
# ==================================================

def load_notes(path):
    """
    Load notes from a text file.
    If the file does not exist, return an empty list.
    """

    notes = []

    try:
        with open(path, "r", encoding="utf-8") as file:

            # SECTION 3
            # List + for loop
            for line in file:
                notes.append(line.strip())

    except FileNotFoundError:
        return []

    return notes


def save_notes(path, notes):
    """
    Save notes into a text file.
    Each note is written on its own line.
    """

    with open(path, "w", encoding="utf-8") as file:

        # SECTION 3
        # for loop to write all notes
        for note in notes:
            file.write(note + "\n")


# ==================================================
# SECTION 4
# main() function
# ==================================================

def main():

    # SECTION 1
    # Variable + input + print
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")

    # Load notes from file
    notes = load_notes("notes.txt")

    # Keep program running until user quits
    while True:

        # SECTION 2
        # Simple text menu using print
        print("\n===== STUDY LOG MENU =====")
        print("1) Add note")
        print("2) List notes")
        print("3) Quit")

        choice = input("Pick: ")

        # SECTION 2
        # if / elif / else menu
        if choice == "1":

            # SECTION 1
            # input + variable
            note = input("Note: ")

            # SECTION 3
            # Add note to list
            notes.append(note)

            print("Note added.")

        elif choice == "2":

            # SECTION 3
            # Print all notes using a for loop
            if len(notes) == 0:
                print("No notes found.")

            else:
                print("\nYour Notes:")

                for note in notes:
                    print(note)

        elif choice == "3":

            # Save notes before quitting
            save_notes("notes.txt", notes)

            print("Bye!")
            break

        else:
            print("Invalid choice. Try again.")


# ==================================================
# SECTION 4
# Run the program
# ==================================================

if __name__ == "__main__":
    main()
