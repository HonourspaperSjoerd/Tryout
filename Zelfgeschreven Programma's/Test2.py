print (type(input('')))

print ('Nu eens zien of we het hoogste getal uit drie willekeurige getallen kunnen extraheren:')

maximum = max(int(input('Noem je eerste getal: ')), int(input('Noem je tweede getal: ')), int(input('Noem je derde getal: ')))

print ('Het hoogste getal uit de door jou ingevoerde reeks = ', maximum)

afstand_tot_nul = abs(maximum)

print ('En dan getal staat',afstand_tot_nul, 'posities van het getal \'nul\' af')

print ('Er bestaan trouwens drie soorten inputvariabelen in Python')

integer = (int(input('Noem maar eens een rond getal: ')))

def drijven2(drijven):
	drijven = (input('Noem maar eens een niet afgerond getal: '))
	if type(drijven) == int:
		print ('Dat is wel een afgerond getal, probeer het nog eens:')
		return drijven2()
	if type(drijven) == str:
		print ('Dat is geen getal, probeer het nog eens: ')
		return drijven2()
	else:
		float(drijven)

drijven2()

string = (str(input('Noem maar eens een woord: ')))

print ('Volgens Python heb je zojuist 3 verschillende types aan input geleverd.')

print ('Je eerste input wordt beoordeeld als: ', type(integer))
print ('Je tweede input wordt beoordeeld als: ', type(drijven2))
print ('Je laatste input wordt beoordeeld als: ', type(string))

print ('Je hebt dus zojuist een integer getal, een float getal en een string ingevoerd!')

def distance_from_zero(x):
    if type(x) == int or type(x) == float:
        return abs(x)
    else:
        return "Nope"

distance_from_zero(2)