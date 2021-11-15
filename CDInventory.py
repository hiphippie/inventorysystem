#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:06:19 2021

@author: andreagorder
"""

#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AndreaGorder, 2021-Nov-10 , Corrected spelling 
#------------------------------------------#

# Declare variables

strChoice = '' # User input 
lstRow = {}  # Dictionary of data row 
lstTbl = []  # Empty table to hold data 
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
#print(-------------------------)
print('The Magic CD Inventory\n')
#print(-------------------------)
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
         objFile = open(strFileName, 'r')
         for row in objFile: 
             print(row)
         objFile.close()
        # TODO Add the functionality of loading existing data
        #pass
        
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        # Updating rows to be dictionaries over lists - A: Added {} rather than []. May require the addition of values?
        lstRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(lstRow)
        print(lstRow) 
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        for row in lstTbl:
            print('ID', 'Title', 'Artist')
            print(*row.values(), sep = ', ')
            print()
            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry A: Adding code below THIS DOESNT WORK YET
        rowRemoval = input('Enter an ID for Deletion: ')
        rowRemInt = int(rowRemoval)
        for row in lstTbl:
            if rowRemInt == row['ID']: #this tells us which element to look in, so here is the id, which is in the column 0
                lstTbl.remove(lstRow)
                print('line74') 
            else:
                print('Not Found')
                
    elif strChoice == 's':
         objFile = open(strFileName, 'a')
         for row in lstTbl:
            strlst = str(lstRow)
         objFile.write(strlst)
         objFile.close()
    print('Please choose either l, a, i, d, s or x!')

