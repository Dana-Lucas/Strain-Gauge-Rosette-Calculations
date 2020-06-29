# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:15:11 2020

@author: Dana
"""
import numpy as np

# Data file containing strain measurements
# Strain gauge 1 @ 90*
# Strain gauge 2 @ 0*
# Strain gauge 4 @ 45*
# Strain gauge 5 @ 60*
f = open('close_end_data.txt')

dictionary45 = {}
dictionary60 = {}

for line in f:
    # split lines by tab, where each line denotes a single trial at pressure specified by first entry of the line
    s = line.split('\t')

    # skip the first line, showing what data/units are
    if s[0] == 'pressure (MN/m^2)':
        continue
    
    else:
        data45 = {}
        data60 = {}
        
    # This calculation is to find strain x, strain y and shear strain with the 45* strain rosette
        # using the strain equations from mechanics of materials, plug in 0*, 45*, 60* for angles
        c = np.array([ [(np.cos(0))**2,(np.sin(0))**2,np.sin(0)*np.cos(0)],
                        [(np.cos((np.pi)/4))**2,(np.sin((np.pi)/4))**2,np.sin((np.pi)/4)*np.cos((np.pi)/4)],
                        [(np.cos((np.pi)/2))**2,(np.sin((np.pi)/2))**2,np.sin((np.pi)/2)*np.cos((np.pi)/2)]  ])
        # plug in data at 0*, 45*, 90*, respectively
        d = np.array([float(s[1]),float(s[3]),float(s[2])])
        # Use numpy to solve the system of equations
        #   first entry is strain in the x direction, 
        #   second entry is strain in the y direction, 
        #   and third entry is shear strain
        y = np.linalg.solve(c,d)
        # Pull out and label each term
        data45['strain x'] = y[0]
        data45['strain y'] = y[1]
        data45['shear strain'] = '{:.2f}'.format(y[2])

        # Add these results to the dictionary, corresponding to its respective pressure
        dictionary45[s[0]] = data45
        
    # This calculation is to find the strain at 60*
        # using the same mechanics of materials equation set, plugging in knowns
        # Note: only two equations are needed because there are only two unknowns
        i = np.array([ [1,-np.sin((np.pi)/3)*np.cos((np.pi)/3)],
                       [0,-np.sin((np.pi)/2)*np.cos((np.pi)/2)] ])
        j = np.array([ (float(s[1])*(np.cos((np.pi)/3))**2+float(s[2])*(np.sin((np.pi)/3))**2),
                       (float(s[1])*(np.cos((np.pi)/2))**2+float(s[2])*(np.sin((np.pi)/2))**2-float(s[2])) ]) 
        k = np.linalg.solve(i,j)
        dictionary60[s[0]] = 'strain at 60*: {:.2f}'.format(k[0])
    
f.close()

# lists all the 45* strain rosette calculations
print(dictionary45)

print()

# lists strain at 60* for each pressure
print(dictionary60)