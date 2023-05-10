#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:50:32 2023

@author: gabriel
"""

import csv


with open("Rapport d'activité.txt", "w" ) as f :
    with open('registre_transmissions.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader :
            if ''.join([row[0][18], row[0][19], row[0][20]]) == "587" :
                f.write("Envoie d'un email à \n")
                f.write("".join([row[0][0], row[0][1], row[0][2], row[0][3], row[0][4], row[0][5], row[0][6], row[0][7], row[0][8], row[0][9], row[0][10], row[0][11], row[0][12], row[0][13], row[0][14], row[0][15], row[0][16], row[0][17]]))
            
            elif ''.join([row[0][18], row[0][19], row[0][20], row[0][21]]) == "8080" : 
                f.write("Connexion internet à l'adresse : \n")
                f.write("".join([row[0][50], row[0][51], row[0][52], row[0][53], row[0][54], row[0][55], row[0][56], row[0][57], row[0][58], row[0][59], row[0][60]]))
                
                
                

