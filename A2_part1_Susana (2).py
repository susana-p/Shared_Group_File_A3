#!/usr/bin/env python
# coding: utf-8

# In[135]:


# SUSANA'S CONTRIBUTION PART 1: Q6 to Q10
# =======================================
# Import necessary modules
import numpy as np
import pandas as pd
import re

# read the csv file into Dataframe: df, and check data is read ok
df = pd.read_csv('data_assignment.csv')
print("The Dataset consists of: ", df.shape[0], " rows and ", df.shape[1], " columuns")
df.head(3)  


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


# In[156]:


#List the salary ranges and their total of job postings
#grouping the salary ranges then calculating their totals   *****????? still need to fix this
salary_range = df["LowestSalary"] + df["HighestSalary"]
salary_range
#group = df.groupby('LowestSalary')
#group.count()


# In[188]:


#Q1.8 List the job types, what are the lowest and highest salary?  ***???? lowest and highest
#job_type = df['JobType'].df.sort_values()
job_type = df['JobType'].value_counts()
job_type


# In[184]:


# Q2.1 The salaries are set as HighestSalary and LowestSalary, calc AverageSalary for each job. ****????

from math import *
#df = df.assign(AverageSalary= df["LowestSalary"] + df["HighestSalary"]/2)
df_low = df['LowestSalary'].mean()
df_high = df['HighestSalary'].mean()
df_low, df_high

