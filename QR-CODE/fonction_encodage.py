# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

def convertisseur_dec_bin(nombre):
	if nombre == 0:
		resultat = 0
	resultat = ''
	else:
    	while nombre!=0:
        	quotient=nombre//2
        	reste=nombre%2
        	resultat += str(reste)
        	nombre=quotient
 
res = ''
for i in range(len(resultat)-1, -1, -1):
    res += resultat[i]

def encodage():
	liste = []
	listebin = []
	message = raw_input("Entrez le message à encoder: ")
	for caractere in message:
		var_temp = ord(caractere)
		print var_temp
		liste.append(var_temp)
		print liste


encodage()
put = input()