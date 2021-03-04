#print("Hello world!");

#elsoValtozo = 1;            #int valami = 1
#masodikValtozo = 3.1415926535897;          #double valami = 2.0;
#harmadikValtozo = "Harmadik változó vagyok!";       #string valami = "szöveg";

#print(elsoValtozo, masodikValtozo, harmadikValtozo, sep=',');

#print(elsoValtozo * masodikValtozo);

#input(prompt) adatbekérés
# print() kiírás

#a = float (input ("Kérek egy számot: "));
#b = float (input ("Kérem a második számot: "));

#print("A két szám szorzata: ", a * b);

#name = input("Kérlek add meg a neved: ");
#print("Üdvözöllek kedves ", name, "!");

# a = b; -> értékeadó operátor
# a == b -> érték ellenörző operátor
# ==, !=, <, <=, >, >=

#elágazások

#a = float (input ("Kérek egy számot: "));
#b = float (input ("Kérem a második számot: "));
#if b > a:
#    print("A második szám nagyobb volt");
#elif a == b:
#    print("A két szám egyenlő");
#else:
#    print("Az első szám volt a nagyobb");

#Ciklusok (iterációk)

#while <expression>
# <statemnt's>


#words = ['diák', 'tanár', 'eszköz'];
#print(len(words));

#for word in words:
#    print(word, len(word))

#for i in range(-10, -100, -20):
#    print(i);


#words = ['diák', 'tanár', 'eszköz', 'asd', 'qwerty'];
#print(words[2]);
#for i in range(len(words)):
#    print(i,words[i]);

#color = ['red', 'blue', 'green'];
#fruits = ['apple', 'banana','cherry'];
#for i in color:
#    for j in fruits:
#        print(i,j);

#myList = ['apple', 'banana','cherry'];
#myList = [11,22,33,44,55,66,77,88,99];
#for i in range(2,5):
#    print(myList[i]);

#def fuggveny(parameter):
#   **kód**
#   **még több kód**
#   print("valamit");
#   return none;

#def Hello():
#    print("Hello");

#def HelloName(name):
#    print("Hello ", name);

#Hello();
#HelloName("Gergő");

#def Abs(num):
#    if num >= 0:
#        return num;
#    else:
#        return -num;

#num = float(input("Adj meg egy számot: "));
#print(Abs(num));

#window.bgcolor("white");
#window.setup(350,350);
#window.title("Első rajzom");

#bela.pencolor("black");

#import turtle;

#window = turtle.Screen();
#bela = turtle.Turtle();
#window.setup(500,500);
#window.bgcolor("white");
#window.title("Ötszög rajzolás");

#for i in range(5):
#    bela.fd(100);
#    bela.left(144);

#import turtle;

#window = turtle.Screen();
#bela = turtle.Turtle();
#window.setup(500,500);
#window.bgcolor("black");
#window.title("Színes rajzolás");

#colors = ['red','orange','green','yellow','blue','purple'];
#pen = turtle.Pen();

#for i in range(180):
#    pen.pencolor(colors[i%6]);
#    pen.width(i/100+1);
#    pen.fd(i);
#    pen.left(59);

#import turtle;

#window = turtle.Screen();
#window.setup(600,600);
#window.bgcolor("white");
#window.title("Coordinate table");

#t = turtle.Turtle();
#t.pencolor("black");

## The python turtle shapes are:
#t.shape('arrow')
#t.shape('turtle')
#t.shape('circle')
#t.shape('square')
#t.shape('triangle')
#t.shape('classic')


#t.speed(0);

#for x in range(12):
#    t.lt(90);
#    t.fd(20);
#    t.rt(90);
#    t.fd(5);
#    t.bk(5);
#t.penup();
#t.goto(0,0);

#for x in range(12):
#    t.pendown();
#    t.fd(20);
#    t.lt(90);
#    t.fd(5);
#    t.bk(5);
#    t.rt(90);
#t.penup();
#t.goto(0,0);

#for x in range(12):
#    t.pendown();
#    t.bk(20);
#    t.lt(90);
#    t.fd(5);
#    t.bk(5);
#    t.rt(90);
#t.penup();
#t.goto(0,0);

#for x in range(12):
#    t.pendown()
#    t.rt(90)
#    t.fd(20)
#    t.lt(90)
#    t.fd(5)
#    t.bk(5)
#t.penup();
#t.goto(0,0);

#t.goto(250,0);
#t.write("x");
#t.goto(0,250);
#t.write("y");
#t.goto(0,0);

#window.exitonclick();

##Sorozatszámítás
#szam = [3,6,1,8,4];
#ertek = 0;

#for i in range(len(szam)):
#    ertek += szam[i];

#print(ertek);


def szamologep():
    
    elsoszam = int(input('Add meg az első számot: '))
    muveletek = input('''
Kérlek válassz egy müveletet:
+ összeadás
- kivonás 
* szorzás
/ osztás
A választásod: ''')
    masodikszam = int(input('Add meg a második számot: '))
    
    def osszeadas():
        if muveletek =='+':
            print(elsoszam,'+',masodikszam,"=",elsoszam + masodikszam)
    osszeadas()

    def kivonas():
        if muveletek =='-':
            print(elsoszam,'-',masodikszam,"=",elsoszam - masodikszam)
    kivonas()

    def szorzas():
        if muveletek =='*':
            print(elsoszam,'*',masodikszam,"=",elsoszam * masodikszam)
    szorzas()

    def osztas():
        if muveletek == '/':
            print(elsoszam,'/',masodikszam,"=",elsoszam / masodikszam)
    osztas()
    ujra()

def ujra():
    ujrakalkula = input('''
Szeretnél újra pörgetni?
Ha igen nyomd meg az: I
Ha nem nyomd meg a: N
A választásod: ''')
    if ujrakalkula == 'I' or ujrakalkula=='i':
        szamologep()
    elif ujrakalkula == 'N' or ujrakalkula == 'n':
        print('Viszlát')

    else: ujra()

szamologep()