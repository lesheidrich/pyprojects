def yiir(yr):
    if yr % 4 == 0 and yr % 100 == 0 and yr % 400 == 0:
        print(f"{yr} is a leap year!")
    elif yr % 4 == 0 and yr % 100 == 0:
        print(f"{yr} is not")
    elif yr % 4 == 0:
        print(f"{yr} is a leap year!")
    else:
        print(f"{yr} is not...")

while True:
    print("Welcome to the leap year app\n")
    query_type = int(input("Press:\n - 1 to check a single year \n - 2 to check a range of years\n>> "))
    if query_type == 1:
        inp_a = int(input("Enter year to check\n>> "))
        yiir(inp_a)
    elif query_type == 2:
        beg_yr_rng = int(input("Enter range start year\n>> "))
        en_yr_rng = int(input("Enter range end year\n>> ")) + 1
        for inp_b in range(beg_yr_rng, en_yr_rng):
            yiir(inp_b)
    else:
        print("You entered an invalid value.")
    play_again = input("Press 'q' to exit. Press any key to play again.\n>> ").lower()
    if play_again == "q":
        print("\n")
        print("Thank you for playing. Goodbye.")
        break
    else:
        print("\n")


