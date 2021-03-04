#Készíts egy Diák/Student osztályt ami konstruktorból kap jegyeket különböző tárgyakhoz. Legyen a Diáknak egy neve, osztálya, 
#és legyen egy metódusa ami visszaadja az átlagait tárgyak alapján.
import random;

class Student():
    __Name = None;
    __Class = None;
    __Math = None;
    __English = None;
    __IT = None;

    def __init__(self, name, classr):
        self.__Name = name;
        self.__Class = classr;
        math = [];
        eng = [];
        it = [];
        for i in range(0,10):
            math.append(random.randint(1,5));
            eng.append(random.randint(1,5));
            it.append(random.randint(1,5));
        self.__Math = math;
        self.__English = eng;
        self.__IT = it;

    def __getAVG(self, t):
        sum = 0;
        for i in range(len(t)):
            sum += t[i];
        return sum / len(t);

    def GetAvg(self):
        return f"The avg of math: {self.__getAVG(self.__Math)}, The avg of english: {self.__getAVG(self.__English)} The avg of IT: {self.__getAVG(self.__IT)}";

    def GetName(self):
        return self.__Name;

    def GetClass(self):
        return self.__Class;

    def GetGradesBySubject(self, t):
        result = " ";
        for i in range(len(t)):
            result += (str(t[i]));
            result += ",";
        return result;



a = Student("János", "13/E");
print(f"{a.GetName()} math grades: {a.GetGradesBySubject(a._Student__Math)}");
print(a.GetAvg());
