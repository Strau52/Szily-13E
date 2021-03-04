#Harmadik feladat
import math;
import random;

class Triangle:
    __A = None;
    __B = None;
    __C = None;

    def GetA(self):
        return self.__A;

    def GetB(self):
        return self.__B;

    def GetC(self):
        return self.__C;

    def District(self):
        return self.__A + self.__B + self.__C;

    def Area(self):
        s = self.District() /2;
        return math.sqrt(s*(s-self.__A)*(s-self.__B)*(s-self.__C));

    def __Editable(self):
        return (self.__A + self.__B > self.__C) and (self.__A + self.__C > self.__B) and (self.__B + self.__C > self.__A);

    def __init__(self):
            self.__A = random.randint(0, 101);
            self.__B = random.randint(0, 101);
            self.__C = random.randint(0, 101);
            while not (self.__Editable):
               self.__A = random.randint(0, 101);
               self.__B = random.randint(0, 101);
               self.__C = random.randint(0, 101);
    

Triangles = [Triangle(),Triangle(),Triangle()];

array_length = len(Triangles);
for i in range(array_length):
            print(f"A: {Triangles[i].GetA()}\n\rB: {Triangles[i].GetB()}\n\rC: {Triangles[i].GetC()}\r\nDistrict: {Triangles[i].District()}\n\rArea:{Triangles[i].Area()}\r\n\r\n")
print("::END::");  


#Második feladat
#def interval(a,b):
#    sum = 0;
#    for i in range(a+1,b):
#        sum += i;
#    return sum;

#print(interval(1,5))


#Összetett progtételek

#lineáris keresés
def LinKeres(x):
    i = 0;
    while((i < len(x)) and x[i] % 2 != 0):
        i+= 1;
    van = (i < len(x))

    if(van):
        idx = i;
        return idx;
    else:
        return van;

#másolás, kiválogatás, szétválogatás, metszet, unió
