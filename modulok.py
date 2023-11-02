
#Kötelező rész: A csatolt feladatok közül válassz ki 5 feladatot: legyen benne számításos, elágazásos és ciklussal megoldható is. 

#Bosco líráért: 10 feladatot válaszz!

#Ötösért: Összes feladat

#Extra Bosco líráért: Ez a titkosítós feladat: https://etananyag.szamalk-szalezi.hu/mod/assign/view.php?id=16140

#Akik szeretik a kihívásokat: Extra Bosco líráért ezek is érdekesek és nehezek: https://etananyag.szamalk-szalezi.hu/mod/assign/view.php?id=16137


# 1. Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!   

def IntervallumKozotti():
	i = 0
	while i > 920 or i < 200:
		szam = int(input("Kérek egy [200, 920] intervallumban lévő egész számot: "))
		print("\nHibás, kérlek olvasd el újra!")
		i = szam
	print(f"\nA  {szam} első számjegye: {str(szam)[0]}")











#2.	Írj metódust, mely a paraméterében kapott számról megmondja, hogy hány 1-es, 10-es, 100 - as, 1000 - es, stb van benne! használd hozzá az egész osztás operátorát - // !  pl: 123//10 =12  123%10=3

def SzamSzamlalo(szam):
	i = 0
	while i==0:
		egyes = szam // 1
		tizes = szam // 10
		szazas = szam // 100
		ezres = szam // 1000
		i+=1
	print(f"\nA '{szam}'' számban:\n\n'{egyes}' db eggyes\n'{tizes}' db tízes\n'{szazas}' db százas\n'{ezres}' db ezres van")













#3.	Írj eljárást, mely paraméterében kap egy számot, majd összeadja a számjegyeket és kiírja a számjegyek összegét a képernyőre. PL. 324 -> „324 számjegyeinek összege: 9”

def SzamjegyOsszead(szam):
	i = 0
	osszeg = 0
	while i != len(str(szam)):
		szam_str = str(szam)
		osszeg += int(szam_str[i]) 
		i += 1
	print(f"\n{szam} számjegyeinek összege:",osszeg)










#4.	Egy hétfői napon az 1-es csoportnak 9 órája van. Az első órában a teljesítményük 90%-át képesek nyújtani. A 2-3. órában már kissé éhesek, és csupán 60%-os a munkabírásuk. A 4-7. órában szerencsére programozást tanulnak, így némiképp javul a hatékonyságuk (70%), a 8-9. órában azonban már újra lecsökken (50%).

#Írj metódust, mely paraméterében kap egy egész számot 1 és 9 között (melyik órán vannak; jelezz hibát, ha nem ebben az intervallumban lévő számot kapsz, pl. “Ez már tényleg túlzás.”). Példa egy esetre: Be: 3, Ki: “Még bírjuk (60%).”    -  nem kell tesztfüggvényeket írni, de az alábbi táblázat alapján ellenőrizzétek a munkátokat!

def Teljesitmeny(szam):

	if szam == 1:
		print("Még 90% on vagyunk!")
	elif szam == 2 or szam == 3:
		print("Még bírjuk (60%)")
	elif szam > 8 and szam < 3:
		print("Progit tanulunk, töltődünk! 70%")
	elif szam == 8 or szam == 9:
		print("Lassan nem bírjuk tovább! 50%")
	elif szam == 0:
		print("Be se jövök!")
	else:
		print("Ez már tényleg túlzás.")











#5.	Az egyik diák (legyen Márti a neve) az alábbi algoritmus alapján tevékenykedik az órákon:
#a.	hétfőn alszik az összes órán,
#b.	kedden csak hittan órán figyel,
#c.	programozás órán dolgozik, de csak szerdán
#d.	csütörtökön minden órán figyel, mert jó kedve van (aznap szokott moziba menni),
#e.	pénteken a hétvégéről ábrándozik, így csak félig figyel minden aznapi órán,
#f.	a többi óráról semmit nem tudunk.
#Írj metódsut, melynek  2 bemenő prarmétere van (nap neve, óra neve) és tájékoztatást ad Márti állapotáról. 

def MartiTeendok(nap,ora):

	if nap == 'h':
		print("alszik")
	elif nap == 'k':
		if ora == 'h':
			print("figyel")
		else:
			print("alszik")
	elif nap == 'sz':
		if ora == 'p':
			print("dolgozik")
		else:
			print("nincs info")
	elif nap == 'cs':
		print("figyel")
	elif nap == 'p':
		print("félig van jelen")
	else:
		print("Kérlek a megadott opciók közül válassz!")










#6.	A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!

def Negyzetgyok():
	szam = float(input("Kérek egy valós számot: "))
	if szam < 0:
		print("Hibaüzenet! Nem szabad negatív számból gyököt vonni!")
	else:
		gyok = szam ** 2
		print(f"A {szam} szám négyzetgyöke a {gyok}")











# 7.	A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!

def KeruletTerulet():
	a = float(input("Kérek egy valós számot: "))
	b = float(input("Kérek egy másik valós számot: "))
	if a <= 0 or b <= 0:
		print("Hiba: a téglalap oldalai nem pozitívak!")
	else:
		kerulet = round(2*(a+b),2)
		terulet = round(a*b,2)
		print(f"A téglalap kerülete: {kerulet}, területe: {terulet}")










# 1.feladat:	Egy a természettel  Vadászati és Természeti Világkiállításon téged bíztak meg, hogy egy kihelyezett információs tábla részműködését leprogramozd! 
#A felhasználónak be kell gépelnie melyik szektort szeretné megnézni, a te programod pedig kiírja az ott található kiállítás nevét.
#•	A esetén Nemzetközi Csarnok, World Conservation Forum 2021
#•	B és E esetén a Kereskedelmi Csarnok felirat jelenjen meg
#•	C esetén Konferencia-központ Innovációs Showroom
#•	D esetén Hal, Víz és Ember
#•	F esetén Hagyományos Vadászati Módok Csarnoka
#•	G Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás
#•	H esetben Központi Magyar Kiállítás
#•	Minden egyéb nem szám adatra írja ki, hogy forduljon a pénztárhoz.
#Pl1: 
#Be: Szektor: D
#Ki: Hal, Víz és Ember
#Pl2:
#Be: Szektor: 4
#Ki: HIBA: Adjon meg egy betűt A-H-ig!

def InformaciosTabla(szektor):

	if szektor.isalpha():
		if szektor == 'a':
			print("Nemzetközi Csarnok, World Conservation Forum 2021")
		elif szektor == 'b' or szektor == 'e':
			print("Kereskedelmi Csarnok")
		elif szektor == 'c':
			print("Konferencia-központ Innovációs Showroom")
		elif szektor == 'd':
			print("Hal, Víz és Ember")
		elif szektor == 'f':
			print("Hagyományos Vadászati Módok Csarnoka")
		elif szektor == 'g':
			print("Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás")
		elif szektor == 'h':
			print("Központi Magyar Kiállítás")
		else:
			print("forduljon a pénztárhoz")
	elif szektor.isdecimal():
		print("HIBA: Adjon meg egy betűt A-H-ig!")
	else:
		print("HIBA: Kérlek gondold át újra!")








# 8. Írj programot, ami kiírja a 10x10-es alapú szorzótáblát! 10-esével egymás alá! használj hozzá formázott kiiratást!

def SzorzoTabla():

	for y in range(1,11):
		for i in range(1,11):
			if i == 10:
				print(f"{y} x {i} =",y*i,"\n")
			else:
				print(f"{y} x {i} =",y*i)











# 9. Írj metódust, mely neveket kér a felhasználótól addig amíg a „@” jelet nem kapja. 
# Hány nevet adott meg a felhasználó? 
# Van-e benne A betűvel kezdődő név? 
# Melyik a leghosszabb név? 

def KukacJel():
	nev = ""
	lista_a = []
	nev_lista = []
	db = 0
	while nev != '@':
		nev = str(input("Kérek egy nevet: "))
		if nev[0] == 'a' or nev[0] == 'A':
			lista_a.append(nev)
		nev_lista.append(nev)
		db += 1 
	leghosszabb_nev = max(nev_lista,key=len)
	print(f"\n{db-1} db nevet adott meg a felhasználó\n'A' betűvel kezdődő nevek: {lista_a}\nLeghosszabb név: {leghosszabb_nev}")









# 10.	Írj metódust, mely egy érmedobás eredményét kéri be a felhasználótól 10-szer egymás után! A felhasználó minden lépésben a „f” vagy  „i” betűket kell megadjon. Addig kérd be a jeleket, amíg jó jelet nem ad meg. 
# Hányszor adott meg „f” betűt? 
# Mekkora a leghosszabb f sorozat? 

def Eremfeldobas():
	lista = []
	leg_h_f = 0


	while len(lista) != 10:
		eredmeny = str(input("\nFej - f\nÍrás - i\nMi lett az éremfeldobás eredménye? : "))
		while eredmeny != "f" and eredmeny != "i":
			eredmeny = input("Érvénytelen, Kérlek add meg újra: ")
		lista.append(eredmeny)
	f_lista = lista.count('f')


	for i in range(len(lista)):
		jelenlegi = lista[i]
		elozo = lista[i-1]
		if jelenlegi == 'f' and elozo == 'f':
			leg_h_f += 1
			print("most")
	if f_lista > 1:
		leg_h_f += 1
	if lista[0] == 'f' and lista[-1] == 'f':
		leg_h_f -= 1


	print(f"\n{f_lista}-szor adtunk meg 'f' betűt\nA leghosszabb 'f' sorozat: {leg_h_f}")













# 11.	++ Írj programot, mely beolvas egy pozitív egész számot, és megmondja, hogy tökéletes szám-e! (A tökéletes számok azok, melyek osztóinak összege egyenlő a szám kétszeresével. Ilyen szám pl. a 6, mert 2*6 = 1 + 2 + 3 + 6.) 
# Tökéletes számok: 6  28  496  8128  33550336

def TokeletesSzamE():
	i = 1
	szam = 0
	while i != szam:
		szam = int(input("Kérek egy pozitív egész számot: "))

		osztoi = 0
		y = 0
		while y != szam:
			y += 1
			if szam % y == 0:
				print("Osztható ezzel:",y)
				osztoi += y

		if 2*szam == osztoi:
			print(f"A {szam} egy tökéletes szám")
			i = szam










# 12.	++ Írj metódust, ami paraméterében kap két számot, és kiírja a két szám legnagyobb közös osztóját! Segítség::: A kisebbik számtól visszafelé nézzük, hogy van-e közös osztó. Nincs, ha az egyet elértük. 

def LegnagyobbKozos(szam1,szam2):
	kisebb = min(szam1,szam2)
	nagyobb = max(szam1,szam2) 


	lista = []
	while True:

		if (nagyobb / kisebb).is_integer():
			if kisebb == 1:
				break
			else:
				lista.append(nagyobb / kisebb)
				kisebb -= 1
		else:
			kisebb -= 1


		LKO = max(lista)

	print(f"A {szam1} és a {szam2} legnagyobb közös osztója a {LKO}")



















# 13.	++Írj metódust, ami paraméterében kap két számot, és kiírja a legkisebb közös többszörösüket! Segítség: Indulj a nagyobb számtól egyesével és keresd meg azt a számot, amelyet mindkettő oszt! Meddig kell mennie a ciklusnak? 

def LegkisebbKozos(szam1,szam2):
	kisebb = min(szam1,szam2)
	nagyobb = max(szam1,szam2) 

	lista_kisebb = []
	lista_nagyobb = []

	eredeti = nagyobb
	while True:

		if (nagyobb / kisebb).is_integer():
			LKKT = nagyobb
			print("LKKT:",LKKT)
			break
			
		else:
			print("nagyobb:",nagyobb) 
			nagyobb += eredeti


	print(f"A {szam1} és a {szam2} legkisebb közös többszöröse a {LKKT}")



















'''
i = 1
	while i != 'siker':
		lista_kisebb.append(kisebb*i)
		lista_nagyobb.append(nagyobb*i)

		for x in lista_nagyobb:
			for y in lista_kisebb:
				if x == y:
					LKKT = x
					i = 'siker'
				else:
					i += 1

'''













