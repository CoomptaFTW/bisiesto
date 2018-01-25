#coding: utf8
print ("Bisiesto o no")
anio1 = int(input("indique un año"))
if anio1%4==0 or anio1%100==0 or anio1%400==0:
	print "es bisiesto"
else:
	print "no es bisiesto"
