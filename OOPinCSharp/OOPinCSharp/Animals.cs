using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPinCSharp
{
    class Animals
    {
        static Random r = new Random();

        private string animal;
        private string diet;
        private bool isHungry;
        private bool isAlive;
        public string Animal
        {
            get { return animal; }
            private set { animal = value; }
        }
        public string Diet
        {
            get { return diet; }
            private set { diet = value; }
        }
        public bool IsHungry
        {
            get { return isHungry; }
            private set { isHungry = value; }
        }
        public bool IsAlive
        {
            get { return isAlive; }
            private set { isAlive = value; }
        }

        public Animals(string animal, string diet)
        {
            Animal = animal;
            Diet = diet;
            IsHungry = false;
            IsAlive = true;
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
            if (Diet == "Carnivorous")
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
    }
}
