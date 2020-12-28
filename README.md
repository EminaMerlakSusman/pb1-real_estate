# pb1-real_estate
Projekt pri predmetu Podatkovne baze 1 - baza nepremičnin v nepremičninski agenciji

Za projekt sem naredila bazo nepremičnin v nepremičninski agenciji. Vsaka nepremičnina ima id, naslov oglasa, regijo, tip posredovanja (prodaja/oddaja), vrsto nepremičnine (hiša/stanovanje/posest/vikend), število sob in ceno. Regija, tip posredovanja in vrsta nepremičnine so tuji ključi, podatke o njih pa sem v bazo dodala na začetku in naj se ne bi spreminjali. Spletni vmesnik omogoča filtriranje nepremičnin na isti način kot na nepremičninskih straneh (cena od-do, velikost, regija, tip posredovanja, vrsta nepremičnine). Ob kliku na gumb ob posamezni nepremičnini se ta lahko izbriše iz baze, lahko pa se tudi dodaja novo nepremičnino. Za delovanje je potreben django, bootstrap in crispy-forms (priloženo v mapi requirements.txt)

Diagram baze, narejen v programu Dia:
![Alt text](https://github.com/EminaMerlakSusman/pb1-real_estate/blob/master/real_estate.png?raw=true "Database diagram")

Projekt vsebuje naslednje datoteke:
<h1>Direktorij real_estate:</h1>
<ul>
  <li>mapa real_estate, kjer se nahaja projekt</li>
  <li>diagram baze, real_estate.png</li>
  <li>mapa templates, ki vsebuje html predloge za generiranje strani</li>
  <li>datoteka requirements.txt, ki vsebuje pakete, ki jih je potrebno naložiti za delovanje projekta.</li>

</ul>

<h1>Direktorij real_estate/real_estate:</h1>
<ul>
  <li>sale_type.csv, regions.csv, listing_types.csv so podatki o vrsti prodaje (oddaja/najem), regijah (seznam slovenskih regij), in vrstah nepremičnin (hiša/stanovanje/posest/vikend). Ti podatki se vnesejo v bazo samo na začetku, in se kasneje ne spreminjajo.</li>
  <li>populate_db.py: python program za gengeriranje naključnih nepremičnin, ki jih nato zapiše v datoteko listings_random.csv. Nekatere parametre, kot so npr. kvadratura in cena, generira smiselno glede na vrsto nepremičnine in tip posredovanja.</li>
  <li>add_to_db.py: program, ki prebere zgornje csv datoteke in jih doda v bazo.</li>
  <li>models.py: datoteka s tabelami baze</li>
  <li>views.py: funkcije, ki se izvajajo na spletnem vmesniku.</li>

</ul>
