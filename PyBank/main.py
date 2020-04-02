#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import os


# In[2]:


total_months = 0
net_total = 0
average_change = 0
net_change=[]
# have a greatest and least variable
greatest_increase = ['', -999999999999]
greatest_decrease = ['', 99999999999]

next_row = []


# In[3]:


budget_data = os.path.join('budget_data.csv')


# In[4]:


#define variables above the with open,otherwise all logic will be within the with open()
#row equals next as csvreader


# In[5]:


with open(budget_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    # Take the first DATA row and pre-populate some pieces
    next_row = next(csvreader) 
    total_months = total_months + 1
    net_total = net_total + int(next_row[1])
    prev_row = next_row
    
    for row in csvreader:
        total_months = total_months +1 
        net_total = net_total + int(row[1])
        #Find the delta between the current row and the previous row
        change = int(row[1]) - int(prev_row[1])
        #Add change to net_change[]
        net_change.append(change)
        
        #Iterate through data and compare change from current row to change from previous row
        if change > int(greatest_increase[1]):
            greatest_increase = [row[0], change]
        if change < int(greatest_decrease[1]):
            greatest_decrease = [row[0], change]
        #reset previous row to the current row so you can go through loop again    
        prev_row = row
        
    next_row = row
#create output my adding values together (must all be strings or use f-string)
output =(
    "Financial Analysis\n"
    "--------------------------\n"
    "Total Months: " + str(total_months) + "\n"
    "Total: $" + str(net_total) + "\n"
    "Average Change: $" +str(round((sum(net_change) / len(net_change)),2)) + "\n"
    f"Greatest Increase in Profits {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    


# In[6]:


#print output to reflect final solutions using \n to create new rows
print(output)


# In[ ]:





# In[ ]:





# In[ ]:




