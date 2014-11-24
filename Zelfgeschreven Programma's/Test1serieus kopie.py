import math

print ('Welkom bij het eerste zelfgeschreven programma van Sjoerd!')
print ('*Applaus - Applaus*')
print ('Ok, laten we beginnen...')


original = input("Typ een woord van 5 letters: ")

empty_string = original.upper()
if len(empty_string) == 5 and empty_string.isalpha():
    print ("Je typte:", empty_string, "Fantastisch! Je hebt het goed gedaan.")
if len(empty_string) == 5 and not empty_string.isalpha():
	print ("Je typte:", empty_string, "Helaas! Je woord mag geen cijfers of non-alfabetische karakters bevatten!")
if len(empty_string) > 5: 
	print ("Je typte:", empty_string, "Helaas! Je woord bevat meer dan 5 letters!")
while len(empty_string) > 5: 
	if not empty_string.isalpha(): 
		print ("Ohja, en je woord bevat één of meer cijfers of non-alfabetische karakters, dat mag niet!")
		empty_string = "hello"
if len(empty_string) < 5: 
	print ("Je typte:", empty_string, "Helaas! Je woord bevat minder dan 5 letters!")
while len(empty_string) < 5: 
	if not empty_string.isalpha():
		print ("Ohja, en je woord bevat één of meer cijfers of non-alfabetische karakters, dat mag niet!")
		empty_string = "hello"
else:
    print ("Dat gaan we straks nog eens proberen!")
    print ("Nu eerst nog een oefening:")

original2 = input("Typ 'Spreek' ")
original3 = original2.lower()
original4 = original3[0]
original5 = original3[1]
original6 = original2[2:6]
original7 = original6 + original4 + original5

print ("Je typte:", original2) 
print ("Goedzo, nu pak ik de eerste 2 letters weg en plak deze erachter, let op:")
print (original7)

original8 = input("Welke letter moet worden verwijderd om opnieuw een geldig woord te vormen? ")

if original8 == "p": 
	print ("Wauw, wat ben jij slim! Je hebt gelijk, kijk maar:")
	print (original6 + original4)

print ("Typ nu een willekeurig woord, dan zal ik de eerste letter erachter plakken en er \'aland\' aan toevoegen")

original9 = input("Typ hier je woord: (een leuk voorbeeld is: 'splop') ")

original10 = original9[0]
original11 = original9[1:len(original9)]
original12 = 'aland'

print (original11 + original10 + original12)

original13 = input("Goedzo, probeer het anders nog eens met een ander woord, bijvoorbeeld je naam: ")

original14 = original13[0]
original15 = original13[1:len(original13)]
original16 = 'aland'

print (original15 + original14 + original16)

print ("Goedzo! Laten we nu eens kijken of we ook wat leuke rekensommen kunnen maken.")
print (" Stel je voor: je eet in een restaurant en je weet dat er op het totale bedrag 8 procent belasting en 15 procent fooi wordt gerekent.")


def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print ("Inclusief belasting betaal je nu: %.2f" % bill, "euro")
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print ("Wanneer je daar ook nog de fooi bij optelt kom je uit op: %.2f" % bill, "euro")
    return bill
    
meal_cost = float(input("Noem maar eens een bedrag tussen de 10 en 100: "))
print ('Je noemde een bedrag van', meal_cost, "laten we ervan uitgaan dat dit euro's zijn.")
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
print ('In totaal is er nu dus ongeveer', int(meal_with_tip) - int(meal_cost), 'euro aan kosten bijgekomen.')

print ('We leren steeds meer, eens zien of we ook het kwadraat van een getal kunnen berekenen.')

def square(n):
    """Returns the square of a number."""
    squared = n**2
    print ("%d in het kwadraat is %d." % (n, squared))
    return squared

square(int(input('Noem maar eens een getal. ')))

def power(base, exponent):  
    result = base**exponent
    print ("Lastig, maar volgens mij is %d tot de macht van %d toch echt: %d." % (base, exponent, result))

power(int(input('Of noem een willekeurig getal: ')), int(input('En vertel maar eens tegen welke macht dit moet worden afgezet: ')))

print ("Goedzo, we zijn bijna klaar, maar je mag nog even lekker iets schreeuwen! Ga maar los: ")  

def main():
    phrase = input()
    while not phrase.isupper():
        print("Nee, dat is geen schreeuwen! Probeer het nog eens! (Tip: gebruik hoofdletters!): ") 
        return main()
    print("Zo ja, dat is pas SCHREEUWEN! ;)") 

main()

print ("Goed, dat is er even uit. Tijd voor wat ingewikkelders: worteltrekken. Gelukig heb ik daarvoor een functie geïnporteert.")
print ('Laten we deze eens toepassen, noem maar eens een getal: ')

print ("Wat een mooi getal! De wortel daarvan is volgens mij: ", math.sqrt(int(input())))


