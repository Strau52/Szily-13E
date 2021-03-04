#Feltöltés
import random;

meresek = [];

for i in range(20):
    meresek.append(random.randint(1,100));
for meres in meresek:
    print(meres, end=' ');

#1. Volt e a repülés során olyan szakasz, amikor sík terep volt haladtunk?
print("\r\nElső feladat:");
i = 0;
while ((i < (len(meresek)-1)) and (meresek[i] != meresek[i+1])):
       i+=1;
van = i < (len(meresek)-1);
if(van):
    print("Volt sík terep!");
else:
    print("Nem volt sík terep!");
#2. Hány olyan 100 méteres szakasz volt, amikor csökkent a magasság?
print("\r\nMásodik feladat:");
db = 0;
for i in range((len(meresek)-1)):
    if(meresek[i] > meresek[i+1]):
        db+=1;
print(db, "db esetben csökkent a magasság.")
#3. Mekkora volt a teljes repülés alatt mért szintemelkedés? (Plusz pontért szintcsökkenést is meg lehet határozni)
print("\r\nHarmadik feladat:");
max = -1; min = 200;
for i in range(len(meresek)):
    if(meresek[i] < min):
        min = meresek[i];
    if(meresek[i] > max):
        max = meresek[i];
print("A teljes szintemelkedes:", max-min, "m volt.");
#4. Hányszor 100 méteres volt az a leghosszabb szakasz, ahol folyamatosan emelkedőn haladtunk?
print("\r\nNegyedik feladat:");
emelkedesDb = ideigDb = 0;
for i in range((len(meresek)-1)):
    if(meresek[i] < meresek[i+1]):
        ideigDb+=1;
    else:
        if(ideigDb > emelkedesDb):
            emelkedesDb = ideigDb;
        ideigDb = 0;
print((emelkedesDb*100),"m volt a leghosszabb szakasz ahol folyamatosan emelkedtünk.");
#5. Mekkora volt a 100 méter alatt megtett legnagyobb szintemelkedés?
print("\r\nÖtödik feladat:");
maximum = -1;
for i in range((len(meresek)-1)):
    kulonbs = meresek[i+1]-meresek[i];
    if(kulonbs > maximum):
        maximum = kulonbs;
print("100 méter alatt a legnagyobb szintemelkedés:",maximum,"m volt.");