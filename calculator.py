while True:
    print("CALCULATOR MENU")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5):")

    if choice == "1":
        a = float(input("Enter First number:"))
        b = float(input("Enter second number:"))
        print("Result:", a + b)
    
    elif choice == "2":
        a = float(input("Enter First number:"))
        b = float(input("Enter second number:"))
        print("Result:", a - b)
    
    elif choice == "3":
        a = float(input("Enter First number:"))
        b = float(input("Enter second number:"))
        print("Result:", a * b)

    elif choice == "4":
        a = float(input("Enter First number:"))
        b = float(input("Enter second number:"))
        if b == 0:
            print("Error! Division by zero.")
        else:
            print("Result:", a / b)


    
    elif choice == "5":
        print("Exiting Calculator...Bye! ")
        break

    else:
        print("Invalid choice! Please select between 1-5.")