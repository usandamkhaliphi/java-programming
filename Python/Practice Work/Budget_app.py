class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:.2f}"
            output += f"{desc:23}{amt:>7}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    spendings = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spendings.append(spent)
    
    total_spent = sum(spendings)

    percentages = [
        int((spent / total_spent) * 100) // 10 * 10 if total_spent > 0 else 0
        for spent in spendings
    ]

    chart = "Percentage spent by category\n"
    
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for pct in percentages:
            chart += "o  " if pct >= level else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"    
    
    max_len = max(len(cat.name) for cat in categories)
    padded_names = [cat.name.ljust(max_len) for cat in categories]

    for i in range(max_len):
        chart += "     "
        for name in padded_names:
            chart += f"{name[i]}  "
        if i < max_len - 1:
            chart += "\n"
    
    return chart
