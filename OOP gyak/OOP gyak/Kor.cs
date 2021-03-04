using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP_gyak
{
    class Kor
    {
        private Random rnd = new Random();
        private int x, y, r;

        public Kor(int x, int y, int r)
        {
            this.x = x;
            this.y = y;
            this.r = r;
        }

        public Kor(int r)
        {
            x = rnd.Next(0, 20);
            y = rnd.Next(0, 20);
            this.r = r;
        }

        public bool BenneVanE(int x, int y)
        {
            return this.x + r >= Math.Abs(x) && this.y + r >= Math.Abs(y);
        }

        public double Tavolsag(int x, int y)
        {
            int a = x - this.x;
            int b = y - this.y;
            return Math.Sqrt((Math.Pow(a, 2) + Math.Pow(b, 2)));
        }
    }
}
