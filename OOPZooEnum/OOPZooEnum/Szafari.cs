using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPZooEnum
{
    class Szafari
    {
        Animal[] animals;
        public Animal[] Animals { get => animals; set => animals = value; }

        public Szafari(int numberOfAnimals)
        {
            this.animals = new Animal[numberOfAnimals];
        }

        public void AddAnimal(Animal newAnimal)
        {
            int i = 0;
            while (i < animals.Length && animals[i] != null)
            {
                i++;
            }
            if (i < animals.Length)
            {
                animals[i] = newAnimal;
            }
        }

        public void OneNormalDayPasses()
        {
            for (int i = 0; i < Animals.Length; i++)
            {
                switch (Animals[i].Diet)
                {
                    case Diet.Carnivorous:
                        Animals[i].Hunting();
                        break;
                    case Diet.Omnivorous:
                        Animals[i].Moving();
                        break;
                    case Diet.Herbivorous:
                        Animals[i].Feeding();
                        break;
                }
                Console.WriteLine(Animals[i]);
            }
        }

        public override string ToString()
        {
            int counter = 0;
            for (int i = 0; i < animals.Length; i++)
            {
                if (animals[i].IsAlive)
                {
                    counter++;
                }
            }
            return $"Animals alive: {counter}";
        }
    }
}
