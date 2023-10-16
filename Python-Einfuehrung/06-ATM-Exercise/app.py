print("1. Einzahlen"
      " 2. Auszahlen"
      " 3. Kontostand"
      " 4. Beenden")

isFinished = False
kontostand = 0

while not isFinished:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print('Einzahlen')
        amount = float(input("Enter the amount to deposit: "))  # Use float to allow decimal values
        kontostand += amount
        print('Sie haben', amount, 'eingezahlt. Ihr neuer Kontostand beträgt', kontostand)
    elif choice == 2:
        print('Auszahlen')
        amount = float(input("Enter the amount to withdraw: "))
        if amount > kontostand:
            print('Nicht genügend Geld auf dem Konto.')
        else:
            kontostand -= amount
            print('Sie haben', amount, 'abgehoben. Ihr neuer Kontostand beträgt', kontostand)
    elif choice == 3:
        print('Kontostand:', kontostand)
    elif choice == 4:
        isFinished = True
    else:
        print('Ungültige Eingabe. Bitte wählen Sie eine der verfügbaren Optionen (1-4).')

print('Das Programm wurde beendet.')