using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CShaprOOPTriangle
{
    class Program
    {
        static void Main(string[] args)
        {
            //Triangle a = new Triangle(7, 8, 9);
            //Triangle r = new Triangle();
            //Triangle a1 = new Triangle(3, 4, 5);
            //Triangle r1 = new Triangle();

            int a, b, c;
            do
            {
                Console.Clear();
                //Console.SetCursorPosition(0, 0);
                Console.Write("Please add the sides of the triangle: \r\nA: ");
                a = Convert.ToInt32(Console.ReadLine());
                Console.Write("B: ");
                b = Convert.ToInt32(Console.ReadLine());
                Console.Write("C: ");
                c = Convert.ToInt32(Console.ReadLine());
            } while (!(a < b + c) && (b < a + c) && (c < a + b));
            Triangle myTriangle = new Triangle(a, b, c);
            Console.WriteLine($"Is my triangle editable? {myTriangle.IsEditable()}");
            Console.ReadKey();
        }
    }
}