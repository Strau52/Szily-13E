using System;

namespace OOPHF
{
    class Program
    {
        static int[] data;
        static Random r = new Random();
        static void Main(string[] args)
        {
            Init();
            Console.WriteLine(":: RAW DATA :: ");
            for (int i = 0; i < data.Length; i++)
            {
                Console.Write($"{data[i]} ");
            }
            Console.WriteLine("\r\n :: TASK 1 ::");
            Console.WriteLine(TaskOne() ? "There was a flat place" : "There was not a flat place");
            Console.WriteLine(":: TASK 2 ::");
            Console.WriteLine($"There was {TaskTwo()} platoon where the heigh dropped");
            Console.WriteLine(":: TASK 3 ::");
            Console.WriteLine($"The total level rise was: {TaskThree()}");
            Console.WriteLine(":: TASK 4 ::");
            Console.WriteLine($"The max times that we were on a continuos rise was {TaskFourStr()} times");
            Console.WriteLine(":: TASK 5 ::");
            Console.WriteLine($"The maximum rising in one measurment was {TaskFive()}");
            Console.ReadKey();
        }

        private static string TaskFourStr()
        {
            int tempRise = 0;
            int maxRise = -1;
            string tempValue = "";
            string returnValue = "";
            for (int i = 0; i < data.Length - 1; i++)
            {
                if (data[i] < data[i + 1])
                {
                    tempRise++;
                    tempValue += $"[{data[i]} - {data[i + 1]}] ";
                }
                else
                {
                    if (tempRise > maxRise)
                    {
                        maxRise = tempRise;
                        returnValue = $"{tempValue} which means {tempRise} times";
                    }
                    tempRise = 0;
                    tempValue = "";
                }
            }
            return returnValue;
        }

        private static int TaskFive()
        {
            int maxRising = -1;
            int tempRising = 0;

            for (int i = 0; i < data.Length - 1; i++) 
            {
                if (data[i] < data[i + 1])
                {
                    tempRising = data[i + 1] - data[i];
                }

                if (tempRising > maxRising)
                {
                    maxRising = tempRising;
                }
                else
                {
                    tempRising = 0;
                }
            }

            return maxRising;
        }

        private static int TaskFour()
        {
            int tempRise = 0;
            int maxRise = -1;
            for (int i = 0; i < data.Length - 1; i++)
            {
                if (data[i] < data[i + 1])
                    tempRise++;
                else
                {
                    if (tempRise > maxRise)
                    {
                        maxRise = tempRise;
                        tempRise = 0;
                    }
                    else
                    {
                        tempRise = 0;
                    }
                }
            }
            return maxRise;
        }

        private static int TaskThree()
        {
            int rise = 0;
            for (int i = 0; i < data.Length - 1; i++)
            {
                if (data[i] < data[i + 1])
                    rise += data[i + 1] - data[i];
                    //rise += Math.Abs(data[i]-data[i-1]);
            }
            return rise;
        }

        private static int TaskTwo()
        {
            int count = 0;
            for (int i = 0; i < data.Length-1; i++)
            {
                if (data[i] > data[i + 1])
                    count++;
            }
            return count;
        }

        private static bool TaskOne()
        {
            int i = 0;
            while (i < (data.Length -1) && data[i] != data[i + 1])
                i++;
            return i < (data.Length - 1);
        }

        private static void Init()
        {
            data = new int[50];
            for (int i = 0; i < data.Length; i++)
            {
                data[i] = r.Next(-50, 1000);
                //data[i] = r.Next(1, 10);
            }
        }
    }
}
