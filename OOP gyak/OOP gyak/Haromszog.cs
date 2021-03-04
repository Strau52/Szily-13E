using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP_gyak
{
    class Haromszog
    {
        private double a, b, c;
        public Haromszog()
        {
            Random r = new Random();
            do
            {
                a = r.Next(0, 101);
                b = r.Next(0, 101);
                c = r.Next(0, 101);

            } while (!SzerkeszthetoEzAHaromszog());
        }

        private bool SzerkeszthetoEzAHaromszog()
        {
            return (a + b > c) && (a + c > b) && (b + c > a);
        }

        public double Kerulet()
        {
            return a + b + c;
        }

        public double Terulet() 
        {
            double s = Kerulet() / 2;
            return Math.Sqrt(s * (s - a) * (s - b) * (s - c));
        }
    }
}
