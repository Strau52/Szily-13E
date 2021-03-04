import random;
import string;

class ZH():
    __Neptun = None;
    __Score = None;
    __Name = None;

    def __init__(self, name):
        self.__Name = name;
        self.__Score = random.randint(0,100);
        self.__Neptun = self.__NeptunGenerate();

    def __NeptunGenerate(self):
        neptun = random.choice(string.ascii_uppercase);
        for i in range(5):
            chance = random.randint(1,100);
            if(chance <= 40):
                neptun += str(random.randint(0,9));
            else:
                neptun += random.choice(string.ascii_uppercase);
        return neptun;

    def GetNeptun(self):
        return self.__Neptun;

    def GetScore(self):
        return self.__Score;

    def GetName(self):
        return self.__Name;


Exams = [ZH("János"), ZH("János1"), ZH("János2"), ZH("János3"), ZH("János4"), ZH("János5"), ZH("János6"), ZH("János7")];
print("::ELSŐ FELADAT::")
for i in range(len(Exams)):
    if(Exams[i].GetScore() >= 51):
        print(f"{Exams[i].GetName()} Átment!")
    else:
        print(f"{Exams[i].GetName()} Megbukott!")

print("::MÁSODIK FELADAT::")
max = 0;
for i in range(1,len(Exams)):
    if(Exams[i].GetScore() > Exams[max].GetScore()):
        max = i;
print(f"A legjobb eredményű hallgató neptunkódja: {Exams[max].GetNeptun()}");
#print("A legjobb eredményű hallgató neptunkódja: ",{Exams[max].GetNeptun()});

print("::HARMADIK FELADAT::")
Ponthatarok = [50,60,80,90,100];

for i in range(len(Exams)):
    j = 0;
    while(j <= len(Ponthatarok) and Exams[i].GetScore() > Ponthatarok[j]):
        j += 1;
    print(f"{Exams[i].GetName()} [{Exams[i].GetNeptun()}] - {j+1} [{Exams[i].GetScore()}]");


#Név - Jegy
#91 - 100 pont --> 5
#81 - 90 pont --> 4
#61 - 80 pont --> 3
#51 - 60 pont --> 2
#0 - 50 pont --> 1






#Do while/hátultesztelős ciklus
#i = 0;
#while(i <= 0 and FELTÉTEL):
#    i += 1;


#Allat osztály, ami tárolja magáról, hogy milyen állat, milyen étrenddel rendelkezik, éhes-e, mozgása, életben van-e
#Legyen olyan metódusa, hogy Mozgas(), ha az állat nem éhes, akkor éhes lesz ha mozgott, ha már éhes akkor meghal.
#Legyen egy Etetes() metódus, ha éhes akkor már nem lesz az.
#A húsevőknek legyen egy Vadasz() metódusa, ami mozgással jár és 45% az esélye hogy sikeres. Ha sikeres akkor eszik, ha nem akkor csak mozgott.
#A megfelelő adattagoknak csinálj Get metódust!
#FELADATOK:
#1. Csinálj egy szafari tömböt és töltsd fel 10 állattal.
#2. A szafariban lévő húsevő állatok induljanak vadászatra, a mindenevők mozogjanak és a növényevők pedig a túristáktól kapnak kaját.
#3. Írjuk ki az állatok állapotát (éhesek-e, élnek-e)
#4. A szafariban lévő állatok mozogjanak! Ezután egyenek és vadásszanak. Írjuk ki a halott állatok adatait!
#5. Írjuk ki az életben maradt állatok adatit.