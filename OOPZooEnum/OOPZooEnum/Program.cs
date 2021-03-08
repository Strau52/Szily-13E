using System;

namespace OOPZooEnum
{
    class Program
    {
        static void Main(string[] args)
        {
            Szafari szafari = new Szafari(3);

            szafari.AddAnimal(new Animal("Tiger", false, true, Diet.Carnivorous));
            szafari.AddAnimal(new Animal("Monkey", false, true, Diet.Omnivorous));
            szafari.AddAnimal(new Animal("Zebra", false, true, Diet.Herbivorous));
            //Obviusly missing.
            szafari.AddAnimal(new Animal("Tiger 2.0", false, true, Diet.Carnivorous));

            Console.WriteLine("After a day");
            szafari.OneNormalDayPasses();
            Console.WriteLine(szafari);
            Console.WriteLine("After moving the data of the dead animals: ");
            for (int i = 0; i < szafari.Animals.Length; i++)
            {
                szafari.Animals[i].Moving();
                if (!szafari.Animals[i].IsAlive)
                {
                    Console.WriteLine(szafari.Animals[i]);
                }
            }
            Console.WriteLine(szafari);
            for (int i = 0; i < szafari.Animals.Length; i++)
            {
                if (szafari.Animals[i].IsAlive)
                {
                    Console.WriteLine(szafari.Animals[i]);
                }
            }
        }
    }
}
