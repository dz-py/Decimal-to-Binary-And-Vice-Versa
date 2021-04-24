condition = True
while condition:
    choice = input("Would you like to convert decimal to binary (1) or binary to decimal (2)?: ")

    # Decimal to Binary
    if choice == "1":
        decimal = int(input("Input your decimal: "))
        list = [decimal]
        while decimal > 1:
            decimal //= 2
            list.append(decimal)
        binary = []
        for element in list:
            if element % 2 == 0:
                binary.append(str(0))
            else:
                binary.append(str(1))
        bin = "".join(binary[::-1])
        print(f"Binary: {bin}")
        # Shortcut using bin() function:
        # print(bin(decimal))

    # Binary to Decimal
    elif choice == "2":
        binary = int(input("Input your binary: "))
        decimal, i = 0, 0
        while binary != 0:
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1
        print(f"Decimal: {decimal}")
        # Shortcut using int() function:
        # print(int(str(binary), 2))

    else:
        print("Please enter either 1 or 2")
        continue

    # Convert again
    while condition:
        reenter = input("Enter yes to convert again or no to stop: ").lower()
        if reenter == "yes":
            break
        elif reenter == "no":
            condition = False
        else:
            print("Please enter yes or no")

    if reenter == "yes":
        continue
    elif reenter == "no":
        break
