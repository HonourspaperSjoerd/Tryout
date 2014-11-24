print ('Welcome to the Pig Latin Translator!')

original = input("Typ een woord van 5 letters:")

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

original9 = input("Typ hier je woord \(een leuk voorbeeld is \'splop\') ")

original10 = original9[0]
original11 = original9[1:len(original9)]
original12 = 'aland'

print (original11 + original10 + original12)

original13 = input("Goedzo, probeer het anders nog eens met een ander woord, bijvoorbeeld je naam: ")

original14 = original13[0]
original15 = original13[1:len(original9)]
original16 = 'aland'

print (original15 + original14 + original16)
