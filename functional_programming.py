from functools import reduce

# Higher-Order Function
def process_data(expenses, func):
  return list(map(func, expenses))

# Side-Effect Free Function
def get_total(expense):
  return expense['price']

# Closure
def make_category_filter(category):
  def category_filter(expense):
    return expense['category'] == category
  return category_filter

# Final Data Structure
expenses = [
    {'item': 'Coffee', 'price': 2.5, 'category': 'Food'},
    {'item': 'Shirt', 'price': 15, 'category': 'Clothing'},
    {'item': 'Book', 'price': 20, 'category': 'Education'},
]

# Functions as Parameters and Return Values
filter_food = make_category_filter('Food')
food_expenses = list(filter(filter_food, expenses))
food_total = reduce(lambda x, y: x + y, process_data(food_expenses, get_total))

print("Food Expenses Total: ", food_total)
