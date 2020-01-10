using System;
using System.Collections.Generic;

namespace POO
{
    class Program
    {
        static void Main()
        {
            List<Computador> lista = new List<Computador>();
            Computador computador0 = new Computador(2000);
            Computador computador1 = new Computador(2500);
            Computador computador2 = new Computador(1500);

            lista.Add(computador0);
            lista.Add(computador1);
            lista.Add(computador2);
            
            computador0.setWindows();
            computador0.setNeon();
            computador1.setLinux();

            Percorre(lista);

        }
        static void Percorre(List<Computador>lista)
        {
            foreach (Computador i in lista)
            {
                Console.WriteLine("Computador R${0}: {1}",i.preco,i.getStatus());
            }
        }
    }

    public struct Gadget
    {
        public int preco;
        public string nome;

        public Gadget(int preco0, string nome0)
        {
            preco = preco0;
            nome = nome0;
        }
    }

    class Computador
    {
        public int preco;
        private List<Gadget> lista = new List<Gadget>();
        private Gadget gadget;

        public Computador(int x)
        {
            preco = x;
        }

        public void setLinux()
        {
            lista.Add(new Gadget(2, "Linux"));
        }
        public void setWindows()
        {
            lista.Add(new Gadget(500, "Windows"));
        }
        public void setNeon()
        {
            lista.Add(new Gadget(100, "Neon"));
        }
        public string getStatus()
        {
            string nome = "| ";
            foreach(Gadget i in lista)
            {
                nome += i.nome + " | ";
                preco += i.preco;
            }
            nome += "\n";
            return nome;
        }
    }
}