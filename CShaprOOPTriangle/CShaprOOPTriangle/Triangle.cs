using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CShaprOOPTriangle
{
    class Triangle
    {
        //double a;
        static Random r = new Random();
        public int A { get; set; }
        public int B { get; set; }
        public int C { get; set; }

        public Triangle(int a, int b, int c)
        {
            //this.a = a;
            A = a;
            B = b;
            C = c;
        }
        public Triangle()
        {
            do
            {
                A = r.Next(0, 101);
                B = r.Next(0, 101);
                C = r.Next(0, 101);
            } while (!IsEditable());
        }

        public bool IsEditable()
        {
            return (A < B + C) && (B < A + C) && (C < A + B);
        }

        public double District()
        {
            return A + B + C;
        }

        public double Area()
        {
            double s = District() / 2;
            return Math.Sqrt(s * (s - A) * (s - B) * (s - C));
        }
    }
}
