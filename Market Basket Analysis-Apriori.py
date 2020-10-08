# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:22:34 2020

@author: Vikee
"""


# Grocery Market Basket Data

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori


store_data = pd.read_csv('store_data.csv',header=None)
a=store_data.shape

# convert pandas df to list of list


records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])
    
    
    
    
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)

b=print(len(association_results)) # Each item corresponds to one rule.

print(association_results[0]) # we see that light cream and chicken are commonly bought together


# The support value for the first rule is 0.0045. This number is calculated by dividing the number of transactions containing light cream divided by total number of transactions. The confidence level for the rule is 0.2905 which shows that out of all the transactions that contain light cream, 29.05% of the transactions also contain chicken. Finally, the lift of 4.84 tells us that chicken is 4.84 times more likely to be bought by the customers who buy light cream compared to the default likelihood of the sale of chicken.




for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
    
    