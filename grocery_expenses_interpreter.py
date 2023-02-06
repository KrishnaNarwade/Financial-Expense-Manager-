class GroceryExpenseInterpreter:
    def __init__(self, file_path):
        self.data = []
        self._parse(file_path)

    def _parse(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]

            for line in lines:
                if 'item:' in line:
                    item = line.split(':')[1].strip()
                elif 'price:' in line:
                    price = float(line.split(':')[1].strip())
                    self.data.append({'item': item, 'price': price})

    def total(self):
        return sum([x['price'] for x in self.data])
    def item(self):
        return [x['item'] for x in self.data]
    def ind_cost(self):
        return [x['price'] for x in self.data]

expense = GroceryExpenseInterpreter('grocery_expenses.dsl')
print(f"You have Spent: € {round(expense.total())} in total\nYou have purchased these following items: {expense.item()}\nYour highest purchase amount is {max(expense.ind_cost())}")
