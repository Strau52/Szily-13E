import random; 
import math;

class Rectangle():
    __A = None;
    __B = None;

    def __init__(self):
        self.__A = random.randint(1,10);
        self.__B = random.randint(1,10);

    def Disctrict(self):
        return 2 * (self.__A + self.__B);

    def Area(self):
        return self.__A * self.__B;

    def GetA(self):
        return self.__A;

    def GetB(self):
        return self.__B;

Rectangles =[Rectangle(),Rectangle(),Rectangle(),Rectangle(),Rectangle(),Rectangle(),Rectangle(),Rectangle(),Rectangle(),Rectangle()]

for i in range(len(Rectangles)):
    print(f"A(z) {i+1}. téglalap Disctrict: {Rectangles[i].Disctrict()} Area: {Rectangles[i].Area()}")

for i in range(len(Rectangles)):
    if(Rectangles[i].GetA() == Rectangles[i].GetB()):
        print(f"Négyzet található a(z) {i}. indexen!!")

#math.sqrt(szam); szam Négyzetgyöke
#math.pow(szam, hatvanykitevo); (alap^kitevo)
#math.pi();