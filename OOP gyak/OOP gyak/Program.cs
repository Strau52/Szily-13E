using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP_gyak
{
    class Program
    {
        static void Main(string[] args)
        {
            Kor kor = new Kor(0, 0, 5);
            Console.WriteLine($"{kor.BenneVanE(-5, -5)},{kor.BenneVanE(5, 0)}, {kor.BenneVanE(5, 5)}");

            Console.ReadKey();
        }
    }
}
