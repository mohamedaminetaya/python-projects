import platform

try:

    print("=== SYSTEM INFO ===")

    print("1 System")
    print("2 Version")
    print("3 Machine")
    print("4 Processor")
    print("5 All informations")

    choice = int(input("Enter option : "))

    if choice == 1:

        print("System :", platform.system())

    elif choice == 2:

        print("Version :", platform.version())

    elif choice == 3:

        print("Machine :", platform.machine())

    elif choice == 4:

        print("Processor :", platform.processor())

    elif choice == 5:

        print("System :", platform.system())
        print("Version :", platform.version())
        print("Machine :", platform.machine())
        print("Processor :", platform.processor())

    else:

        print("Program closed")

except ValueError:

    print("Enter numbers only")
