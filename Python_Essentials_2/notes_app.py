import os

try:

    while True:

        print("\n=== NOTES APP ===")

        print("1 Write notes")
        print("2 Read notes")
        print("3 Delete file")
        print("4 Exit")

        choice = int(input("Enter option : "))

        if choice == 1:

            note = input("Write your note : ")

            with open("note.txt", "a") as f:

                f.write(note + "\n")

            print("Note saved successfully")

        elif choice == 2:

            with open("note.txt", "r") as f:

                print("\n=== NOTES ===")
                print(f.read())

        elif choice == 3:

            os.remove("note.txt")

            print("File deleted successfully")

        elif choice == 4:

            print("Program closed")

            break

        else:

            print("Invalid choice")

except FileNotFoundError:

    print("File not found")

except ValueError:

    print("Enter numbers only")
