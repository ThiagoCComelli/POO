using System;
using System.Collections.Generic;

namespace POO
{
    class Program
    {
        static void Main()
        {
            List<Funcinario> lista = new List<Funcinario>();
            Funcinario bob = new Funcinario("Bob",23,3900);
            Funcinario tom = new Funcinario("Tom",27,1200);
            Funcinario tonim = new Funcinario("Tonim",27,10000);

            lista.Add(bob);
            lista.Add(tom);
            lista.Add(tonim);

            bob.setCargo("Vendedor");
            tom.setCargo("Vendedor");
            tonim.setCargo("Gerente");

            bob.setVendas(1000);
            tom.setVendas(5000);
            tonim.setVendas(1500);

            bob.darAumento(10);
            tom.darAumento(5);

            status(lista);

        }

        static void status(List<Funcinario> list)
        {
            foreach(Funcinario i in list)
            {
                Console.WriteLine("Nome: {0}\nIdade: {1}\nCargo: {2}\nVendas: {3:0.00}\nSalario base: {4:0.00}\n" +
                    "Comissao: {5:0.00}\nImposto: {6:0.00}\nSalario final: {7:0.00}\n", i.nome,i.idade,i.cargo,i.vendas,i.salario,i.calcComissao(),i.calcImposto(),i.calcSalario());
            }
        }
    }

    class Funcinario
    {
        public string nome,cargo;
        public double salario,vendas;
        public int idade;

        public Funcinario(string nome0,int idade0,int salario0)
        {
            nome = nome0;
            idade = idade0;
            salario = salario0;
        }

        public void setCargo(string x)
        {
            cargo = x;
        }

        public void setVendas(double x)
        {
            vendas = x;
        }

        public void darAumento(double percentual)
        {
            salario *= percentual/100;
        }

        public double calcImposto()
        {
            double imp;
            if (0 <= salario && salario <= 1000)
            {
                imp = .05;
            } else if (1000 < salario && salario <= 5000)
            {
                imp = .08;
            } else if (5000 < salario && salario <= 10000)
            {
                imp = .12;
            } else
            {
                imp = .2;
            }
            return salario * imp;
        }

        public double calcComissao()
        {
            return vendas * 0.04;
        }

        public double calcSalario()
        {
            return salario + calcComissao() - calcImposto();
        }
    }
}
