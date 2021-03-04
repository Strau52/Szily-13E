using System;
using System.Collections.Generic;
using System.Text;

namespace dartsOOP
{
    class Circle
    {
        static private Random rnd = new Random();
        private int r;
        private int x;
        private int y;

        public Circle(int r)
        {
            this.r = r;
            this.x = rnd.Next(100);
            this.y = rnd.Next(100);
        }

        public Circle(int r, int x, int y)
        {
            this.r = r;
            this.x = x;
            this.y = y;
        }

        public bool IsInTheCircle(int x, int y)
        {
            return Math.Abs(this.x + r) >= Math.Abs(x) && Math.Abs(this.y + r) >= Math.Abs(y);
        }

        //AB => sqrt(pow(px-ox) + pow(py-oy))
        public double Distance(int x, int y)
        {
            double distance = Math.Sqrt(Math.Pow(x - this.x, 2) + Math.Pow(y - this.y, 2));
            //TODO: score
            return distance;
        }
        
    }
}