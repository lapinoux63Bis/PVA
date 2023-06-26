#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:50:32 2023

@author: gabriel
"""

import csv


with open("Rapport d'activité.txt", "w" ) as f :
    with open('registre_transmissions.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ";")
        for row in reader :
            if row[7] == "eth:ethertype:ip:tcp:smtp" :
                f.write("Envoie d'un email à ")
                f.write(row[0] + "\n")
             
            elif row[7] == "eth:ethertype:ip:tcp:tls" :
                f.write("Connexion internet à l'adresse : ")
                f.write(row[2] + "\n")
                
                
                

