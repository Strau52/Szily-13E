##Soroztaszámítás
#szamok = [3,7,2,3,6,10];
#osszeg = 0;

#for i in range(len(szamok)):
#    osszeg += szamok[i];

#print(("Sorozatszámítás tétele:").upper());
#print("Feladat: Adjuk össze a tömb elemeit és írjuk ki ezeknek összegét.");
#print("A tömbben lévő számok összege: ", osszeg, end='\n\n');

##Eldöntés
#szamok = [3,7,2,3,5,9];
#szamok = [3,7,1,3,5,9];
#i = 0;

#while ((i < len(szamok)) and (szamok[i] % 2 != 0)):
#    i+=1;

#van = (i < len(szamok));
#print(("Eldöntés tétele:").upper());
#print("Feladat: Döntsük el van e páros szám a tömben.");
#print("Van e páros szám a tömbben: ", van, end='\n\n');

##Kiválasztás
#szamok = [3,5,9,2,5,8];
#i = 0;
#idx = -1;

#while(szamok[i] % 2 != 0):
#    i+=1;

#idx = i;

#print(("Kiválasztás tétele:").upper());
#print("Feladat: Válasszuk ki az első páros számot a tömbben és mondjuk meg melyik szám az és melyik indexen van.");
#if (idx >= 0):
#    print("Az első páros szám a(z) ", szamok[idx] ,"indexe a tömbben: ", idx, end='\n\n');
#else:
#    print("A tömbben nincs páros szám!", end='\n\n');

##Megszámlálás
#szamok = [3,5,9,2,5,8];
#db = 0;

#for i in range(len(szamok)):
#    if(szamok[i] % 2 == 0):
#        db+=1;

#print(("Megszámlálás tétele:").upper());
#print("Feladat: Számoljuk meg hány páros szám van a tömbben.");
#print("A tömbben: ", db, "db páros szám van.", end='\n\n');

##Maximumkiválasztás
#szamok = [1,20,2,2,1,1,5,9];
#max = 0;
#i = 1;

#for i in range(len(szamok)):
#    if(szamok[i] > szamok[max]):
#        max = i;

#print(("Maximumkiválasztás tétele:").upper());
#print("Feladat: Válasszuk ki a legnagyobb számot a tömbben és mondjuk meg melyik indexen van.");
#print("A tömb legnagyobb eleme: ", szamok[max], " és ez a(z) ", max,". indexen van.", end='\n\n');

