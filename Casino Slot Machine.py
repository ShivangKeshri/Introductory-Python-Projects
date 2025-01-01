rt random

max_lines = 3
max_bet = 100
min_bet = 1

rows = 3
cols = 3

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
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,winning_lines

def slot_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns): # transposing a matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1 :
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): # tells us if amount is a valid whole number.
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(max_lines) + ")? ")
        if lines.isdigit(): # tells us if amount is a valid whole number.
            lines = int(lines) # if the input is some digit, then this converts it to an integer.
            if 1 <= lines <= max_lines:
                break
            else:
                print("enter a valid number of lines.")
        else:
            print("please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): # tells us if amount is a valid whole number.
            amount = int(amount)
            if min_bet <= amount <= max_bet :
                break
            else:
                print(f"Amount must be between ${min_bet} - ${max_bet}.")
        else:
            print("please enter a number.")
    return amount
# want to play again : then I just call the main function.

def main():
    balance = deposit()
    lines= get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"you do not have enough to bet, your current balance is ${balance}")
        else:
            print("Bet successful")
            break
    print(f"you are betting ${bet} on {lines} lines. Total Bet = ${total_bet}")

    slots = slot_spin(rows,cols,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on lines:", *winning_lines)
main()
