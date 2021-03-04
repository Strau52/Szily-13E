using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpBasics
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] tomb = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            int[] x = { 1, 9, 9, 7, 5, 1 };
            string[] tomb2 = { "én", "okos", "vagyok" };

            Console.WriteLine(EldontesParosE(x)?"Van benne páros szám!":"Nincs benne páros szám!");
            Console.WriteLine(LinerarisKeresesParos(x) == -1?"Nincs benne páros":"Van benne páros");
            Console.ReadKey();

            //bool visszatérésű feltétel?igaz ág:hamis ág
        }

        private static int Sorozatszamitas(int[] x)
        {
            int sum = 0;
            for (int i = 0; i < x.Length; i++)
            {
                sum += x[i];
            }

            return sum;
        }

        private static bool EldontesParosE(int[] x)
        {
            int i = 0;
            while (i < x.Length && x[i]%2 != 0)
            {
                i++;
            }
            bool van = i < x.Length;
            return van;
        }

        private static int KivalasztasParos(int[] x)
        {
            int i = 0;
            while (x[i] % 2 != 0)
            {
                i++;
            }
            int idx = i;
            return idx;
        }

        private static int LinerarisKeresesParos(int[] x)
        {
            int i = 0;
            while (i < x.Length && x[i] % 2 != 0)
            {
                i++;
            }
            bool van = i < x.Length;
            if (van)
            {
                int idx = i;
                return idx;
            }
            return -1;
        }

        private static int MegszamlalasParos(int[] x)
        {
            int db = 0;
            for (int i = 0; i < x.Length; i++)
            {
                if (x[i] % 2 == 0)
                {
                    db++;
                }
            }
            return db;
        }

        private static int MaximumKivalasztas(int[] x)
        {
            int max = 0;
            for (int i = 1; i < x.Length; i++)
            {
                if (x[i] > x[max])
                {
                    max = i;
                }
            }
            return max;
        }
    }
}
