#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import os


# In[78]:


csv_path = os.path.join('election_data.csv')

with open(csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    candidate_votes = {}
    total_votes= 0
    candidate_list=[]

    for row in csvreader:
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name]=1
         
            total_votes= total_votes +1
           
        else: 
            candidate_votes[candidate_name]=candidate_votes.get(candidate_name,0)+1
            total_votes = total_votes +1

    
    #print(total_votes)
    winner = max(candidate_votes, key=candidate_votes.get)
    #print(winner)
    print(candidate_votes)
    
  
    for candidate_name in candidate_votes:
        candidate_votes[candidate_name]=round(float(candidate_votes[candidate_name]/total_votes*100),2)
    print(candidate_votes)
    #sum(candidate_votes.values())
    
output = (
     "-------------------------\n"
    "Election Results\n"
     "-------------------------\n"
     f"Total Votes: {str(total_votes)}\n"
     "-------------------------\n")
print(output)
for x, y in candidate_votes.items():
    print(x+":", str(y)+"%")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# In[3]:


#Create a list that counts VoterID column
#Create a dictionary of Candidates and and then find count of candidates

#Candidates = {Candidate: row[2], Total_Votes: total_votes}

#print(total_votes)
    


# In[ ]:




