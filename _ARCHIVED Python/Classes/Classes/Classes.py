class Hallgato():
    __Name = None;
    __Age = None;
    __Department = None;

    def __init__(self, name, age, department):
        self.__Name = name;
        self.__Age = age;
        self.__Department = department;

    def displaySelfDetails(self):
        print("Name: ", self.__Name);
        print("Age: ", self.__Age);
        print("Department: ", self.__Department);

obj = Hallgato("Gergő", 22, "Tanár");

obj.displaySelfDetails();




#16. Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap egy egész számot és eldönti a számról, hogy osztható-e 2-vel és 3-mal is egyszerre! 
#A programodban hívd is meg ezt az alprogramot!
def oszthatoE(szam):
    return (szam%2==0)and(szam%3==0);
#17. Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap három számot és eldönti, hogy az összes paramétere pozitív-e!
#A programodban hívd is meg ezt az alprogramot!
def pozitivE(elso,masodik,harmadik):
    return (elso%2==0)and(masodik%2==0)and(harmadik%2==0);
#18. Írj egy Python függvényt, amely paraméterként kap 2 egész számot és visszatér a két szám által meghatározott zárt intervallumban található egész számok összegével! 
#A programodban hívd is meg ezt az alprogramot!
def intervallum(elso,masodik):
    osszeg = 0;
    for x in range(elso,masodik+1):
        osszeg+=x;
    return osszeg;
#19. Írj egy Python eljárást, amely paraméterként kap egy szót (sztringet) és annyi darab csillag (*) karaktert ír ki a képernyőre, ahány karaktert tartalmazott a szó! 
#A programodban hívd is meg ezt az alprogramot!
def csillag(szoveg):
    rejtett = "";
    for x in range(len(szoveg)):
        rejtett += "*";
    return rejtett;

print(":: TESZTELÉSEK ::");
print("16. feladat teszt: ");
print("A 6 oszható 2-vel és 3-al egyszerre? Az állítás:", oszthatoE(6));
print("A 8 oszható 2-vel és 3-al egyszerre? Az állítás:", oszthatoE(8));

print("17. feladat teszt: ");
print("A 2,4,6 számsor összes tagja pozitív? Az állítás:", pozitivE(2,4,6));
print("Az 1,3,4 számsor összes tagja pozitív? Az állítás:", pozitivE(1,3,4));

print("18. feladat teszt: ");
print("Az 1-től 5-ig tartó zárt intervallumban lévő számok összege: ", intervallum(1,5));

print("19. feladat teszt: ");
print("A bemenet 'valami', a kiement:",csillag("valami"));

