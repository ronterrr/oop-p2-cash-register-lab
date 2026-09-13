#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    # discount
    self.discount = discount

    # total
    self.total = 0

    # items
    self.items = []

    # previous_transactions
    self.previous_transactions = []


  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    if not isinstance(value, int) or value < 0 or value > 100:
      print("Not valid discount")
      self._discount = 0
    else:
      self._discount = value


  def add_item(self, item, price, quantity=1):
    self.total += price * quantity

    for i in range(quantity):
      self.items.append(item)
      
    temp_object = {'item': item, 'price': price, 'quantity' : quantity}
    self.previous_transactions.append(temp_object)

  def apply_discount(self):
    if not self.previous_transactions:
      print("There is no discount to apply")
      return

    discount_amount = self.total * (self.discount / 100)
    self.total -= discount_amount

  def void_last_transaction(self):
    if not self.previous_transactions:
      print("There are no transactions to void.")
      return

    last_transaction = self.previous_transactions.pop()

    item_cost = last_transaction['price'] * last_transaction['quantity']
    self.total -= item_cost

    if last_transaction['item'] in self.items:
      self.items.remove(last_transaction['item'])