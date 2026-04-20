class Category:
    def __init__(self, name):
        self.name = name 
        self.ledger = []

    def deposit(self, amount, desc = ""):
        deposit = {'amount': amount, 'description': desc}
        self.ledger.append(deposit)

    def get_balance(self):
        current_balance = sum(item['amount'] for item in self.ledger)
        return current_balance

    def transfer(self, amount, other):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': - amount, 'description': f'Transfer to {other.name}'})
        other.ledger.append({'amount': amount, 'description': f'Transfer from {self.name}'})
        return True

    def withdraw(self, amount, desc = ""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({'amount': - amount, 'description': desc})
            return True

    def check_funds(self, amount):
        current_balance = self.get_balance()
        if amount > current_balance:
            return False
        else:
            return True

    def __str__(self):
        output = f"{self.name:*^30}\n"
        for item in self.ledger:
            desc = item['description'][:23]
            amt = item['amount']
            output += f"{desc:<23}{amt:>7.2f}\n"
        output += f"Total: {self.get_balance()}"
        return output 

food = Category('Food')
clothing = Category('Clothing')
food.deposit(100)
food.withdraw(10.51)
food.transfer(20, clothing)
clothing.withdraw(8.61)
print(food)

def create_spend_chart(categories):
    # 1. Calculate the total withdrawals across all categories
    total_spent = 0
    category_spent = []
    
    for cat in categories:
        # Sum only the negative amounts (withdrawals/transfers out)
        spent = sum(item['amount'] for item in cat.ledger if item['amount'] < 0)
        category_spent.append(abs(spent))
        total_spent += abs(spent)

    # 2. Calculate percentages rounded down to the nearest 10
    # We use // 10 * 10 to ensure 26% becomes 20%, satisfying requirement 19
    percentages = [int(((spent / total_spent) * 100) // 10 * 10) for spent in category_spent]

    # 3. Build the chart top-down (Y-axis and bars)
    chart = "Percentage spent by category\n"
    for n in range(100, -1, -10):
        # rjust(3) ensures '100', ' 90', and '  0' align perfectly
        chart += f"{str(n).rjust(3)}| "
        
        for pct in percentages:
            if pct >= n:
                chart += "o  " # 'o' plus two spaces for requirement 20
            else:
                chart += "   " # Three spaces to maintain alignment
        chart += "\n"

    # 4. Add the horizontal divider
    # Length is 3 spaces per category plus one extra dash
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 5. Build the vertical names (X-axis)
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "     " # Initial padding of 5 spaces
        for cat in categories:
            if i < len(cat.name):
                chart += f"{cat.name[i]}  " # Letter plus two spaces
            else:
                chart += "   " # Three spaces if the name is shorter than max_len
        
        # Add newline for all rows except the very last one
        if i < max_len - 1:
            chart += "\n"

    return chart

print(create_spend_chart([food, clothing]))
