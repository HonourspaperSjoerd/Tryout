from decimal import Decimal

print ('Dit is een programma om vakantiekosten te berekenen.')

# def vakantie_kosten(kosten_kamer, aantal_nachten, afstand_van_huis, vervoersmiddel, verbruik_auto, benzine_kosten_per_liter):
bestemming = input('Waar wil je naar toe op vakantie? ')
kosten_kamer = int(input('Wat zijn de reserveringskosten (in euro\'s) per nacht van de beoogde verblijfplaats? '))
aantal_nachten = int(input('Hoeveel nachten wil je gaan? '))
vervoersmiddel = (input('Wil je met de auto of met het vliegtuig? ')) 
dagbesteding = int(input('Hoeveel euro wil je per persoon, per dag, uitgeven? '))
aantal_personen = int(input('Met hoeveel personen ga je op reis? '))
kosten_dagbesteding = Decimal(dagbesteding) * Decimal(aantal_personen) * Decimal(aantal_nachten)
if not 'auto' or 'vliegtuig' in vervoersmiddel:
	print ('Zo te zien wil je niet met de auto of het vliegtuig, dan is dit programma helaas niet geschikt.')
if 'auto' in vervoersmiddel:
	afstand_van_huis = int(input('Hoeveel km ligt de verblijfplaats van huis af? '))
	verbruik_auto = int(input('Hoeveel km rijdt de auto gemiddeld op 1 liter benzine? '))
	benzine_kosten_per_liter = (input('Hoeveel euro betaal je voor 1 liter benzine? '))
	print ('Ok, dus je wilt op vakantie naar', bestemming, 'met', aantal_personen, 'personen, voor', aantal_nachten, 'nachten.', 'Je gaat met een auto die 1 op', verbruik_auto, 'rijdt.')
	prijs_kamer = (kosten_kamer * aantal_nachten) 
	print ('De kosten van je kamer komen uit op', prijs_kamer, 'euro.')
	aantal_liter = afstand_van_huis / verbruik_auto
	aantal_liter2 = '{0:.2f}'.format(aantal_liter)
	print ('Op de opgegeven afstand van', afstand_van_huis, 'km, vebruikt je auto', aantal_liter2, 'liter benzine.')
	benzine_kosten_totaal = Decimal(aantal_liter) * Decimal(benzine_kosten_per_liter)
	benzine_kosten_totaal2 = '{0:.2f}'.format(benzine_kosten_totaal)
	benzine_kosten_totaal3 = Decimal(benzine_kosten_totaal2) * 2
	print ('De kosten hiervan, bij een rourtrip, zijn:', benzine_kosten_totaal3, 'euro.')
	prijs_reis = benzine_kosten_totaal3
	totale_kosten = prijs_kamer + prijs_reis + kosten_dagbesteding
	overzicht = '{0:.2f}'.format(totale_kosten)
	totale_kosten_pp = totale_kosten / aantal_personen
	overzicht2 = '{0:.2f}'.format(totale_kosten_pp)

vakantiekosten = [bestemming, kosten_kamer, aantal_nachten, vervoersmiddel, dagbesteding, aantal_personen, kosten_dagbesteding, afstand_van_huis, verbruik_auto, benzine_kosten_per_liter, prijs_kamer, aantal_liter, aantal_liter2, benzine_kosten_totaal, benzine_kosten_totaal2, benzine_kosten_totaal3, prijs_reis, totale_kosten, overzicht, overzicht2, totale_kosten_pp]

print ('De geschatte leefkosten terplekke bedragen', vakantiekosten[6], 'euro.')
print ('De totale kosten van deze reis komen uit op,', vakantiekosten[18], 'euro.')
print ('Of', vakantiekosten[19], 'euro per persoon.')

if 'vliegtuig' in vervoersmiddel:
	ticketprijs = ('Check www.skyscanner.nl en vul hier de prijs van de meest voordelige vlucht in: ', int(input('')))
	print ('Ok, dus je wilt op vakantie naar', bestemming, 'voor', aantal_nachten, 'nachten.', 'Je gaat met het vliegtuig waarbij het ticket', ticketprijs, 'kost.')
	prijs2 = (kosten_kamer*aantal_nachten) + (ticketprijs)
	print ('De totale kosten van deze reis komen uit op,', prijs2)

print ('Laten we meteen ook even je koffer inpakken.')

suitcase = []  

suitcase.append(input(str('Noem maar eens een kledingstuk: ')))

def koffer_inpakken():
	antwoord = input('Wil je nog meer kledingstukken meenemen? (ja of nee): ')
	if 'ja' in antwoord:
		nieuw_item = suitcase.append(input(str('Ok, welk kledingstuk wil je nog meer meenemen? ')))
		print (suitcase[-1], 'is op de lijst geplaatst. ')
		return koffer_inpakken()
	if 'nee' in antwoord:
		list_length = len(suitcase)
		print ("Ok, er zitten nu %d kledingstukken in je koffer." % (list_length))
		print ('Dit zijn: ', suitcase)
	else:
		print ('Je moet met ja of nee antwoorden. ')
		return koffer_inpakken

koffer_inpakken()

# print ('wil je nog iets toevoegen?')

dubbel_check = input('Of wil je nog een kleidingstuk omruilen? ')
if 'ja' in dubbel_check:
	omruil_item1 = str(input('Welk kledingstuk wil je omruilen? '))
	omruil_item = suitcase.index(omruil_item1)
	nieuw_item2 = str(input('En welk kledingstuk komt ervoor in de plaats? '))
	nieuwe_lijst = suitcase.insert(omruil_item, nieuw_item2)
	print ('Ok, je neemt nu dus mee: ', suitcase)


