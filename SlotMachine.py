# Starting Date: 04.17.2024
# Completion Date:

# based on a youtube video in order to learn and familiarize myself with python syntax while also making a fun game

MAX_LINES = 3


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{str(MAX_LINES)})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number")
        else:
            print("Please enter a number")

    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()
