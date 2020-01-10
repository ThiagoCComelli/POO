using System;
using System.Collections.Generic;

namespace POO
{
	class Program
	{
		static void Main()
        {
			List<Viagem> lista = new List<Viagem>();
			Viagem roma = new Viagem("Roma","10/03/2019", "12/05/2019");
			Viagem istambul = new Viagem("Istanbul", "14/06/2019", "12/07/2019");

			lista.Add(roma);
			lista.Add(istambul);

			roma.setViajantes(3);
			roma.setFebre(false);
			roma.setValor(2000);
			roma.setEstadia(1000);
			roma.setSeguro(120);

			istambul.setViajantes(2);
			istambul.setFebre(true);
			istambul.setValor(2500);
			istambul.setEstadia(1200);
			istambul.setSeguro(150);

			roma.getStatus();
			istambul.getStatus();

			Console.WriteLine("Viagem mais barata no total: {0}",maisBarato(lista,0).getNome());
			Console.WriteLine("Viagem mais barata no individual: {0}",maisBarato(lista,1).getNome());

			roma.setViajantes(2);

			Console.WriteLine("Viagem mais barata no total: {0}", maisBarato(lista, 0).getNome());
			Console.WriteLine("Viagem mais barata no individual: {0}", maisBarato(lista, 1).getNome());

		}

		static Viagem maisBarato(List<Viagem> lista,int x)
		{
			Viagem barato = lista[0];
			foreach(Viagem i in lista)
			{
				if (i.getCusto(x) < barato.getCusto(x))
				{
					barato = i;
				}
			}
			return barato;
		}


	}

	class Viagem
	{
		private string nome,datai,dataf;
		private double valor, estadia, seguro;
		private int qtde;
		private bool febre;

		public Viagem(string nome1,string data1,string data2)
		{
			nome = nome1;
			datai = data1;
			dataf = data2;
		}

		public void setViajantes(int x)
		{
			qtde = x;
		}

		public void setFebre(bool x)
		{
			febre = x;
		}

		public void setValor(double x)
		{
			valor = x;
		}

		public void setEstadia(double x)
		{
			estadia = x;
		}

		public void setSeguro(double x)
		{
			seguro = x;
		}

		public string getNome()
		{
			return nome;
		}

		public double getCusto(int x)
		{
			double custo;
			if(x == 0)
			{
				custo = (estadia + seguro + valor) * qtde;
			} else
			{
				custo = (estadia + seguro + valor);
			}
			return custo;
		}

		public void getStatus()
		{
			Console.WriteLine("Destino: {0}\nData de inicio: {1}\nData de fim: {2}\nFebre: {3}\n" +
				"Valor das passagens: {4}\nValor da estadia: {5}\nValor do seguro: {6}\n" +
				"Viajantes: {7}\nCusto total: {8}\n",nome,datai,dataf,febre,valor,estadia,seguro,qtde,getCusto(0));
		}


		

	}
}
