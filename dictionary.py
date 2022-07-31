# This is my examples on using Dictionary

# Import all Add-ons 
import pandas as pd
import numpy as np

## EXAMPLE 1
basket_items = {'apples': 4, 'oranges':19, 'kites':3, 'sandwiches':8}
fruits = ['apples','oranges','pears','peaches','grapes']

# Create a local variable total 
# Specify value of "total" = 0
total = 0

# Iterate through basket_items
# For each iteration, check if index matches "fruits"
# If it matches, add the value into "total"
for index, value in basket.items():
  if index in fruits:
    total += value

print (total)
