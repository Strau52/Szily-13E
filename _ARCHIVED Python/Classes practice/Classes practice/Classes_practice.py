import random;
import math;

class Kor():
    __X = None; #Private
    __Y = None;
    __R = None;
    __Score = None;

    def __init__(self, r, x = random.randint(-50,50), y = random.randint(-50,50)): #Ctor
        self.__X = x;
        self.__Y = y;
        self.__R = r;
        self.__Score = 0;

    def InnerPoint(self, x, y): #Public
        return (abs(self.__X + self.__R) >= abs(x) and abs(self.__Y + self.__R) >= abs(y));

    #AB = d = sqrt(pow((pkp1-kkp1), 2) + pow((pkp-kkp2),2))
    def Distance(self, x, y):
        distance = round(math.sqrt(pow(x-self.__X, 2) + pow(y-self.__Y, 2)));
        if(self.InnerPoint(x,y)):
            self.__Score += abs((self.__R - distance)*10);
        return distance;

    def GetScore(self):
        return self.__Score;

#2. Készítsünk egy Kor példányt, kérjünk be a felhasználótól egy kör adatait majd kérjünk be pontokat és 
#mondjuk meg benne vannak e a körben.
#korX = (int(input("Adja meg a kör X koordinátáját: ")));
#korY = (int(input("Adja meg a kör Y koordinátáját: ")));
korR = (int(input("Adja meg a kör sugarát: ")));

#3. Készítsünk vagy módosítsuk a Kor kontrsuktort arra hogy, megadott sugárral de random középpontal hozza létre a Kört.
korVar = Kor(korR);
#korVar = Kor(korR, korX, korY);

for x in range(15):
    print(f"Próbálkozásaid száma: {x+1}");
    pontX = (int(input("Adja meg a pont X koordinátáját: ")));
    pontY = (int(input("Adja meg a pont Y koordinátáját: "))); 
    print(f"Benne van-e a körben a(z) [{pontX} , {pontY}] pont? Válasz: {korVar.InnerPoint(pontX, pontY)}");
    print(f"A távolság a kör középpontjától körülbelül: {korVar.Distance(pontX, pontY)}");
    print(f"Aktuális pontszámod: {korVar.GetScore()}");

print(f"A kör középpontja: {korVar._Kor__X , korVar._Kor__Y}");
print(f"Végső pontszámod: {korVar.GetScore()}");

#4. Módosítsa a Kör osztályt Céltábla osztállyá úgy, hogy legyen benne metódus, 
#amely egy adott pontnak a középponttól való távolsága szerint különböző pontszámokat ad! 
#Ezután készítsen céllövő játékot: hozzon létre egy véletlenszerű középpontú céltáblát, 
#majd kérjen be a felhasználótól 15 lövést (pontot), és számolja, hány pontnyi találata van a felhasználónak a 15 lövés után
#Minden lövés után segítségül közölje, mekkora volt a lövés távolsága a céltáblától.

