import random

maxlines = 3
maxgamble = 100
mingamble = 1

ROWS = 3
COLS = 3

symbol_count = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8
}
symbol_value = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2
}


def check_winning(columns, lines, gamble, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[0]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*gamble
            winning_lines.append(line+1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")

            else:
                print(column[row], end="")
        print()


def deposit():

    while True:
        amount = input("The amount that you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_no_of_lines():

    while True:
        lines = input("Enter the no. of lines (1-"+str(maxlines)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 < lines <= maxlines:
                break
            else:
                print("Enter a valid no. of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_gamble():
    while True:
        amount = input("The amount that you want to gamble: $")
        if amount.isdigit():
            amount = int(amount)
            if mingamble <= amount <= maxgamble:
                break
            else:
                print(f"Amount must be between ${mingamble} - ${maxgamble}.")
        else:
            print("Please enter a number.")
    return amount


def spin(balance):
    lines = get_no_of_lines()

    while True:
        gamble = get_gamble()
        total_gamble = gamble * lines
        if total_gamble > balance:
            print(f"Not enough amount: ${balance}")
        else:
            break
    print(f"You are gambling ${gamble} on ${lines} lines.Total gamble is equal to: ${total_gamble}")
    print(balance, lines)
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, gamble, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_gamble


def main():

    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spinner = input("Enter to spin (q to quit).")
        if spinner == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
