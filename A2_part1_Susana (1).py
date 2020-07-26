#!/usr/bin/env python
# coding: utf-8

# In[103]:


# SUSANA'S CONTRIBUTION PART 1: Q6 to Q10
# =======================================
# Import necessary modules
import numpy as np
import pandas as pd
import re

# read the csv file into Dataframe: df, and check data is read ok
df = pd.read_csv('data_assignment.csv')
print("The Dataset consists of: ", df.shape[0], " rows and ", df.shape[1], " columuns")
df.head(5)  


# In[116]:


# Choose job sector, how many sub-sectors are there in that sector? 
# I tried using Unique function, but couldn't make it work:  np.unique(sector, trim='fb')[source]

# Chose the Accounting Sector, create new dataset
sub_classification = df[df['Classification'] == "Accounting" ].groupby(['Classification','SubClassification'])
sub_classification['Classification'].value_counts()
print('There are',len(sub_classification), 'sub sectors within Accounting')


# In[118]:


# List the names of each sub-sector and it's job posting total
print('Sub Sectors and total job posting numbers:')
df[df['Classification'] == "Accounting" ]['SubClassification'].value_counts()


# In[77]:


# List the salary ranges and their total of job openings

# List the job types, what are the lowest and highest salary?


# In[119]:


# The salaries are set as HighestSalary and LowestSalary, calculate AverageSalary for each job.
df = df.assign(AverageSalary= (df["LowestSalary"] + df["HighestSalary"])/2 )

