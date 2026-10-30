"""
Expense Tracker v1.1: 
- A simple command-line programme that records how much money is spent at each place or category, 
- and prints a total for each one. 

How it works:
1. Enter a place/category (e.g. "eat out") and the amount spent. 
2. Repeat as many times as you like; amounts for the same category are added together (input is case-insensitive and ignores leading/trailing spaces)
3. Invalid amounts are rejected and you're asked for the amount again (no need to re-enter the place). 
4. Press Ctrl-D to finish. 

Output:
- Each category with its total in euros, sorted from highest to lowest. 
- The total of all spending. 

Usage: python3 expenses.py

"""

def main():
    bill_dic = {}

    while True:
        try:
            place = input("Place or Category: ").strip().lower()
            money = get_money()
            if place in bill_dic:
                bill_dic[place] = bill_dic[place] + money
            else:
                bill_dic[place] = money
            print()
        except EOFError: 
            print("\n")
            break

    print("---------- Summary ----------")

    for place, money in sorted(bill_dic.items(), key=lambda item: item[1], reverse=True):
        print(f"{place}: €{money:.2f}")

    print("-" * 29)
    print(f"Total: €{sum(bill_dic.values()):.2f}")


def get_money():
    while True:
        try: 
            amount = float(input("Money Spent: ")) 
            if not amount > 0:
                raise ValueError
            return amount 
        except ValueError:
            print("Please enter a positive number.")

    
if __name__ == "__main__":
    main()