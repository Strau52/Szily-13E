using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPinCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            //1. módszer
            Animals[] szafari = { new Animals("Tiger", "Carnivorous"), new Animals("Monkey", "Omnivorous"), new Animals("Zebra", "Herbivorous") };
            //2. módszer
            /*Animals tiger = new Animals("Tiger", "Carnivorous");
            Animals monkey = new Animals("Monkey", "Omnivorous");
            Animals zebra = new Animals("Zebra", "Herbivorous");
            Animals[] szafari = { tiger, monkey, zebra };*/
            //3-4. módszer
            //Animals[] szafari = new Animals[3];
            //Animals tiger = new Animals("Tiger", "Carnivorous");
            //Animals zebra = new Animals("Zebra", "Herbivorous");
            //szafari[0] = tiger;
            //szafari[1] = new Animals("Monkey", "Omnivorous");
            //szafari[2] = zebra;
            //Console.WriteLine("FIRST");
            //for (int i = 0; i < szafari.Length; i++)
            //{
            //    Console.WriteLine("::BEFORE::\r\nData of {0}: \tDiet: {1}\r\n\tStatus of hunger: {2}\r\n\tIs alive: {3}", szafari[i].Animal, szafari[i].Diet, szafari[i].IsHungry?"Hungry":"not hungry", szafari[i].IsAlive?"Alive":"Ded");
            //    if (szafari[i].Diet == "Carnivorous")
            //    {
            //        szafari[i].Hunting();
            //    }else if(szafari[i].Diet == "Omnivorous")
            //    {
            //        szafari[i].Moving();
            //    }
            //    else
            //    {
            //        szafari[i].Feeding();
            //    }
            //    Console.WriteLine("::AFTER::\r\nData of {0}: \tDiet: {1}\r\n\tStatus of hunger: {2}\r\n\tIs alive: {3}\r\n", szafari[i].Animal, szafari[i].Diet, szafari[i].IsHungry ? "Hungry" : "not hungry", szafari[i].IsAlive ? "Alive" : "Ded");
            //}
            //Console.WriteLine("SECOND");
            //for (int i = 0; i < szafari.Length; i++)
            //{
            //    szafari[i].Moving();
            //    if (szafari[i].IsAlive)
            //    {
            //        szafari[i].Feeding();
            //        if (szafari[i].Diet == "Carnivorous")
            //        {
            //            szafari[i].Hunting();
            //        }
            //        Console.WriteLine($"Data of { szafari[i].Animal}: \tDiet: { szafari[i].Diet}\r\n\tStatus of hunger: { szafari[i].IsHungry}\r\n\tIs alive: { szafari[i].IsAlive}");
            //    }
            //    else
            //    {
            //        Console.WriteLine($"Data of { szafari[i].Animal}: \tDiet: { szafari[i].Diet}\r\n\tStatus of hunger: { szafari[i].IsHungry}\r\n\tIs alive: { szafari[i].IsAlive}");
            //    }
            //}

             


            Console.ReadKey();
        }
    }
}
