def calculator():
    print("____Simple Calculator____")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit")
    while True:
        choice = input("Enter your choice(1-5):")
        if choice in ['1','2','3','4']:
            N1 = int(input("Enter first number:"))
            N2 = int(input("Enter second number:"))
            if choice == '1':
                print("sum of N1 and N2:",N1+N2)
            elif choice == '2':
                print("Differ of N1 and N2:",N1-N2)
            elif choice == '3':
                print("Product of N1 and N2:",N1*N2)
            elif choice == '4':
                print("Division of N1 and N2:",N1/N2)
        elif choice == '5':
            print("See you soon...")
        else:
            print("Invalid Choice")
calculator()
