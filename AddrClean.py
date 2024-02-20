#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:45:35 2020

@author: mak
"""


import csv
l=[]
with open('DataClean.csv', 'r',errors="ignore") as file:
    reader = csv.reader(file)
    for row in reader:
        if(row):
            l.append(row)
            
m=[]
with open('countries.csv', 'r',errors="ignore") as file:
    reader = csv.reader(file)
    for row in reader:
        if(row):
            m.append(row)
            
n=[]
with open('cities.csv', 'r',errors="ignore") as file:
    reader = csv.reader(file)
    for row in reader:
        if(row):
            n.append(row)
            
o=[]
with open('States.csv', 'r',errors="ignore") as file:
    reader = csv.reader(file)
    for row in reader:
        if(row):
            o.append(row)
            

#---------------------------------------------------
            
#---------------------------------------------------
            
#---------------------------------------------------
            

count = 0
lstCheck = []
for j in l:
    
    flag = True
    for i in m:
        con = i[0]
        try:
            j[0].index(con)
            count += 1
            flag = False
            break
        except:
            temp = ''
    if flag == True:
        con = 'not found'
        
    flag = True
    for i in n:
        city = i[0]
        try:
            j[0].index(city)
            count += 1
            flag = False
            break
        except:
            temp = ''
    if flag == True:
        city = 'not found'
    
    
    flag = True
    for i in o:
        state = i[1]
        try:
            j[0].index(state)
            count += 1
            flag = False
            break
        except:
            temp = ''
    if flag == True:
        state = 'not found'
    
    
    lstCheck.append([j[0],con,city,state])

for i in lstCheck:
    with open('updatedAddresses.csv','a',newline='',errors='ignore') as fd:
            wr = csv.writer(fd, dialect='excel')
            wr.writerow(i)