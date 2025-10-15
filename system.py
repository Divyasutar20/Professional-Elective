from datetime import datetime

class Expense:
    def __init__(self, amount, description, date_str):
        self.amount = amount
        self.description = description.lower()
        self.date = datetime.strptime(date_str, "%Y-%m-%d")
        self.category = None

class ExpenseExpertSystem:
    def __init__(self):
        self.rules = [
            (["coffee", "cafe", "restaurant", "food", "drink"], "Food & Drinks"),
            (["bus", "taxi", "uber", "train", "transport"], "Transport"),
            (["movie", "concert", "game", "entertainment"], "Entertainment"),
            (["supermarket", "grocery", "market"], "Groceries"),
            (["rent", "mortgage", "apartment"], "Housing"),
            (["electricity", "water", "internet", "utility"], "Utilities"),
        ]
        self.expenses = []

    def categorize(self, expense):
        for keywords, category in self.rules:
            if any(keyword in expense.description for keyword in keywords):
                expense.category = category
                return
        expense.category = "Other"

    def add_expense(self, amount, description, date_str):
        expense = Expense(amount, description, date_str)
        self.categorize(expense)
        self.expenses.append(expense)

    def summarize(self):
        summary = {}
        for expense in self.expenses:
            summary[expense.category] = summary.get(expense.category, 0) + expense.amount
        return summary

    def check_budget(self, budgets):
        summary = self.summarize()
        alerts = []
        for category, limit in budgets.items():
            spent = summary.get(category, 0)
            if spent > limit:
                alerts.append(f"⚠️ Over budget in '{category}': spent ${spent:.2f}, limit ${limit:.2f}")
        return alerts

    def print_summary(self):
        summary = self.summarize()
        print("\nExpense Summary by Category:")
        for category, amount in summary.items():
            print(f"- {category}: ${amount:.2f}")

    def print_alerts(self, budgets):
        alerts = self.check_budget(budgets)
        if alerts:
            print("\nBudget Alerts:")
            for alert in alerts:
                print(alert)
        else:
            print("\nAll expenses are within the budget limits.")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

def get_budgets():
    print("\nSet your monthly budgets for categories (press Enter to use default):")
    default_budgets = {
        "Food & Drinks": 100,
        "Groceries": 150,
        "Transport": 50,
        "Entertainment": 60,
        "Housing": 1200,
        "Utilities": 100
    }
    budgets = {}
    for category, default in default_budgets.items():
        while True:
            val = input(f"- {category} (default ${default}): ").strip()
            if val == "":
                budgets[category] = default
                break
            try:
                amount = float(val)
                if amount < 0:
                    print("Please enter a positive number or leave blank for default.")
                else:
                    budgets[category] = amount
                    break
            except ValueError:
                print("Invalid number. Please try again.")
    return budgets

def main():
    print("Welcome to the Expert System Expense Tracker!")

    tracker = ExpenseExpertSystem()

    if get_yes_no("Do you want to set custom budgets? (y/n): "):
        budgets = get_budgets()
    else:
        budgets = {
            "Food & Drinks": 100,
            "Groceries": 150,
            "Transport": 50,
            "Entertainment": 60,
            "Housing": 1200,
            "Utilities": 100
        }
        print("Using default budgets.")

    print("\nEnter your expenses:")

    while True:
        amount = get_float("Enter expense amount ($): ")
        description = input("Enter expense description: ").strip()
        date_str = get_date("Enter expense date (YYYY-MM-DD): ")

        tracker.add_expense(amount, description, date_str)
        print("Expense added.\n")

        if not get_yes_no("Add another expense? (y/n): "):
            break

    tracker.print_summary()
    tracker.print_alerts(budgets)

    print("\nThank you for using Expense Tracker!")

if __name__ == "__main__":
    main()
