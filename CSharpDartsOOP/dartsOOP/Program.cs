using System;

namespace dartsOOP
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.Write("Please give me the x coordinate of teh Origo: ");
            //int x = Convert.ToInt32(Console.ReadLine()); //int.Parse, IMPLICIT TÍPUS CASTOLÁS => (int)Console.ReadLine();
            //Console.Write("Please give me the y coordinate of teh Origo: ");
            //int y = Convert.ToInt32(Console.ReadLine());
            //Console.Write("Please give me the range of the circle: ");
            //int r = Convert.ToInt32(Console.ReadLine());

            //Circle circle = new Circle(r, x, y);
            Circle circle = new Circle(5);
            int tempX, tempY, remeainingShoots = 15;

            do
            {
                Console.Clear();
                Console.WriteLine($"You have {circle.Score} point!\r\n");
                Console.WriteLine($"You still have {remeainingShoots} bullet!\r\n");
                Console.Write("Please give me an x coordinate: ");
                tempX = Convert.ToInt32(Console.ReadLine());
                Console.Write("Please give me an y coordinate: ");
                tempY = Convert.ToInt32(Console.ReadLine());
                //Console.WriteLine(circle.IsInTheCircle(tempX, tempY) ? "The point is in the circle" : "The point is not in the circle");
                //} while (Console.ReadKey().Key != ConsoleKey.Escape);
                circle.Distance(tempX, tempY);
                //TODO: get the score, get help with the distance
                remeainingShoots--;
            } while (remeainingShoots > 0);
            
        }
    }
}
