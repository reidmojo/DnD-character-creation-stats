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

# simulate 100k dice rolls, storing each result in the list
for num in range(1,200000): 
    # define your stats min and max values here
    roll_a = random.randint(9,18) #str
    roll_b = random.randint(3,18) #dex
    roll_c = random.randint(3,18) #con
    roll_d = random.randint(3,18) #int
    roll_e = random.randint(3,18) #wis
    roll_f = random.randint(3,18) #cha

    roll_total = int(roll_a+roll_b+roll_c+roll_d+roll_e+roll_f)

    list.append(roll_total)
 
#create a new list of the disticnt roll totals, the number of occurrences, and the number of trials
list2 = [[i,list.count(i), len(list)] for i in set(list)] 

#create a data frame, because i need to practice pandas
df = pd.DataFrame(data = list2, columns = ['Roll', 'n','total'])
df['Probability'] = df['n']/df['total'] #this is the easy way to add a column
df['Cumulative Prob'] = 1-df['Probability'].cumsum() #add a cumulative total of the probability column


#allow the user to check multiple rolls
again = 'y'

while (again == 'y'):
    
    print 'please enter a value between %s and %s' % (df['Roll'].min(), df['Roll'].max()) 

    Roll = raw_input(int) #data type is important here, think it defaults to a string

    #use a while loop to make sure the input is within range
    while (int(Roll) < df['Roll'].min() or int(Roll) > df['Roll'].max()):
        print 'not in range, try again'
        Roll = raw_input(int)

    output = df['Cumulative Prob'][df['Roll']==int(Roll)]

    print 'there is a %s percent chance to roll a %s or higher' % (round(output.values*100,2), Roll)

    print 'would you like to roll again?'
    again = raw_input()    

    while (again != 'y' and again != 'n'):
        print 'please enter y or n'        
        again = raw_input()
