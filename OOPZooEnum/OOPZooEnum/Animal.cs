using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPZooEnum
{
    class Animal
    {
        static Random r = new Random();

        private string animalSpecies;
        private Diet diet;
        private bool isHungry;
        private bool isAlive;

        public string AnimalSpecies { get => animalSpecies; set => animalSpecies = value; }
        public bool IsHungry { get => isHungry; set => isHungry = value; }
        public bool IsAlive { get => isAlive; set => isAlive = value; }
        public Diet Diet { get => diet; set => diet = value; }

        public Animal(string animalSpecies, bool isHungry, bool isAlive, Diet diet)
        {
            AnimalSpecies = animalSpecies;
            IsHungry = isHungry;
            IsAlive = isAlive;
            Diet = diet;
        }

        public void Moving()
        {
            if (!IsHungry)
            {
                IsHungry = true;
            }
            else
            {
                IsAlive = false;
            }
        }
        public void Feeding()
        {
            if (IsHungry)
            {
                IsHungry = false;
            }
        }
        public void Hunting()
        {
            if (Diet == Diet.Carnivorous)
            {
                int succes = r.Next(1, 101);
                if (succes <= 45)
                {
                    IsHungry = false;
                }
                else
                {
                    Moving();
                }
            }
        }

        public override string ToString()
        {
            string hunger = isHungry ? "Hungry" : "Well fed";
            string alive = IsAlive ? "Alive" : "Dead";
            return $"Species: {animalSpecies}\t Diet: {Diet}\t Hunger condition: {hunger}\t Alive condition: {alive}";
        }
    }
}
