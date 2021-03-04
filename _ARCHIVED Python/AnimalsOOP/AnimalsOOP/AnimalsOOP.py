import random;

class Animals():
    __Animal = None;
    __Diet = None;
    __Hungry = None;
    __Alive = None;

    def __init__(self, animal, diet):
        self.__Animal = animal;
        self.__Diet = diet;
        self.__Hungry = False;
        self.__Alive = True;

    def Moving(self):
        if(self.__Hungry == False):
            self.__Hungry = True;
        else:
            self.__Alive = False;

    def Feeding(self):
        if(self.__Hungry == True):
            self.__Hungry = False;

    def Hunting(self):
        if(self.__Diet == "Carnivorous"):
            succes = random.randint(1,100);
            if(succes <= 45):
                self.__Hungry = False;
            else:
                self.Moving();

    def GetHungry(self):
        return self.__Hungry;

    def GetAlive(self):
        return self.__Alive;

    def GetDiet(self):
        return self.__Diet;

    def GetAnimal(self):
        return self.__Animal

#1. feladat:
Szafari = [Animals("Tiger", "Carnivorous"), Animals("Monkey", "Omnivorous"), Animals("Zebra", "Herbivorous")];
print("::2. TASK::")
#2. feladat:
for i in range(len(Szafari)):
    if(Szafari[i].GetDiet() == "Carnivorous"):
        Szafari[i].Hunting();
    elif(Szafari[i].GetDiet() == "Omnivorous"):
        Szafari[i].Moving();
    else:
        Szafari[i].Feeding();
print("::3. TASK::")
#3. feladat:
hungry = "hungry";
alive = "alive";
for i in range(len(Szafari)):
    if(not Szafari[i].GetHungry()):
        hungry = "not hungry";
    if(not Szafari[i].GetAlive()):
        alive = "not alive";

    print(f"The {Szafari[i].GetAnimal()} is {hungry} and he/she is {alive}");
print("::4. TASK::")
#4. feladat:
for i in range(len(Szafari)):
    Szafari[i].Moving();
    Szafari[i].Feeding();
    if(Szafari[i].GetDiet() == "Carnivorous"):
        Szafari[i].Hunting();
    if(Szafari[i].GetAlive() == False):
        print(f"The {Szafari[i].GetAnimal()} died due to hunger.");
print("::5. TASK::");
#5. feladat:
hungry = "hungry";
alive = "alive";
for i in range(len(Szafari)):
    if(not Szafari[i].GetHungry()):
        hungry = "not hungry";
    if(Szafari[i].GetAlive() == True):
        print(f"The {Szafari[i].GetAnimal()} is {hungry} and he/she is {alive}");