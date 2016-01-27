# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:04:47 2016

@author: rjohnson26

Purpose: Generate the probabilities of rolling a particular stat roll total
         while creating a character in Baldur's Gate (or any D&D game using 
         that rule set)
         
Approach: Simulate a large number of dice rolls, get the probabilities from that.

"""

import random
import pandas as pd

list = [] # need to create an empty list

for num in range(1,100000): 
    # define your stats min and max values here
    roll_a = random.randint(10,18) #str
    roll_b = random.randint(14,18) #dex
    roll_c = random.randint(6,18) #con
    roll_d = random.randint(4,18) #int
    roll_e = random.randint(3,18) #wis
    roll_f = random.randint(15,18) #cha

    roll_total = int(roll_a+roll_b+roll_c+roll_d+roll_e+roll_f)

    list.append(roll_total)
    
list2 = [[i,list.count(i), len(list)] for i in set(list)]

df = pd.DataFrame(data = list2, columns = ['Roll', 'n','total'])
df['Probability'] = df['n']/df['total']
df['Cumulative Prob'] = df['Probability'].cumsum()

print 'please enter a value between %s and %s' % (df4['Roll'].min(), df4['Roll'].max()) 

Roll = raw_input(int)

while (int(Roll) < df['Roll'].min() or int(Roll) > df['Roll'].max()):
    print 'not in range, try again'
    Roll = raw_input(int)

output = df['Cumulative Prob'][df['Roll']==int(Roll)]

print 'there is a %s percent chance to roll a %s or higher' % (100-round(output.values*100,2), Roll)

#print 'there is a %s chance of rolling a %s' % (output, Roll)
