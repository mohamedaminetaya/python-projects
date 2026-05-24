balance = 1000

try:

    while True:

        print("\n=== ATM System ===")

        print("1 afficher solde")
        print("2 déposer argent")
        print("3 retirer argent")
        print("4 quitter programme")

        choice = int(input("Tapez le nombre de operation : "))

        if choice == 1:

            print("Balance :", balance)

        elif choice == 2:

            deposer = int(input("Déposer argent : "))

            balance = balance + deposer

            print("New balance :", balance)

        elif choice == 3:

            retirer = int(input("Retirer argent : "))

            if retirer <= balance:

                balance = balance - retirer

                print("New balance :", balance)

            else:

                print("Insufficient balance")

       
        elif choice == 4:

            print("Program closed")

            break

        else:

            print("Invalid choice")

except:

    print("Tapez seulement des chiffres")
