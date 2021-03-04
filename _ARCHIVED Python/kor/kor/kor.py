import math;
import random;

class Kor():

    __R = None;

    def __init__(self, r):
        self.__R = r;

    def Kerulet(self):
        return 2*math.pi*self.__R;

    def Terulet(self):
        return math.pi*math.pow(self.__R,2);

    def GetR(self):
        return self.__R;


Korok = [Kor(random.randint(0,21)), Kor(random.randint(0,21)),Kor(random.randint(0,21)), Kor(random.randint(0,21)),Kor(random.randint(0,21))];

for i in range(len(Korok)):
    print(f"A(z) {i+1}. Kör: Sugara: {Korok[i].GetR()}\r\n\tKerülete: {Korok[i].Kerulet()}\r\n\tTerülete: {Korok[i].Terulet()}");